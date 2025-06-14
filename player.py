import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image_left = pygame.image.load("Peacock.png").convert_alpha()
        self.image_left = pygame.transform.scale(self.image_left, (100, 100))
        self.image_right = pygame.transform.flip(self.image_left, True, False)
        self.image_right = pygame.transform.scale(self.image_right, (100, 100))
        self.image = self.image_right
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.pos = pygame.math.Vector2(self.rect.center)
        self.velocity = pygame.math.Vector2(0, 0)
        self.speed = 200
        self.can_move = False

    def move(self):
        self.velocity = pygame.math.Vector2(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.velocity.x += 1
            self.image = self.image_right
            self.rect = self.image.get_rect(center=(self.x, self.y))
        if keys[pygame.K_a]:
            self.velocity.x -= 1
            self.image = self.image_left
            self.rect = self.image.get_rect(center=(self.x, self.y))
        if keys[pygame.K_w]:
            self.velocity.y -= 1
        if keys[pygame.K_s]:
            self.velocity.y += 1
        if self.velocity.length_squared() > 0:
            self.velocity = self.velocity.normalize() * self.speed

    def update(self, **kwargs):
        dt = kwargs.get("dt", 0)
        if self.can_move:
            self.move()
        self.pos += self.velocity * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))
