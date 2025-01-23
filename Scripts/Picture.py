import pygame
from extensions import load_image


class Picture(pygame.sprite.Sprite):
    def __init__(self, path, pos: tuple[int, int], size: tuple[int, int], *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image(path), (size[0], size[1]))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]