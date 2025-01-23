import pygame
from extensions import load_image
from random import choice


class Map(pygame.sprite.Sprite):
    def __init__(self, map, pos: tuple[int, int], speed, *group):
        super().__init__(*group)
        self.path = [['maps/1.png', 'maps/2.png', 'maps/3.png', 'maps/4.png', 'maps/5.png', 'maps/6.png'], []]
        # self.image = load_image(self.path[map][choice(range(0, len(self.path[map]) - 1))])
        self.image = load_image(self.path[0][0])
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.speed = speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.rect.x -= self.speed
        if keys[pygame.K_a]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y += self.speed
        if keys[pygame.K_s]:
            self.rect.y -= self.speed