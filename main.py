import pygame
from constants import WIDTH, HEIGHT, FPS
from Scripts.Player import Player
from windows import *


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()
    player = Player(all_sprites)
    state = 0

    running = True
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if state == 0:
            show_start_window(screen, all_sprites)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()