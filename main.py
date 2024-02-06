import pygame
import game
import pyperclip
from PIL import Image
from math import *
import json
import os
import shutil
import tkinter as tk
from tkinter import messagebox
import sprite

pygame.init()

# Константы окна
X = 1000
Y = 600
FPS = 40
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (238, 159, 34)

# Флаги
game_run_flag = True
im_flag = True
window_flag = -2
enter_num_flag = 0
enter_path_flag = 0

# Подгрузка изображений
zastav_im = pygame.image.load("data/imgs/first.jpg")
fone_im = pygame.image.load("data/imgs/fone.png")
difficulty_im = pygame.image.load("data/imgs/difficulty.png")
pers_level_im = pygame.image.load("data/imgs/pers_level.png")
star_im = pygame.image.load("data/imgs/star.png")
levels_im = pygame.image.load("data/imgs/levels.jpg")
error_im = pygame.image.load("data/imgs/error.png")
menu_im = pygame.image.load("data/imgs/menu.png")

# Объявление переменных
all_sprites = sprite.main()
screen = pygame.display.set_mode([X, Y])
loading = 0
clock = pygame.time.Clock()
difficulty = 3
str_difficulty = str()
str_level = str()
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
            if window_flag == -2:
                window_flag = -1
            elif window_flag == -1:
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
                        game_class = game.Game(
                            f"data/imgs/{number}.jpg", difficulty)
                        star = game_class.main()
                        screen = pygame.display.set_mode([X, Y])
                        if star == 1:
                            if number not in lst:
                                stars += star
                                lst.append(number)
                    star = 0
                elif window_flag == 2:
                    enter_path_flag = 1
                elif window_flag == 3:
                    enter_num_flag = 1
                    if 163 < pos[0] < 867 and 424 < pos[1] < 551:
                        if str_difficulty == str():
                            str_difficulty = "3"
                        difficulty = int(str_difficulty)
                        if difficulty < 3 or difficulty > 100:
                            difficulty = 3
                        str_difficulty = str()
                        window_flag = 0
                if str(window_flag) in "123":
                    if 0 < pos[0] < 50 and 0 < pos[1] < 50:
                        window_flag = 0
                if str(window_flag) in "012":
                    enter_num_flag = 0
                if str(window_flag) in "013":
                    enter_path_flag = 0
                    str_level = str()
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
            if enter_num_flag:
                if event.key == pygame.K_RETURN:
                    if str_difficulty == str():
                        str_difficulty = "3"
                    difficulty = int(str_difficulty)
                    if difficulty < 3 or difficulty > 100:
                        difficulty = 3
                    str_difficulty = str()
                    window_flag = 0
                if 48 <= event.key <= 57:
                    if str_difficulty == str():
                        str_difficulty = str()
                    temp = event.key - 48
                    str_difficulty += str(temp)
                if event.key == pygame.K_BACKSPACE:
                    if len(str_difficulty) > 0:
                        str_difficulty = str_difficulty[:-1]
            if enter_path_flag:
                if pygame.key.get_mods() & pygame.KMOD_CTRL:
                    if event.key == pygame.K_v:
                        str_level += pyperclip.paste()
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    if event.key in (54, 59):
                        str_level += ':'
                    if event.key == 45:
                        str_level += '_'
                    if event.key in (44, 46):
                        str_level += '.'
                    if 97 <= event.key <= 122 or 48 <= event.key <= 57:
                        if event.key == pygame.K_v and str_level[-1 * len(pyperclip.paste()):] == pyperclip.paste():
                            pass
                        else:
                            str_level += chr(event.key).upper()
                    if event.key == 92:
                        str_level += chr(event.key).upper()
                else:
                    if 97 <= event.key <= 122 or 48 <= event.key <= 57:
                        if event.key == pygame.K_v and str_level[-1 * len(pyperclip.paste()):] == pyperclip.paste():
                            pass
                        else:
                            str_level += chr(event.key)
                    if event.key == 92:
                        str_level += chr(event.key)
                    if event.key in (54, 59):
                        str_level += ':'
                    if event.key == 45:
                        str_level += '_'
                    if event.key in (44, 46):
                        str_level += '.'
                    if event.key == pygame.K_ESCAPE:
                        str_level = str()
                    if event.key == pygame.K_BACKSPACE:
                        if str(str_level):
                            str_level = str_level[:-1]
                    if event.key == pygame.K_RETURN:
                        try:
                            str_level = str_level.strip().lower()
                            shutil.copyfile(str_level,
                                            "data/imgs/person.png")
                            img = Image.open("data/imgs/person.png")
                            img = img.resize((800, 450))
                            img.save("data/imgs/person.png")
                            game_class = game.Game(
                                f"data/imgs/person.png", difficulty)
                            star = game_class.main()
                            screen = pygame.display.set_mode([X, Y])
                            stars += star
                        except Exception as e:
                            print(type(e).__name__)
                            tk.Tk().wm_withdraw()
                            messagebox.showerror(
                                'Error', 'Неправильный путь до файла')
                            window_flag = 0
                        finally:
                            screen = pygame.display.set_mode([X, Y])
                            str_level = str()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
    if window_flag == -1:
        screen.fill(BLACK)
        all_sprites.update()
        all_sprites.draw(screen)
        font = pygame.font.Font(None, 90)
        text = font.render("Загрузка:", True, WHITE)
        screen.blit(text, (x + 340, y + 120))
        pygame.draw.rect(screen, WHITE, (150, 350, 700, 50), 5)
        if loading < 700:
            loading += 2
            pygame.draw.rect(screen, WHITE, (150, 350, loading, 50))
        else:
            window_flag = 0
    if window_flag == 0:
        screen.blit(fone_im, (x - 5, y - 5))
    elif window_flag == 1:
        screen.blit(levels_im, (x, y))
    elif window_flag == 2:
        screen.blit(pers_level_im, (x - 50, y - 50))
        font = pygame.font.Font(None, 60)
        text = font.render(str_level, True, WHITE)
        screen.blit(text, (40, 260))
    elif window_flag == 3:
        screen.blit(difficulty_im, (x, y))
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
