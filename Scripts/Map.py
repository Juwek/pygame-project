import pygame
from extensions import load_image


class Map(pygame.sprite.Sprite):
    def __init__(self, map, *group):
        super().__init__(*group)
        self.image = load_image('maps/map1.png')
        self.rect = self.image.get_rect()
        self.x = -self.image.get_width() / 2
        self.y = -self.image.get_height() / 2

    def draw(self, player_pos):
        self.player_x = player_pos[0]
        self.player_y = player_pos[1]
        self.rect.x = self.x - self.player_x
        self.rect.y = self.y - self.player_y