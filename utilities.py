from constants import *


def stop(start_time, duration):
  return pygame.time.get_ticks() >= start_time + duration

def unroll_scroll(text, visible_width):
    lines = text.split("\n")
        
    text_surface = pygame.Surface((scroll_width, scroll_height), pygame.SRCALPHA)
    text_surface.fill((0, 0, 0, 0)) 

    y_offset = 10
    for line in lines:
        line_surf = font1.render(line, True, (0, 0, 0))
        text_surface.blit(line_surf, (10, y_offset))
        y_offset += line_surf.get_height() + 5
    
    if visible_width > 0:
      visible_width -= unroll_speed
      
      handle_width = 20
      pygame.draw.rect(screen, HANDLE_COLOR, (scroll_x - handle_width, scroll_y, handle_width, scroll_height))
      scroll_rect = pygame.Rect(scroll_x, scroll_y, visible_width, scroll_height)
      pygame.draw.rect(screen, SCROLL_COLOR, scroll_rect)
      pygame.draw.rect(screen, HANDLE_COLOR, (scroll_rect.right, scroll_y, handle_width, scroll_height))
      pygame.draw.rect(screen, (160, 82, 45), scroll_rect, 3)

      screen.blit(text_surface, (scroll_x, scroll_y), area=pygame.Rect(0, 0, visible_width, scroll_height))

    return visible_width