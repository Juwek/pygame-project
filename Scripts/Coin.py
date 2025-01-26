import pygame
from extensions import load_image


class Coin(pygame.sprite.Sprite):
    def __init__(self, size, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(load_image('pictures/coin.png'), (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0


class ParticleCoins(Coin):
    def __init__(self, size, pos, dx, dy, *group):
        super().__init__(size, group)
        self.velocity = [dx, dy]
        self.direction = 0
        self.rect.x, self.rect.y = -size, -size
        self.x, self.y = pos
        self.gravity = 0.2

    def update(self, player_pos):
        self.player_x = player_pos[0]
        self.player_y = player_pos[1]
        self.rect.x = self.x - self.player_x
        self.rect.y = self.y - self.player_y

        if self.direction <= 15:
            self.velocity[1] += self.gravity
            self.x += self.velocity[0]
            self.y += self.velocity[1]
            self.direction += 1