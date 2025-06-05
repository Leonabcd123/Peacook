import pygame

class Starting_Room:
    def __init__(self, player):
        self.img = pygame.image.load("room.webp").convert_alpha()
        self.img = pygame.transform.scale(self.img, (450, 450))
        self.rect = self.img.get_rect(topleft=(175, 175))
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