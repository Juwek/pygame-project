import pygame
import math


class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_pos, target_pos, speed, color):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=start_pos)
        self.speed = speed

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

    def shoot(self, target_pos):
        bullet_speed = 10
        bullet_color = (255, 0, 0)  # Красные пули
        bullet = Bullet(self.rect.center, target_pos, bullet_speed, bullet_color)
        self.bullets.add(bullet)

    def update(self):
        self.bullets.update()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.bullets.draw(screen)


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

        screen.fill((0, 0, 0))  # Заполняем экран черным цветом

        shooter.update()
        shooter.draw(screen)

        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    pygame.quit()