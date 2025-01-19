import pygame
from extensions import load_image


class Enemy(pygame.sprite.Sprite):
    def __init__(self, path, start_pos, *group):
        super().__init__(*group)
        self.image = load_image(path)
        self.rect = self.image.get_rect()
        self.x = start_pos[0]
        self.y = start_pos[1]
        self.speed = 1.5

    def draw(self, player_pos, player_rect):
        self.rect.x = self.x - player_pos[0]
        self.rect.y = self.y - player_pos[1]
        self.player_rect_x = player_rect[0]
        self.player_rect_y = player_rect[1]

    def update(self):
        """Передвижение врага к игроку, сравнивая их rect
            и меняя значения self.x/y"""
        pass

    """Нужно добавить фунцию столкновения rect врага и rect игрока"""