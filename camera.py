from constants import *

class Camera(pygame.sprite.Group):
  def __init__(self):
    super().__init__()
    self.display_surface = pygame.display.get_surface()
    self.half_width = self.display_surface.get_width() // 2
    self.half_height = self.display_surface.get_height() // 2
    self.offset = pygame.math.Vector2()

  def custom_draw(self, player, starting_room):
      self.offset.x = player.rect.centerx - self.half_width
      self.offset.y = player.rect.centery - self.half_height

      room_screen_rect = starting_room.rect.move(-self.offset.x, -self.offset.y)
      
      self.display_surface.set_clip(room_screen_rect)

      for sprite in self.sprites():
        offset_pos = sprite.rect.topleft - self.offset
        self.display_surface.blit(sprite.image, offset_pos)

      self.display_surface.set_clip(None)

