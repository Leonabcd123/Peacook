import pygame

class Starting_Room:
    def __init__(self, player):
        self.rect = pygame.Rect(175, 175, 450, 450)
        self.player = player

    def update(self):
        if self.player.rect.right > self.rect.right:
            self.player.rect.right = self.rect.right
            self.player.velocity = pygame.math.Vector2(0, 0)
        if self.player.rect.left < self.rect.left:
            self.player.rect.left = self.rect.left
            self.player.velocity = pygame.math.Vector2(0, 0)
        if self.player.rect.bottom > self.rect.bottom:
            self.player.rect.bottom = self.rect.bottom
            self.player.velocity = pygame.math.Vector2(0, 0)
        if self.player.rect.top < self.rect.top:
            self.player.rect.top = self.rect.top
            self.player.velocity = pygame.math.Vector2(0, 0)