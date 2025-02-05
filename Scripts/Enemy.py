import pygame
from extensions import load_image


class Enemy(pygame.sprite.Sprite):
    def __init__(self, path, start_pos, *group):
        super().__init__(*group)
        self.image = load_image(path)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = start_pos
        self.x, self.y = start_pos
        self.speed = 1.4
        self.health = 50

    def draw(self, player_pos, player_rect):
        self.player_x = player_pos[0]
        self.player_y = player_pos[1]
        self.player_rect_x = player_rect[0]
        self.player_rect_y = player_rect[1]

        self.rect.x = self.x - self.player_x
        self.rect.y = self.y - self.player_y

    def update(self):
        dx = 0
        dy = 0
        if self.rect.centerx < player.rect.centerx:
            dx = self.speed
        elif self.rect.centerx > player.rect.centerx:
            dx = -self.speed

        if self.rect.centery < player.rect.centery:
            dy = self.speed
        elif self.rect.centery > player.rect.centery:
            dy = -self.speed

        self.rect.x += dx
        self.rect.y += dy

    def check_colliders(self, player_rect):
        return self.rect.colliderect(player_rect)
