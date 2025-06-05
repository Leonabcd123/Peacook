import pygame
from player import Player
from starting_room import Starting_Room
from npc import NPC

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Peacook")
clock = pygame.time.Clock()
fps = 60
font1 = pygame.font.SysFont("Arial", 25)
font2 = pygame.font.SysFont("Arial", 50)
text = "Dad:\nMe and mom are gonna get some milk, Don't do anything stupid, ok?\n(Press Space To Continue)"

player = Player(380, 380)
starting_room = Starting_Room(player)
npcs = [NPC(500, 340, font1, screen), NPC(500, 420, font1, screen)]
old = NPC(440, 650, font1, screen)

room_surface = pygame.Surface((starting_room.rect.width, starting_room.rect.height))
skipped = False

delay_start_time = 0
delay1_duration = 500
delay2_duration = 3000
delay_phase = 0

TRANSPARENCY = 128

waiting_surface = pygame.Surface((800, 800), pygame.SRCALPHA)
waiting_surface.fill((128, 128, 128, TRANSPARENCY))
waiting_rect = waiting_surface.get_rect(center=(400, 400))
waiting_text = font2.render("2000 Years Later...", True, (255, 255, 255))
waiting_text_rect = waiting_text.get_rect(center=(400, 300))
