import os
import sys
import pygame

pygame.init()


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    img = pygame.image.load(fullname)
    return img


def set_text(size, text):
    font = pygame.font.Font('fonts/ConcertOne-Regular.ttf', size)
    return font.render(text, True, (255, 255, 255))


def get_data():
    with open('data.txt', 'r') as file:
        data = {}
        for line in file.readlines():
            inf = line.split()
            data[inf[0]] = inf[1]
    return data