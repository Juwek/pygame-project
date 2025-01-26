import pygame
from extensions import load_image
from random import choice


class Map(pygame.sprite.Sprite):
    def __init__(self, map, pos: tuple[int, int], *group):
        super().__init__(*group)
        self.path = [['maps/1.png', 'maps/2.png', 'maps/3.png', 'maps/4.png', 'maps/5.png', 'maps/6.png'], []]
        # self.image = load_image(self.path[map][choice(range(0, len(self.path[map]) - 1))])
        self.image = load_image(self.path[0][0])
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.x = pos[0]
        self.y = pos[1]

    def draw(self, player_pos):
        self.player_x = player_pos[0]
        self.player_y = player_pos[1]
        self.rect.x = self.x - self.player_x
        self.rect.y = self.y - self.player_y