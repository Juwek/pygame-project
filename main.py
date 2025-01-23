from random import choice

import pygame
from constants import WIDTH, HEIGHT, FPS
from Scripts.Button import Button
from Scripts.Player import Player
from Scripts.Map import Map
from Scripts.Enemy import Enemy
from Scripts.Picture import Picture

state = 0
game = True


def show_start_window(screen, group):
    global state, game
    clock = pygame.time.Clock()
    Picture("maps/1.png", (0, 0), (1000, 800), group)
    play_button = Button("pictures/buttons/button1.png", WIDTH / 2 - 250, HEIGHT / 2 - 125,
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
    start_button = Button("pictures/buttons/button2.png", WIDTH - 250, HEIGHT - 150,
                          200, 100, group)

    running = True
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game = False
            elif start_button.is_clicked(event):
                state = 2
                running = False

        group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


"""главный цикл самой игры"""
def show_main_window(screen, group, map):
    global state, game
    clock = pygame.time.Clock()
    group_map = pygame.sprite.Group()
    world_map = Map(map, (0, 0), 3, group_map)
    player = Player(world_map.speed, group)

    enemies = []
    limit_spawn = 300
    #координаты спавна врагов за пределами экрана (не доделано)
    x = [i for i in range(-limit_spawn, WIDTH + limit_spawn + 1)
         if (-limit_spawn <= i <= -80) or (WIDTH + 80 <= i <= WIDTH + limit_spawn + 1)]
    y = [i for i in range(-limit_spawn, HEIGHT + limit_spawn + 1)
         if (-limit_spawn <= i <= -80) or (HEIGHT + 80 <= i <= HEIGHT + limit_spawn + 1)]

    enemy_time_spawn = 10                                           #время спавна врага в млсек
    enemy_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_timer, enemy_time_spawn)            #таймер для спавна врага
    wave_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(wave_timer, 20000)                  #таймер для снижения времени спавна врага

    running = True
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game = False
            elif event.type == enemy_timer:
                ex, ey = choice(x), choice(y)
                enemies.append(Enemy("pictures/enemies/poker.png",
                                     (ex, ey), group))
            elif event.type == wave_timer:
                #снижается время спавна врага на 10% и обновляется таймер
                enemy_time_spawn -= enemy_time_spawn * 10 / 100
                pygame.time.set_timer(enemy_timer, int(enemy_time_spawn))

        group_map.draw(screen)
        group_map.update()
        for enemy in enemies:
            enemy.draw((player.x, player.y), (player.rect.x, player.rect.y))
        group.draw(screen)
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
            show_main_window(screen, main_group, 0)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
