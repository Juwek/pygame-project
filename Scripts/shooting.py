import pygame
import random
import math
from constants import WIDTH, HEIGHT

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Список путей к изображениям
image_paths = [f"data/pictures/pencils/{i}.png" for i in range(1, 11)]  # Создаем список путей к файлам image1.png - image10.png

# Предварительная загрузка изображений
images_cache = {}
for path in image_paths:
    images_cache[path] = pygame.image.load(path).convert_alpha()


# Класс для вращающейся картинки
class SpinningImage:
    def __init__(self, x, y):
        # Выбираем случайное изображение
        self.image_path = random.choice(image_paths)
        self.original_image = images_cache[self.image_path]
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.x = float(x)  # Храним координаты как float для более точного движения
        self.y = float(y)
        self.angle = 0
        self.rotation_speed = 15  # Скорость вращения
        self.speed = 6  # Скорость движения
        self.dx = 0  # Направление движения по x
        self.dy = 0  # Направление движения по y

    def set_direction(self, target_x, target_y):
        # Вычисляем направление движения
        distance_x = target_x - self.x
        distance_y = target_y - self.y
        angle = math.atan2(distance_y, distance_x)
        self.dx = math.cos(angle) * self.speed
        self.dy = math.sin(angle) * self.speed

    def update(self):
        # Вращение
        self.angle += self.rotation_speed
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=(int(self.x), int(self.y)))  # Обновляем rect с учетом float координат

        # Движение
        self.x += self.dx
        self.y += self.dy
        self.rect.center = (int(self.x), int(self.y))

        # Удаление картинки, если она выходит за пределы экрана (опционально)
        if self.x < -self.rect.width or self.x > WIDTH + self.rect.width or \
                self.y < -self.rect.height or self.y > HEIGHT + self.rect.height:
            return True  # Indicate that the image should be removed
        return False  # Indicate that the image should be kept

    def draw(self, screen):
        screen.blit(self.image, self.rect)