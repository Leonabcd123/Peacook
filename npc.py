from utilities import *
from constants import *

class NPC(pygame.sprite.Sprite):
    def __init__(self, x, y, screen, color):
        super().__init__()
        self.image = pygame.image.load("peacock1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect(center=(x, y))
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed_x = 0.0
        self.speed_y = 0.0
        self.screen = screen
        self.started_talking = False
        self.start_unroll_time = 0
        self.talking_phase = 0
        self.skipped = False
        self.closed = False
        self.index = 0
        self.rows = 0
        self.done = False
        self.last_update = pygame.time.get_ticks()
        self.color = color

    def move(self, direction, amount):
        if direction == "right":
            self.speed_x += amount
        elif direction == "left":
            self.speed_x -= amount
        elif direction == "up":
            self.speed_y -= amount
        elif direction == "down":
            self.speed_y += amount

    def talk(self, text, visible_width, skipped, skipped_animation):
        if skipped and visible_width == scroll_width:
            self.talking_phase += 1
            self.closed = False
            self.done = False
            self.index = 0
            self.rows = 0
            skipped = False
            skipped_animation = False

        if self.talking_phase == len(text):
            visible_width, self.closed = unroll_scroll(text, visible_width, self.talking_phase - 1, self.closed)
            return visible_width, skipped, skipped_animation
        
        now = pygame.time.get_ticks()
        lines = text[self.talking_phase].split("\n")

        text_surface = pygame.Surface((scroll_width, scroll_height), pygame.SRCALPHA)
        text_surface.fill((0, 0, 0, 0))

        y_offset = 10

        if not skipped_animation:
            for i in range(self.rows):
                line_surf = font1.render(lines[i], True, (0, 0, 0))
                text_surface.blit(line_surf, (10, y_offset))
                y_offset += line_surf.get_height() + 5

            if self.rows < len(lines):
                partial_line = lines[self.rows][:self.index]
                line_surf = font1.render(partial_line, True, (0, 0, 0))
                text_surface.blit(line_surf, (10, y_offset))
                y_offset += line_surf.get_height() + 5
        else:
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

        if visible_width >= scroll_width and not self.done and now > self.last_update + typewriter_speed:
            self.last_update = now
            self.index += 1
            if self.index > len(lines[self.rows]):
                self.index = 0
                self.rows += 1
                if self.rows >= len(lines):
                    self.done = True

        return visible_width, skipped, skipped_animation



    def update(self, **kwargs):
        self.pos.x += self.speed_x
        self.pos.y += self.speed_y

        self.rect.center = (round(self.pos.x), round(self.pos.y))

        self.speed_x = 0.0
        self.speed_y = 0.0
