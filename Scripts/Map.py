import pygame
from extensions import load_image
from constants import WIDTH, HEIGHT


class Map(pygame.sprite.Sprite):
    def __init__(self, map, *group):
        super().__init__(*group)
        self.maps = ['maps/map1.png', 'maps/map2.png']
        self.image = load_image(self.maps[map])
        self.rect = self.image.get_rect()
        self.x = -self.image.get_width() / 2 + WIDTH / 2
        self.y = -self.image.get_height() / 2 + HEIGHT / 2

    def draw(self, player_pos):
        self.player_x = player_pos[0]
        self.player_y = player_pos[1]
        self.rect.x = self.x - self.player_x
        self.rect.y = self.y - self.player_y