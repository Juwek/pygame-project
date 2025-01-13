import pygame
from constants import WIDTH, HEIGHT, FPS
from Scripts.Player import Player
from Scripts.Button import Button


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)

    all_sprites = pygame.sprite.Group()
    player = Player(all_sprites)
    start_button = Button("pictures/button.png", 100, 40, all_sprites)

    running = True
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.draw(screen)
        all_sprites.update(pygame.key.get_pressed())
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()