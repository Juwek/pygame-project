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
        if self.rect.x < self.player_rect_x:
            self.x += self.speed
        if self.rect.x > self.player_rect_x:
            self.x -= self.speed
        if self.rect.y < self.player_rect_y:
            self.y += self.speed
        if self.rect.y > self.player_rect_y:
            self.y -= self.speed