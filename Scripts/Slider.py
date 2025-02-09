import pygame
from Scripts.Button import Button
from Scripts.Picture import Picture
from constants import WIDTH, HEIGHT
from extensions import set_text


class Slider:
    def __init__(self, maps, open_maps, group):
        self.group = group
        self.size = 700, 600
        self.pos = WIDTH / 2 - self.size[0] / 2, HEIGHT / 2 - self.size[1] / 2 - 50
        self.maps = maps
        self.open_maps = [int(i) for i in open_maps.split()]
        self.rect = pygame.rect.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.current_map = 0
        self.image = Picture(self.maps[self.current_map], (self.pos[0] + 150, self.pos[1] + 50),
                             (400, 400), self.group)
        self.left_button = Button('pictures/buttons/left.png', self.pos[0] + 45,
                                   265, 52, 66, group)
        self.right_button = Button('pictures/buttons/right.png', self.pos[0] + 600,
                                  265, 52, 66, group)
        self.buy_button = Button('pictures/buttons/button4.png', self.pos[0] + 250,
                                 self.pos[1] + 475, 200, 100, inf='100')
        self.price = set_text(45, self.buy_button.get_inf())

    def update(self):
        self.image.set_img(self.maps[self.current_map])
        if not self.open_maps[self.current_map]:
            self.buy_button.set_group(self.group)
        else:
            self.group.remove(self.buy_button)

    def set_open_maps(self, open_maps):
        self.open_maps = [int(i) for i in open_maps.split()]