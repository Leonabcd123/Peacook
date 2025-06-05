from utilities import *
from constants import *
import sys

while True:
    screen.fill((224, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if not skipped:
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
                old.move("up", 2)
            old.update((0, 255, 0), room_surface, room_offset)


    screen.blit(room_surface, starting_room.rect.topleft)
    if not npcs and delay_phase == 2:
        screen.blit(waiting_surface, waiting_rect)
        screen.blit(waiting_text, waiting_text_rect)
    pygame.display.update()
    clock.tick(fps)
