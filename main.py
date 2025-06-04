import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Peacook")
clock = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont("Arial", 25)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 40, 40)
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
        pygame.draw.rect(surface, (255, 255, 255), local_rect)

class Starting_Room:
    def __init__(self):
        self.rect = pygame.Rect(175, 175, 450, 450)

    def update(self):
        if player.rect.right > self.rect.right:
            player.rect.right = self.rect.right
            player.velocity = pygame.math.Vector2(0, 0)
        if player.rect.left < self.rect.left:
            player.rect.left = self.rect.left
            player.velocity = pygame.math.Vector2(0, 0)
        if player.rect.bottom > self.rect.bottom:
            player.rect.bottom = self.rect.bottom
            player.velocity = pygame.math.Vector2(0, 0)
        if player.rect.top < self.rect.top:
            player.rect.top = self.rect.top
            player.velocity = pygame.math.Vector2(0, 0)

class NPC:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)
        self.speed_x = 0
        self.speed_y = 0

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
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(400, 700))
        screen.blit(text_surface, text_rect)

    def update(self, color, surface, offset):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.speed_x = 0
        self.speed_y = 0

        visible_area = pygame.Rect(offset[0], offset[1], surface.get_width(), surface.get_height())
        if self.rect.colliderect(visible_area):
            local_rect = self.rect.move(-offset[0], -offset[1])
            pygame.draw.rect(surface, color, local_rect)

player = Player(380, 380)
starting_room = Starting_Room()
npcs = [NPC(500, 340), NPC(500, 420)]

room_surface = pygame.Surface((starting_room.rect.width, starting_room.rect.height))
skipped = False

while True:
    screen.fill((224, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and npcs[0].rect.x <= 440:
                skipped = True

    if npcs and npcs[0].rect.x > 440:
        for npc in npcs:
            npc.move("right", 1)
    elif npcs and npcs[0].rect.x == 440:
        if npcs[0].rect.y == 340:
            npcs[0].talk("Me and mom are gonna get some milk, Don't do anything stupid, ok?")
        if skipped:
            for npc in npcs:
                npc.move("down", 1)

    room_surface.fill((128, 128, 128))
    room_offset = (starting_room.rect.left, starting_room.rect.top)

    for i, npc in enumerate(npcs):
        color = (0, 0, 255) if i == 0 else (255, 0, 0)
        npc.update(color, room_surface, room_offset)
    
    player.update()
    starting_room.update()
    player.draw(room_surface, room_offset)

    

    npcs = [npc for npc in npcs if starting_room.rect.colliderect(npc.rect)]
    if not npcs:
        player.can_move = True

    screen.blit(room_surface, starting_room.rect.topleft)
    pygame.display.update()
    clock.tick(fps)
