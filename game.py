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
RED = (255, 0, 0)

# Шрифт
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

# Начальная скорость мяча
INITIAL_SPEED_X = 4
INITIAL_SPEED_Y = 4
SPEED_INCREMENT = 0.5  # Увеличение скорости мяча при каждом отскоке от ракетки

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
        pygame.draw.ellipse(screen, RED, self.rect)

    def bounce(self):
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

    def reset_position(self):
        self.rect.x = WIDTH // 2 - self.radius
        self.rect.y = HEIGHT // 2 - self.radius
        self.speed_x = INITIAL_SPEED_X * (-1 if self.speed_x > 0 else 1)  # Сброс скорости
        self.speed_y = INITIAL_SPEED_Y * (1 if self.speed_y > 0 else -1)

# Создание объектов
paddle_left = Paddle(30, HEIGHT // 2 - 60, 10, 120, 10)
paddle_right = Paddle(WIDTH - 40, HEIGHT // 2 - 60, 10, 120, 10)
ball = Ball(WIDTH // 2, HEIGHT // 2, 15, INITIAL_SPEED_X, INITIAL_SPEED_Y)

# Переменные счета
score_left = 0
score_right = 0

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
        # Увеличение скорости при отскоке от ракетки
        ball.speed_x += SPEED_INCREMENT if ball.speed_x > 0 else -SPEED_INCREMENT
        ball.speed_y += SPEED_INCREMENT if ball.speed_y > 0 else -SPEED_INCREMENT

    # Проверка на выход мяча за границы
    if ball.rect.left <= 0:
        score_right += 1
        ball.reset_position()
    elif ball.rect.right >= WIDTH:
        score_left += 1
        ball.reset_position()

    # Очистка экрана
    screen.fill(BLACK)

    # Отрисовка объектов
    paddle_left.draw(screen)
    paddle_right.draw(screen)
    ball.draw(screen)

    # Отображение счета
    score_text_left = font.render(str(score_left), True, WHITE)
    score_text_right = font.render(str(score_right), True, WHITE)
    screen.blit(score_text_left, (WIDTH // 4, 10))
    screen.blit(score_text_right, (WIDTH * 3 // 4, 10))

    # Проверка на победу
    if score_left >= 2 or score_right >= 2:
        winner_text = "Победил" + " " + ("левый" if score_left >= 2 else "правый") + " " + "игрок "
        winner_surface = small_font.render(winner_text, True, WHITE)
        screen.blit(winner_surface, (WIDTH // 2 - winner_surface.get_width() // 2, HEIGHT // 2))

        pygame.display.flip()
        pygame.time.wait(3000)  # Пауза перед сбросом

        # Сброс счета и позиции
        score_left = 0
        score_right = 0
        ball.reset_position()

    # Обновление экрана
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()