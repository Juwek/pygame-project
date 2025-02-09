from random import choice

import pygame
from constants import WIDTH, HEIGHT, FPS
from Scripts.Button import Button
from Scripts.Player import Player
from Scripts.Map import Map
from Scripts.Enemy import Enemy
from Scripts.Picture import Picture
from Scripts.Slider import Slider
from Scripts.Coin import ParticleCoins
from Scripts.Base import *
from extensions import set_text, base_is_created, load_image

state = 0
game = True
enemys = ['crazy', 'devil', 'poker']
main_count_coin = 0
collected_coins = 0
current_map = 0


def show_start_window(screen, group):
    """
    Отображает стартовое окно игры с кнопкой "Играть".

    Args:
        screen: Объект поверхности Pygame, на котором отображается окно.
        group: Объект группы спрайтов Pygame, в которой хранятся элементы окна.

    Изменяет глобальные переменные:
        state:  Изменяется на 1, если нажата кнопка "Играть" (переход к следующему состоянию игры).
        game: Изменяется на False, если игрок закрывает окно.
    """
    global state, game  # Объявляем, что используем глобальные переменные state и game
    clock = pygame.time.Clock()  # Создаем объект Clock для контроля FPS.

    # Создаем и добавляем фоновое изображение в группу спрайтов.
    Picture("maps/1.png", (0, 0), (1000, 800), group)  # Отображаем фоновое изображение

    # Создаем и добавляем кнопку "Играть" в группу спрайтов.
    play_button = Button("pictures/buttons/button1.png", WIDTH / 2 - 300, HEIGHT / 2 - 100,
                         600, 200, group) # Создаем кнопку "Играть"

    running = True  # Устанавливаем флаг для управления игровым циклом.
    while running:  # Основной игровой цикл для стартового окна.
        screen.fill('black')  # Заполняем экран черным цветом.

        for event in pygame.event.get():  # Обрабатываем события.
            if event.type == pygame.QUIT:  # Если игрок закрыл окно.
                running = False  # Останавливаем игровой цикл.
                game = False  # Завершаем игру.
            if play_button.is_clicked(event):  # Если кнопка "Играть" нажата.
                state = 1  # Переключаемся в следующее состояние игры (например, лобби).
                running = False  # Останавливаем игровой цикл стартового окна.

        group.draw(screen)  # Отображаем все спрайты из группы на экране.
        pygame.display.flip()  # Обновляем содержимое всего экрана.
        clock.tick(FPS)  # Контролируем FPS.


def show_lobby_window(screen, group):
    """
    Отображает окно лобби игры с кнопкой "Старт" и отображением количества монет игрока.

    Args:
        screen: Объект поверхности Pygame, на котором отображается окно.
        group: Объект группы спрайтов Pygame, в которой хранятся элементы окна.

    Изменяет глобальные переменные:
        state:  Изменяется на 2, если нажата кнопка "Старт" (переход к игровому процессу).
        game: Изменяется на False, если игрок закрывает окно.
        main_count_coin: Обновляет количество монет, полученное из `get_data()`.
    """
    global state, game, main_count_coin, current_map
    clock = pygame.time.Clock()  # Создаем объект Clock для контроля FPS.

    data = get_data() # Получаем данные об игре (включая количество монет)
    main_count_coin = data['coins']  # Обновляем глобальную переменную main_count_coin

    # Создаем и добавляем кнопку "Старт" в группу спрайтов.
    start_button = Button("pictures/buttons/button2.png", WIDTH - 250, HEIGHT - 150,
                          200, 100, group) # Создаем кнопку "Старт"

    # Создаем и добавляем изображение монеты в группу спрайтов.
    Picture('pictures/coin.png', (10, 10), (50, 50), group)  # Отображаем изображение монеты

     # Создаем текст с количеством монет игрока
    slider = Slider(['maps/preview1.png', 'maps/preview2.png'], data['maps'], group)

    running = True  # Устанавливаем флаг для управления игровым циклом.
    while running:  # Основной игровой цикл для окна лобби.
        screen.fill('#131010')  # Заполняем экран темно-серым цветом.
        coins_text = set_text(45, f' x {main_count_coin}')
        screen.blit(coins_text, (60, 10))  # Отображаем текст с количеством монет.

        for event in pygame.event.get():  # Обрабатываем события.
            if event.type == pygame.QUIT:  # Если игрок закрыл окно.
                running = False  # Останавливаем игровой цикл.
                game = False  # Завершаем игру.
            if start_button.is_clicked(event) and slider.open_maps[slider.current_map]:  # Если кнопка "Старт" нажата.
                state = 2  # Переключаемся в состояние игры.
                current_map = slider.current_map
                running = False
            if slider.right_button.is_clicked(event):
                slider.current_map = (slider.current_map + 1) % len(slider.maps)
            if slider.left_button.is_clicked(event):
                slider.current_map = (slider.current_map - 1) % len(slider.maps)
            if (slider.buy_button.is_clicked(event) and not slider.open_maps[slider.current_map]
                and int(slider.buy_button.get_inf()) <= main_count_coin):
                set_data('coins', main_count_coin - int(slider.buy_button.get_inf()))
                set_data('maps', '1 1')
                main_count_coin -= int(slider.buy_button.get_inf())
                data = get_data()
                slider.set_open_maps(data['maps'])
                print(get_data())

        slider.update()
        #pygame.draw.rect(screen, (0, 0, 0), slider.rect)
        group.draw(screen)
        if not slider.open_maps[slider.current_map]:
            screen.blit(slider.price, (470, 550))
        pygame.display.flip()  # Обновляем содержимое всего экрана.
        clock.tick(FPS)  # Контролируем FPS.


