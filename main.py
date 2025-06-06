from utilities import *
from constants import *
from npc import *
from player import *
from starting_room import *
import sys


player = Player(300, 380)
starting_room = Starting_Room(player)
room_surface = starting_room.img
npcs = [NPC(500, 340, screen), NPC(500, 420, screen)]
old = NPC(380, 650, screen)


while True:

    dt = clock.tick(fps) / 1000

    screen.blit(bg, (0, 0))

    current_room_surface = room_surface.copy()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if not skipped:
                if event.key == pygame.K_SPACE and visible_width == scroll_width:
                    skipped = True

    if npcs and npcs[0].rect.x > 380:
        for npc in npcs:
            npc.move("left", 100 * dt)

    elif npcs and 375 < npcs[0].rect.x < 381:
        if npcs[0].rect.y == 340:
            visible_width = npcs[0].talk(text, visible_width)
        skipped, visible_width = check_skipped(skipped, text, visible_width, npcs)
        if skipped:
            for npc in npcs:
                npc.move("down", 100 * dt)

    room_offset = (starting_room.rect.left, starting_room.rect.top)

    for i, npc in enumerate(npcs):
        color = (0, 0, 255) if i == 0 else (255, 0, 0)
        npc.update(color, current_room_surface, room_offset)

    player.update(dt)
    starting_room.update()
    player.draw(current_room_surface, room_offset)

    npcs = [npc for npc in npcs if starting_room.rect.colliderect(npc.rect)]

    if not npcs:
        if delay_phase == 0:
            delay_start_time = pygame.time.get_ticks()
            delay_phase = 1

        elif delay_phase == 1:
            if stop(delay_start_time, delay1_duration):
                delay_phase = 2

        elif delay_phase == 2:
            if stop(delay_start_time, delay2_duration):
                delay_phase = 3

        elif delay_phase == 3:
            if old.rect.y > 380:
                old.move("up", 90 * dt)
            old.update((0, 255, 0), current_room_surface, room_offset)
    
    screen.blit(current_room_surface, starting_room.rect.topleft)

    if not npcs and delay_phase == 2:
        screen.blit(waiting_surface, waiting_rect)
        screen.blit(waiting_text, waiting_text_rect)

    pygame.display.update()
