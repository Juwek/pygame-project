import pygame
from extensions import load_image
from constants import WIDTH, HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self, speed, *group, width=80, height=100):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image("pictures/player.png"), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2 - self.image.get_width() / 2
        self.rect.y = HEIGHT / 2 - self.image.get_height() / 2
        self.x, self.y = 0, 0
        self.speed = speed
        self.health = 100

    def update(self, *args):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed