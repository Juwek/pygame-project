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
        self.speed = speed
        self.max_health = 100 
        self.health = self.max_health

    def update(self, *args):
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0
        if keys[pygame.K_d]:
            dx += self.speed
        if keys[pygame.K_a]:
            dx -= self.speed
        if keys[pygame.K_w]:
            dy -= self.speed
        if keys[pygame.K_s]:
            dy += self.speed

        self.rect.x += dx
        self.rect.y += dy
