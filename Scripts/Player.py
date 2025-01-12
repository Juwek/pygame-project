import pygame
from extensions import load_image
from constants import WIDTH, HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self, *group, width=100, height=110):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image("pictures/player.png"), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2 - self.image.get_width() / 2
        self.rect.y = HEIGHT / 2 - self.image.get_height() / 2
        self.speed = 3

    def update(self, keys):
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed