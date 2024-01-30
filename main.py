import pygame
import game
from math import *
import json
import os

pygame.init()

# Константы окна
X = 1000
Y = 600
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (238, 159, 34)

# Флаги
game_run_flag = True
im_flag = True
window_flag = -1
enter_flag = 0

# Объявление переменных
screen = pygame.display.set_mode([X, Y])
clock = pygame.time.Clock()
zastav_im = pygame.image.load("data/first.jpg")
fone_im = pygame.image.load("data/fone.png")
pers_level_im = pygame.image.load("data/pers_level.png")
star_im = pygame.image.load("data/star.png")
levels_im = pygame.image.load("data/levels.jpg")
error_im = pygame.image.load("data/error.png")
menu_im = pygame.image.load("data/menu.png")
difficulty = 3
str_difficulty = None
x = int()
y = int()

# Чтение данных из файла
lst = list()
stars = 0
if "data.json" in os.listdir():
    with open("data.json", "r") as file:
        data = json.load(file)
        lst = data["list_of_solved_pazles"]
        stars = data["count_of_stars"]


# Начальные команды
pygame.display.set_caption("Пазлы")

# Функции


def check(pos):
    c = 0
    x = pos[0]
    y = pos[1]
    if 165 < x < 265 and 65 < y < 165:
        c = 1
    if 305 < x < 405 and 65 < y < 165:
        c = 2
    if 445 < x < 545 and 65 < y < 165:
        c = 3
    if 585 < x < 685 and 65 < y < 165:
        c = 4
    if 725 < x < 825 and 65 < y < 165:
        c = 5

    if 165 < x < 265 and 195 < y < 295:
        c = 6
    if 305 < x < 405 and 195 < y < 295:
        c = 7
    if 445 < x < 545 and 195 < y < 295:
        c = 8
    if 585 < x < 685 and 195 < y < 295:
        c = 9
    if 725 < x < 825 and 195 < y < 295:
        c = 10

    if 165 < x < 265 and 325 < y < 425:
        c = 11
    if 305 < x < 405 and 325 < y < 425:
        c = 12
    if 445 < x < 545 and 325 < y < 425:
        c = 13
    if 585 < x < 685 and 325 < y < 425:
        c = 14
    if 725 < x < 825 and 325 < y < 425:
        c = 15

    if 165 < x < 265 and 445 < y < 545:
        c = 16
    if 305 < x < 405 and 445 < y < 545:
        c = 17
    if 445 < x < 545 and 445 < y < 545:
        c = 18
    if 585 < x < 685 and 445 < y < 545:
        c = 19
    if 725 < x < 825 and 445 < y < 545:
        c = 20
    return c


# Главный код
while game_run_flag:
    clock.tick(FPS)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run_flag = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            im_flag = False
            if window_flag == -1:
                window_flag = 0
            else:
                pos = event.pos
                if window_flag == 0:
                    if 50 <= pos[0] <= 400:
                        if 100 <= pos[1] <= 175:
                            window_flag = 1
                        elif 250 <= pos[1] <= 325:
                            window_flag = 2
                        elif 400 <= pos[1] <= 475:
                            window_flag = 3
                elif window_flag == 1:
                    number = check(pos)
                    if number != 0:
                        star = game.main(f"data/{number}.jpg", difficulty)
                        screen = pygame.display.set_mode([X, Y])
                        if star == 1:
                            if number not in lst:
                                stars += star
                                lst.append(number)
                    star = 0
                elif window_flag == 2:
                    pass
                elif window_flag == 3:
                    
                    enter_flag = 1
                    if 163 < pos[0] < 867 and 424 < pos[1] < 551:
                        if str_difficulty == None:
                            str_difficulty = "3"
                        difficulty = int(str_difficulty)
                        if difficulty < 3:
                            difficulty = 3
                        str_difficulty = None
                        window_flag = 0
                if str(window_flag) in "123":
                    if 0 < pos[0] < 50 and 0 < pos[1] < 50:
                        window_flag = 0
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
            if event.key in (pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9):
                if enter_flag:
                    if str_difficulty == None:
                        str_difficulty = ""
                    str_difficulty += str(event.key - 48)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass

    if window_flag == 0:
        screen.blit(fone_im, (x - 5, y - 5))
    elif window_flag == 1:
        screen.blit(levels_im, (x, y))
    elif window_flag == 2:
        screen.blit(error_im, (x, y))
    elif window_flag == 3:
        screen.blit(pers_level_im, (x, y))
        font = pygame.font.Font(None, 90)
        text = font.render(str_difficulty, True, BLACK)
        screen.blit(text, (250, 258))
    if str(window_flag) in "01":
        screen.blit(star_im, (X - 55, y))
        font = pygame.font.Font(None, 90)
        text = font.render(str(stars), True, ORANGE)
        screen.blit(text, (X - 50 - 40 * len(str(stars)), y))

        font = pygame.font.Font(None, 90)
        text = font.render(f"Сложность {difficulty}", True, WHITE)
        screen.blit(text, (x + 160, y))

    if str(window_flag) in "123":
        screen.blit(menu_im, (x, y))

    if im_flag:
        screen.blit(zastav_im, (x, y))

    pygame.display.flip()

# Запись данных
data = dict()
lst.sort()
data["list_of_solved_pazles"] = lst
data["count_of_stars"] = stars

with open("data.json", "w") as file:
    json.dump(data, file)
pygame.quit()
