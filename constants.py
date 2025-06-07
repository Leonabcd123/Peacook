import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Peacook")
clock = pygame.time.Clock()
fps = 60
font1 = pygame.font.SysFont("Arial", 25)
font2 = pygame.font.SysFont("Arial", 50)
dad = ["Dad:\nMe and mom are gonna get some milk, Don't do anything stupid, ok?\n(Press Space To Continue)"]
old_peacock = ["Old Peacock:\nHello Yoshi, I got some bad news for you...\n(Press Space To Continue)", "Old Peacock:\nA cat cooked your parents\n(Press Space To Continue)", "Old Peacock:\nYou have to get revenge!\n(Press Space To Continue)"]

bg = pygame.image.load("bg.webp").convert_alpha()
bg = pygame.transform.scale(bg, (800, 800))
skipped = False
skipped_animation = False
typewriter_speed = 25

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

scroll_width, scroll_height = 650, 135
scroll_x, scroll_y = 80, 660

visible_width = 0
unroll_speed = 13

BG_COLOR = (245, 222, 179)
SCROLL_COLOR = (210, 180, 140)
HANDLE_COLOR = (139, 69, 19)