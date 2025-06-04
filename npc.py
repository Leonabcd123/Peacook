import pygame

class NPC:
    def __init__(self, x, y, font, screen):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.speed_x = 0
        self.speed_y = 0
        self.font = font
        self.screen = screen

    def move(self, direction, amount):
        pygame.time.delay(1)
        if direction == "right":
            self.speed_x -= amount
        elif direction == "left":
            self.speed_x += amount
        elif direction == "up":
            self.speed_y -= amount
        else:
            self.speed_y += amount

    def talk(self, text):
        lines = text.split("\n")
        y_offset = 700
        for line in lines:
            line_surface = self.font.render(line, True, (0, 0, 0))
            line_rect = line_surface.get_rect(center=(400, y_offset))
            self.screen.blit(line_surface, line_rect)
            y_offset += line_surface.get_height() + 5

    def update(self, color, surface, offset):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.speed_x = 0
        self.speed_y = 0

        visible_area = pygame.Rect(offset[0], offset[1], surface.get_width(), surface.get_height())
        if self.rect.colliderect(visible_area):
            local_rect = self.rect.move(-offset[0], -offset[1])
            pygame.draw.rect(surface, color, local_rect)