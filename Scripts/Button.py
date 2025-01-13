import pygame
from extensions import load_image


class Button(pygame.sprite.Sprite):
    def __init__(self, path, width, height, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image(path), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.x = 0