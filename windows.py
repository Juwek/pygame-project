import pygame
from Scripts.Button import Button


def show_start_window(screen, group):
    start_button = Button("pictures/button.png", 100, 40, group)

    while True:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if (event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]
                and start_button.rect.collidepoint(pygame.mouse.get_pos())):
                print(start_button.rect)

        group.draw(screen)
        pygame.display.flip()