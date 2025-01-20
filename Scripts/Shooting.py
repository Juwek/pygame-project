import pygame
import math
import os
import random


class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos, speed, image_path):
        super().__init__()
        self.original_image = pygame.image.load(image_path).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=start_pos)
        self.speed = speed
        self.angle = 0  # Угол поворота
        self.rotation_speed = 10  # Скорость вращения

        # Расчет вектора движения
        dx = target_pos[0] - start_pos[0]
        dy = target_pos[1] - start_pos[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance > 0:  # Avoid division by zero
            self.dx = dx / distance
            self.dy = dy / distance
        else:
            self.dx = 0
            self.dy = 0

    def update(self):
        self.rect.x += self.dx * self.speed
        self.rect.y += self.dy * self.speed

        # Вращение изображения
        self.angle += self.rotation_speed
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

        # Удалить пулю, когда она уходит за экран
        if (self.rect.x < 0 or self.rect.x > 800 or self.rect.y < 0 or self.rect.y > 600):  # Размеры экрана 800x600
            self.kill()


class Shooter():
    def __init__(self, color=(255, 255, 255), size=20):
        self.color = color
        self.size = size
        self.bullets = pygame.sprite.Group()
        self.image = pygame.Surface((self.size, self.size))
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(400, 300))  # Начальное положение шутера
        self.image_paths = self.create_random_image_list()  # Список путей к изображениям
        self.current_image_index = 0
        self.magazine_size = 5  # Размер обоймы
        self.bullets_in_magazine = self.magazine_size  # количество патрон в обойме
        self.reload_time = 5000  # 5 секунд в миллисекундах
        self.last_shot_time = 0
        self.reloading = False
        self.show_reloading_text = False  # Флаг для показа надписи "Reloading"

    def create_random_image_list(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_files = [f for f in os.listdir(script_dir) if
                       os.path.isfile(os.path.join(script_dir, f)) and f.endswith(('.png', '.jpg')) and f[
                                                                                                        :-4].isdigit()]
        if image_files:
            image_paths = [os.path.join(script_dir, f) for f in image_files]
            random.shuffle(image_paths)
            return image_paths
        return []

    def get_next_image_path(self):
        if self.image_paths:
            path = self.image_paths[self.current_image_index]
            self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
            return path
        return None

    def shoot(self, target_pos):
        if self.reloading:
            return  # Не стреляем во время перезарядки

        current_time = pygame.time.get_ticks()

        if self.bullets_in_magazine > 0:
            bullet_speed = 10
            image_path = self.get_next_image_path()
            if image_path:
                bullet = Bullet(self.rect.center, target_pos, bullet_speed, image_path)
                self.bullets.add(bullet)
                self.bullets_in_magazine -= 1
                self.last_shot_time = current_time

        if self.bullets_in_magazine == 0 and not self.reloading:  # если обойма пустая, начинаем перезарядку
            self.reloading = True
            self.show_reloading_text = True  # Показываем надпись
            self.last_shot_time = current_time  # Обновляем таймер

    def update(self):
        current_time = pygame.time.get_ticks()
        if self.reloading:
            if current_time - self.last_shot_time >= self.reload_time:
                self.bullets_in_magazine = self.magazine_size  # Перезарядка
                self.reloading = False
                self.show_reloading_text = False  # Скрываем надпись
        self.bullets.update()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.bullets.draw(screen)
        # Отображение количества патронов
        font = pygame.font.Font(None, 30)
        text = font.render(f"Ammo: {self.bullets_in_magazine}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        if self.show_reloading_text:  # Проверяем флаг, чтобы отображать надпись только когда она нужна
            text = font.render(f"Reloading", True, (255, 0, 0))
            screen.blit(text, (10, 40))


if __name__ == '__main__':
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Shooting Example")

    clock = pygame.time.Clock()

    shooter = Shooter()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # Стрельба по нажатию кнопки мыши
                if event.button == 1:  # Левая кнопка мыши
                    target_pos = pygame.mouse.get_pos()
                    shooter.shoot(target_pos)

        screen.fill((0, 0, 0))


        shooter.update()
        shooter.draw(screen)

        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    pygame.quit()