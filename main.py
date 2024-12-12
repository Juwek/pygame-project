import pygame


def draw(width, height):
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 255, 255), (0, 0), (width, height), 5)
    pygame.draw.line(screen, (255, 255, 255), (width, 0), (0, height), 5)


if __name__ == '__main__':
    try:
        pygame.init()
        size = width, height = list(map(lambda x: int(x), input().split()))
        screen = pygame.display.set_mode(size)

        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.flip()
            draw(width, height)

        pygame.quit()
    except ValueError:
        print('Неправильный формат ввода')