"""главный цикл самой игры"""
def show_main_window(screen, group, map):
    global state, game, collected_coins
    clock = pygame.time.Clock()
    group_map = pygame.sprite.Group()
    group_coins = pygame.sprite.Group()
    world_map = Map(map, group_map)
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
                enemies.append(Enemy(f"pictures/enemies/{enemys[choice(range(0, len(enemys)))]}.png",
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
        world_map.draw((player.x, player.y))

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

        screen.blit(pygame.transform.scale(load_image('pictures/coin.png'), (50, 50)), (10, 10))
        coins_text = set_text(45, f' x {count_coin}')
        screen.blit(coins_text, (60, 10))
        bar_pos = 600, 40
        health_bar_width = int(player.health * 3)
        health_bar_rect = pygame.Rect(bar_pos[0], bar_pos[1], health_bar_width, 20)
        pygame.draw.rect(screen, (0, 0, 0), (bar_pos[0] - 3, bar_pos[1] - 3, 306, 26))
        pygame.draw.rect(screen, (255, 0, 0), health_bar_rect)

        pygame.display.flip()
        clock.tick(FPS)


def show_final_window(screen, group, coins):
    """
    Отображает финальное окно игры, показывающее сообщение о проигрыше и статистику (количество монет).
    Также включает кнопку для возврата в лобби.

    Args:
        screen: Объект поверхности Pygame, на котором отображается окно.
        group: Объект группы спрайтов Pygame, в которой хранятся элементы окна.
        coins:  Количество монет, заработанных игроком.

    Изменяет глобальные переменные:
        state:  Изменяется на 1, если нажата кнопка "Лобби" (возврат в лобби).
        game: Изменяется на False, если игрок закрывает окно.
    """
    global state, game  # Объявляем, что используем глобальные переменные state и game.
    clock = pygame.time.Clock()  # Создаем объект Clock для контроля FPS.

    # Создаем и добавляем изображение "RIP" (Rest In Peace) в группу спрайтов.
    Picture("pictures/rip.png", (WIDTH / 2 - 70, 140), (140, 140), group)  # Отображаем изображение "RIP"

    # Создаем текст с сообщением о проигрыше.
    final_text = set_text(45, 'You lose')  # Создаем текст "You lose".

    # Создаем текст со статистикой (количество монет).
    statistic = set_text(45, f'coins: {coins}')  # Создаем текст со статистикой.

    # Создаем и добавляем кнопку "Лобби" в группу спрайтов.
    lobby_button = Button('pictures/buttons/button3.png', WIDTH / 2 - 175, 600,
                          350, 150, group)  # Создаем кнопку "Лобби".

    running = True  # Устанавливаем флаг для управления игровым циклом.
    while running:  # Основной игровой цикл для финального окна.
        screen.fill('#131010')  # Заполняем экран темно-серым цветом.

        for event in pygame.event.get():  # Обрабатываем события.
            if event.type == pygame.QUIT:  # Если игрок закрыл окно.
                running = False  # Останавливаем игровой цикл.
                game = False  # Завершаем игру.
            if lobby_button.is_clicked(event):  # Если кнопка "Лобби" нажата.
                state = 1  # Переключаемся в состояние лобби.
                running = False  # Останавливаем игровой цикл финального окна.

        group.draw(screen)  # Отображаем все спрайты из группы на экране.

        # Отображаем текст "You lose" по центру экрана.
        screen.blit(final_text, (WIDTH / 2 - final_text.get_width() / 2, 60))

        # Отображаем статистику (количество монет) по центру экрана.
        screen.blit(statistic, (WIDTH / 2 - statistic.get_width() / 2, 350))

        pygame.display.flip()  # Обновляем содержимое всего экрана.
        clock.tick(FPS)  # Контролируем FPS.


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
            show_main_window(screen, main_group, current_map)
        elif state == 3:
            show_final_window(screen, final_group, collected_coins)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()