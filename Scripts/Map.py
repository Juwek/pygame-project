import pygame
from extensions import load_image


class Map(pygame.sprite.Sprite):
    def __init__(self, map, *group):
        super().__init__(*group)
        self.image = load_image('maps/map1.png')
        self.rect = self.image.get_rect()
        self.x = -self.image.get_width() / 2
        self.y = -self.image.get_height() / 2

    def draw(self, player_rect):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j]:
                    self.tile = load_image(f'maps/{self.map[i][j]}.png')
                    screen.blit(self.tile, (j * 100, i * 100 - player_rect.y))
