import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.img = pygame.image.load("peacock1.png").convert_alpha()
        self.img = pygame.transform.scale(self.img, (100, 100))
        self.rect = self.img.get_rect(center=(x, y))
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.can_move = False

    def move(self):
        self.velocity = pygame.math.Vector2(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.velocity.x += 1
        if keys[pygame.K_a]:
            self.velocity.x -= 1
        if keys[pygame.K_w]:
            self.velocity.y -= 1
        if keys[pygame.K_s]:
            self.velocity.y += 1
        if self.velocity.length_squared() > 0:
            self.velocity = self.velocity.normalize() * self.speed

    def update(self):
        if self.can_move:
            self.move()
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def draw(self, surface, offset):
        local_rect = self.rect.move(-offset[0], -offset[1])
        surface.blit(self.img, local_rect)