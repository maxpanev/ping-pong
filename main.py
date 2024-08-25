import pygame
pygame.init() # Эта функция инициализирует все основные модули pygame
import time

window_size = (800, 600) # Настраиваем размер окна
screen = pygame.display.set_mode(window_size) # Создаем экран
pygame.display.set_caption('Игра "Тест"') # Даем название окна

# Загружаем изображения
image = pygame.image.load('images/Python.png') # Загружаем фоновое изображение
image_rect = image.get_rect() # Создаём переменную для хитбокса
#speed = 1 # Задаём скорость

image2 = pygame.image.load('images/Java.png') # Загружаем второе фоновое изображение
image_rect2 = image2.get_rect()

# Загружаем игровой цикл
run = True

while run:
    for event in pygame.event.get(): # Обрабатываем события
        if event.type == pygame.QUIT: # Если нажата кнопка "выход"
            run = False # Завершаем игру

    #Настраиваем движение с помощью клавиш
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     image_rect.x -= speed
    # if keys[pygame.K_RIGHT]:
    #     image_rect.x += speed
    # if keys[pygame.K_UP]:
    #     image_rect.y -= speed
    # if keys[pygame.K_DOWN]:
    #     image_rect.y += speed

    # # Либо настраиваем движение с помощью мышки
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect.x = mouseX - 40
            image_rect.y = mouseY - 40

    if image_rect.colliderect(image_rect2):
        print('Произошло столкновение!')
        time.sleep(1)

    screen.fill((0, 0, 0)) # Настраиваем цвет фона
    screen.blit(image, image_rect) # Выводим изображение на экране
    screen.blit(image2, image_rect2)  # Выводим изображение на экране
    pygame.display.flip()

pygame.quit()