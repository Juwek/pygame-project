import pygame
from extensions import load_image


class Button(pygame.sprite.Sprite):
    def __init__(self, path, x, y, width, height, *group, inf=None):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image(path), (width, height))
        self.rect = self.image.get_rect()
        self.inf = inf
        self.rect.x = x
        self.rect.y = y

    def is_clicked(self, event):
        if (event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]
            and self.rect.collidepoint(pygame.mouse.get_pos())):
            return True

    def get_inf(self):
        return self.inf

    def set_group(self, *group):
        super().__init__(*group)