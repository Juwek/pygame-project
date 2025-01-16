from constants import WIDTH, HEIGHT, FPS
from Scripts.Player import Player
from windows import *

state = 0

def set_state(num):
    global state
    state = num

def get_state():
    return state

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)

    start_group = pygame.sprite.Group()
    lobby_group = pygame.sprite.Group()
    main_group = pygame.sprite.Group()
    player = Player(main_group)

    running = True
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if get_state() == 0:
            show_start_window(screen, start_group)
        elif get_state() == 1:
            show_lobby_window(screen, lobby_group)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()