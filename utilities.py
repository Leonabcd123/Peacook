import pygame

def stop(start_time, duration):
  return pygame.time.get_ticks() >= start_time + duration