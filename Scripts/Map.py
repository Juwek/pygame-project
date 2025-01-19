import pygame
from extensions import load_image
from constants import WIDTH, HEIGHT


class Map(pygame.sprite.Sprite):
    def __init__(self, path, speed, *group):
        super().__init__(*group)
        self.image = load_image(path)
        self.rect = self.image.get_rect()
        self.rect.x = -self.image.get_width() / 2
        self.rect.y = -self.image.get_height() / 2
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