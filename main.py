from utilities import *
from constants import *
from npc import *
from player import *
from starting_room import *
from camera import *
import sys

player = Player(300, 380)
starting_room = Starting_Room(player, screen)
room_surface = starting_room.image
npcs = [NPC(500, 340, screen, (0, 0, 255)), NPC(500, 420, screen, (255, 0, 0)), NPC(400, 650, screen, (0, 255, 0))]
old = npcs[2]
visible_sprites = pygame.sprite.Group()
visible_sprites.add(starting_room, player, npcs)

while True:
    
    dt = clock.tick(fps) / 1000
    
    starting_room.draw(bg)

    current_room_surface = room_surface.copy()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if not skipped:
                if event.key == pygame.K_SPACE and visible_width == scroll_width:
                    if not skipped_animation:
                        skipped_animation = True
                    else:
                        skipped = True

    if npcs and npcs[0].rect.centerx > 400:
        for i in range (len(npcs) - 1):
            npcs[i].move("left", 100 * dt)

    elif npcs and 395 < npcs[0].rect.centerx < 401:
        if npcs[0].rect.y == 290:
            visible_width, skipped, skipped_animation = npcs[0].talk(dad, visible_width, skipped, skipped_animation)
        if npcs[0].closed:
            for i in range (len(npcs) - 1):
                npcs[i].move("down", 100 * dt)

    for i, sprite in enumerate(visible_sprites):
        sprite.update(
            dt=dt,
        )

    starting_room.update()
    screen.set_clip(starting_room.rect)
    visible_sprites.draw(screen)
    screen.set_clip(None)

    npcs = [npc for npc in npcs if npc is old or starting_room.rect.colliderect(npc.rect)]

    for sprite in visible_sprites.sprites():
        if isinstance(sprite, NPC) and sprite not in npcs:
            old.rect.centerx = sprite.rect.centerx
            visible_sprites.remove(sprite)

    if len(npcs) == 1:
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
            if npcs[0]:
                if npcs[0].closed:
                    npcs[0].move("down", 90 * dt)
                    if not starting_room.rect.colliderect(npcs[0].rect):
                        delay_phase = 4
                if npcs[0].rect.centery > 380 and not npcs[0].closed:
                    npcs[0].move("up", 90 * dt)
                elif not npcs[0].closed:
                    visible_width, skipped, skipped_animation = npcs[0].talk(old_peacock, visible_width, skipped, skipped_animation)

        elif delay_phase == 4:
            player.can_move = True
            npcs.pop()
            

    if len(npcs) == 1 and delay_phase == 2:
        screen.blit(waiting_surface, waiting_rect)
        screen.blit(waiting_text, waiting_text_rect)

    pygame.display.update()
