import pygame

class Starting_Room(pygame.sprite.Sprite):
    def __init__(self, player, screen):
        super().__init__()
        self.image = pygame.image.load("room.webp").convert_alpha()
        self.image = pygame.transform.scale(self.image, (450, 450))
        self.rect = self.image.get_rect(topleft=(175, 175))
        self.player = player
        self.screen = screen

    def draw(self, bg):
        self.screen.blit(bg, (0, 0))

    def update(self, **kwargs):
        if self.player.rect.right > self.rect.right:
            self.player.rect.right = self.rect.right
            self.player.velocity = pygame.math.Vector2(0, 0)
            self.player.pos = pygame.math.Vector2(self.player.rect.center)
        if self.player.rect.left < self.rect.left:
            self.player.rect.left = self.rect.left
            self.player.velocity = pygame.math.Vector2(0, 0)
            self.player.pos = pygame.math.Vector2(self.player.rect.center)
        if self.player.rect.bottom > self.rect.bottom:
            self.player.rect.bottom = self.rect.bottom
            self.player.velocity = pygame.math.Vector2(0, 0)
            self.player.pos = pygame.math.Vector2(self.player.rect.center)
        if self.player.rect.top < self.rect.top:
            self.player.rect.top = self.rect.top
            self.player.velocity = pygame.math.Vector2(0, 0)
            self.player.pos = pygame.math.Vector2(self.player.rect.center)