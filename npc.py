from utilities import *
from constants import *

class NPC:
    def __init__(self, x, y, screen):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed_x = 0.0
        self.speed_y = 0.0
        self.screen = screen
        self.started_talking = False
        self.start_unroll_time = 0
        self.talking_phase = 0
        self.skipped = False
        self.closed = False

    def move(self, direction, amount):
        if direction == "right":
            self.speed_x += amount
        elif direction == "left":
            self.speed_x -= amount
        elif direction == "up":
            self.speed_y -= amount
        elif direction == "down":
            self.speed_y += amount

    def talk(self, text, visible_width, skipped):
        if skipped and visible_width >= scroll_width:
            self.talking_phase += 1
            self.closed = False
            skipped = False

        if self.talking_phase == len(text):
            visible_width, self.closed = unroll_scroll(text, visible_width, self.talking_phase - 1, self.closed)
            return visible_width, skipped
        
        parts = text[self.talking_phase]
        lines = parts.split("\n")
        
        text_surface = pygame.Surface((scroll_width, scroll_height), pygame.SRCALPHA)
        text_surface.fill((0, 0, 0, 0))

        y_offset = 10
        for line in lines:
            line_surf = font1.render(line, True, (0, 0, 0))
            text_surface.blit(line_surf, (10, y_offset))
            y_offset += line_surf.get_height() + 5

        if visible_width < scroll_width:
            visible_width += unroll_speed

        handle_width = 20
        pygame.draw.rect(self.screen, HANDLE_COLOR, (scroll_x - handle_width, scroll_y, handle_width, scroll_height))
        scroll_rect = pygame.Rect(scroll_x, scroll_y, visible_width, scroll_height)
        pygame.draw.rect(self.screen, SCROLL_COLOR, scroll_rect)
        pygame.draw.rect(self.screen, HANDLE_COLOR, (scroll_rect.right, scroll_y, handle_width, scroll_height))
        pygame.draw.rect(self.screen, (160, 82, 45), scroll_rect, 3)

        self.screen.blit(text_surface, (scroll_x, scroll_y), area=pygame.Rect(0, 0, visible_width, scroll_height))

        return visible_width, skipped



    def update(self, color, surface, offset):
        self.pos.x += self.speed_x
        self.pos.y += self.speed_y

        self.rect.center = (round(self.pos.x), round(self.pos.y))

        self.speed_x = 0.0
        self.speed_y = 0.0

        visible_area = pygame.Rect(offset[0], offset[1], surface.get_width(), surface.get_height())
        if self.rect.colliderect(visible_area):
            local_rect = self.rect.move(-offset[0], -offset[1])
            pygame.draw.rect(surface, color, local_rect)
