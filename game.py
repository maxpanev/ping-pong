import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение размеров окна
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)

# Создание окна
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Пинг-понг")

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Определение классов
class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move(self, up=True):
        if up:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y):
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.radius = radius

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)

    def bounce(self):
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x *= -1

# Создание объектов
paddle_left = Paddle(30, HEIGHT // 2 - 60, 10, 120, 10)
paddle_right = Paddle(WIDTH - 40, HEIGHT // 2 - 60, 10, 120, 10)
ball = Ball(WIDTH // 2, HEIGHT // 2, 15, 2, 2)  # Замедление скорости мяча

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление ракетками
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_left.rect.top > 0:
        paddle_left.move(up=True)
    if keys[pygame.K_s] and paddle_left.rect.bottom < HEIGHT:
        paddle_left.move(up=False)
    if keys[pygame.K_UP] and paddle_right.rect.top > 0:
        paddle_right.move(up=True)
    if keys[pygame.K_DOWN] and paddle_right.rect.bottom < HEIGHT:
        paddle_right.move(up=False)

    # Перемещение и отскок мяча
    ball.move()
    ball.bounce()

    # Проверка столкновений с ракетками
    if ball.rect.colliderect(paddle_left.rect) or ball.rect.colliderect(paddle_right.rect):
        ball.speed_x *= -1
    screen.fill(BLACK)

    # Отрисовка объектов
    paddle_left.draw(screen)
    paddle_right.draw(screen)
    ball.draw(screen)

    # Обновление экрана
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()