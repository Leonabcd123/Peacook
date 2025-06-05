from player import *
from starting_room import Starting_Room
from npc import NPC
from utilities import *
import sys

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Peacook")
clock = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont("Arial", 25)

player = Player(380, 380)
starting_room = Starting_Room(player)
npcs = [NPC(500, 340, font, screen), NPC(500, 420, font, screen)]
old = NPC(440, 650, font, screen)

room_surface = pygame.Surface((starting_room.rect.width, starting_room.rect.height))
skipped = False

delay_started = False
delay_start_time = 0
delay_duration = 3000
delay_done = False

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
            npc.move("right", 2)
    elif npcs and npcs[0].rect.x == 440:
        if npcs[0].rect.y == 340:
            text = "Dad:\nMe and mom are gonna get some milk, Don't do anything stupid, ok?\n(Press Space To Continue)"
            npcs[0].talk(text)
        if skipped:
            for npc in npcs:
                npc.move("down", 2)

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
        if not delay_done: 
            if not delay_started:
                delay_start_time = pygame.time.get_ticks()
                delay_started = True    
            if delay_started and pygame.time.get_ticks() - delay_start_time >= delay_duration:
                color = (0, 255, 0)
                stop(delay_start_time, delay_duration)
                delay_done = True
        else:
            if old.rect.y > 380: 
                old.move("up", 2)
            old.update(color, room_surface, room_offset)
        

    screen.blit(room_surface, starting_room.rect.topleft)
    pygame.display.update()
    clock.tick(fps)
