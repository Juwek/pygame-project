from random import choice

import pygame
from constants import WIDTH, HEIGHT, FPS
from Scripts.Button import Button
from Scripts.Player import Player
from Scripts.Map import Map
from Scripts.Enemy import Enemy
from Scripts.Picture import Picture
from Scripts.Coin import ParticleCoins
from Scripts.Base import *
from extensions import set_text, base_is_created

state = 0
game = True
spis = ['crazy', 'devil', 'poker']
main_count_coin = 0
collected_coins = 0


def show_start_window(screen, group):
    global state, game
    clock = pygame.time.Clock()
    Picture("maps/1.png", (0, 0), (1000, 800), group)
    play_button = Button("pictures/buttons/button1.png", WIDTH / 2 - 300, HEIGHT / 2 - 100,
                         600, 200, group)

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
    global state, game, main_count_coin
    clock = pygame.time.Clock()
    data = get_data()
    main_count_coin = data['coins']
    start_button = Button("pictures/buttons/button2.png", WIDTH - 250, HEIGHT - 150,
                          200, 100, group)
    Picture('pictures/coin.png', (10, 10), (50, 50), group)
    coins_text = set_text(45, f' x {main_count_coin}')

    running = True
    while running:
        screen.fill('#131010')
        screen.blit(coins_text, (60, 10))
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
    global state, game, collected_coins
    print(main_count_coin)
    clock = pygame.time.Clock()
    group_map = pygame.sprite.Group()
    group_coins = pygame.sprite.Group()
    pos = [(0, 0)]
    tiles_map = []
    tiles_map.append(Map(map, group_map))
    player = Player(3, group)

    count_coin = 0
    coins = []

    enemies = []
    limit_spawn = 300
    #координаты спавна врагов за пределами экрана
    one = [[x for x in range(-limit_spawn, WIDTH + limit_spawn + 1)
         if x not in range(-80, WIDTH + 80)],
           [y for y in range(-limit_spawn, HEIGHT + limit_spawn + 1)]]
    two = [[x for x in range(-limit_spawn, WIDTH + limit_spawn + 1)],
           [y for y in range(-limit_spawn, HEIGHT + limit_spawn + 1)
         if y not in range(-80, HEIGHT + 80)]]
    enemy_spawn_coords = [one, two]

    enemy_time_spawn = 3000                                         #время спавна врага в млсек
    enemy_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(enemy_timer, enemy_time_spawn)            #таймер для спавна врага
    wave_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(wave_timer, 20000)                   #таймер для снижения времени спавна врага
    stabilization_timer = pygame.USEREVENT + 3
    stabilization = False
    Picture('pictures/coin.png', (10, 10), (50, 50), group)

    running = True
    while running:
        screen.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game = False
            if event.type == enemy_timer:
                lst = choice(enemy_spawn_coords)
                x, y = lst[0], lst[1]
                enemies.append(Enemy(f"pictures/enemies/{spis[choice(range(0, len(spis)))]}.png",
                                     (choice(x) + player.x, choice(y) + player.y), group))
            if event.type == wave_timer:
                #снижается время спавна врага на 10% и обновляется таймер
                enemy_time_spawn -= enemy_time_spawn * 10 / 100
                pygame.time.set_timer(enemy_timer, int(enemy_time_spawn))
            if event.type == stabilization_timer:
                stabilization = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                numbers = range(-5, 6)
                for _ in range(choice(range(1, 4))):
                    coins.append(ParticleCoins(30, (100, 100), choice(numbers), choice(numbers),
                                               group_coins))

        group_map.draw(screen)
        for tile in tiles_map:
            tile.draw((player.x, player.y))

        group_coins.draw(screen)
        group_coins.update((player.x, player.y))
        for coin in group_coins:
            if player.rect.colliderect(coin.rect):
                group_coins.remove(coin)
                count_coin += 1

        for enemy in enemies:
            enemy.draw((player.x, player.y), (player.rect.x, player.rect.y))
        enemy_colide = pygame.sprite.spritecollide(player, enemies, False)

        if enemy_colide and not stabilization:
            player.health -= choice(range(5, 16))
            pygame.time.set_timer(stabilization_timer, 1000)
            stabilization = True

        if player.health <= 0:
            collected_coins = count_coin
            set_data('coins', main_count_coin + count_coin)
            running = False
            group.empty()
            state = 3

        group.draw(screen)
        group.update()

        coins_text = set_text(45, f' x {count_coin}')
        screen.blit(coins_text, (60, 10))

        pygame.display.flip()
        clock.tick(FPS)


def show_final_window(screen, group, coins):
    global state, game
    clock = pygame.time.Clock()
    Picture("pictures/rip.png", (WIDTH / 2 - 70, 140), (140, 140), group)
    final_text = set_text(45, 'You lose')
    statistic = set_text(45, f'coins: {coins}')
    lobby_button = Button('pictures/buttons/button3.png', WIDTH / 2 - 175, 600,
                          350, 150, group)

    running = True
    while running:
        screen.fill('#131010')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game = False
            if lobby_button.is_clicked(event):
                state = 1
                running = False

        group.draw(screen)
        screen.blit(final_text, (WIDTH / 2 - final_text.get_width() / 2, 60))
        screen.blit(statistic, (WIDTH / 2 - statistic.get_width() / 2, 350))
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    size = WIDTH, HEIGHT
    screen = pygame.display.set_mode(size)

    if not base_is_created():
        create_base()

    """Для каждого окна создается отдельная группа спрайтов"""
    start_group = pygame.sprite.Group()
    lobby_group = pygame.sprite.Group()
    main_group = pygame.sprite.Group()
    final_group = pygame.sprite.Group()

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
        elif state == 3:
            show_final_window(screen, final_group, collected_coins)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()