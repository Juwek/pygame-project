import pygame
from Scripts.Button import Button
from main import set_state


def show_start_window(screen, group):
    start_button = Button("pictures/button.png", 100, 40, group)

    running = True
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if (event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]
                and start_button.rect.collidepoint(pygame.mouse.get_pos())):
                set_state(1)
                running = False

        group.draw(screen)
        pygame.display.flip()

def show_lobby_window(screen, group):
    print('ds')