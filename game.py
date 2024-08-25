import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Параметры окна
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption('Игра "Выживание"')

# Загрузка изображений
player_image = pygame.image.load('Python.png')
player_rect = player_image.get_rect()

enemy_image = pygame.image.load('Java.png')
enemy_rect = enemy_image.get_rect()

# Настройки игрока
player_speed = 5

# Настройки врагов
enemy_speed = 0.45
enemy_spawn_time = 2000  # Время появления новых врагов в миллисекундах

# Список врагов
enemies = []

# Таймер для появления врагов
pygame.time.set_timer(pygame.USEREVENT, enemy_spawn_time)

# Игровой цикл
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.USEREVENT:
            # Создание нового врага
            new_enemy_rect = enemy_image.get_rect()
            new_enemy_rect.x = random.randint(0, window_size[0] - enemy_rect.width)
            new_enemy_rect.y = random.randint(0, window_size[1] - enemy_rect.height)
            enemies.append(new_enemy_rect)

    # Получение позиции мыши
    mouseX, mouseY = pygame.mouse.get_pos()
    player_rect.x = mouseX - player_rect.width // 2
    player_rect.y = mouseY - player_rect.height // 2

    # Обновление позиции врагов
    for enemy in enemies:
        enemy.y += enemy_speed
        if enemy.y > window_size[1]:
            enemies.remove(enemy)

    # Проверка на столкновение
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            print('Произошло столкновение!')
            pygame.quit()
            sys.exit()

    # Отрисовка
    screen.fill((0, 0, 0))
    screen.blit(player_image, player_rect)
    for enemy in enemies:
        screen.blit(enemy_image, enemy)
    pygame.display.flip()

pygame.quit()