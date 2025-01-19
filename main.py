import pygame
from constants import WIDTH, HEIGHT, FPS
from Scripts.Button import Button
from Scripts.Player import Player
from Scripts.Map import Map
from Scripts.Enemy import Enemy

state = 0
game = True


def show_start_window(screen, group):
    global state, game
    clock = pygame.time.Clock()
    play_button = Button("pictures/button1.png", WIDTH / 2 - 250, HEIGHT / 2 - 125,
                          500, 250, group)

    running = True
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game = False
            if play_button.is_clicked(event):
                state = 1
                running = False

        group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def show_lobby_window(screen, group):
    global state, game
    clock = pygame.time.Clock()
    start_button = Button("pictures/button2.png", WIDTH - 250, HEIGHT - 150,
                         200, 100, group)

    running = True
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game = False
            if start_button.is_clicked(event):
                state = 2
                running = False

        group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


def show_main_window(screen, group):
    """Здесь нужно добавить динамическое появление врагов через pygame.timer
        и добавлять их в список. Так же нужно сделать список путей картинок врагов"""
    global state, game
    clock = pygame.time.Clock()
    world_map = Map("maps/map1.png", 3, group)
    player = Player(world_map.speed, group)
    enemies = []
    enemies.append(Enemy("pictures/poker.png", (0, 400), group))

    running = True
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game = False

        group.draw(screen)
        for enemy in enemies:
            enemy.draw((player.x, player.y), (player.rect.x, player.rect.y))
        group.update()
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)

    """Для каждого окна создается отдельная группа спрайтов"""
    start_group = pygame.sprite.Group()
    lobby_group = pygame.sprite.Group()
    main_group = pygame.sprite.Group()

    while game:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        if state == 0:
            show_start_window(screen, start_group)
        elif state == 1:
            show_lobby_window(screen, lobby_group)
        elif state == 2:
            show_main_window(screen, main_group)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()