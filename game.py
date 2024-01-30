import pygame
import random
import time


def main(number, num):
    start_time = time.time()
    pygame.init()
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 550
    X = WINDOW_WIDTH
    Y = WINDOW_HEIGHT
    play_flag = 1
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Puzzle Game')
    FPS = 30
    clock = pygame.time.Clock()
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    CRIMSON = (220, 20, 60)
    ORANGE = (255, 127, 0)
    font_title = pygame.font.Font(None, 64)
    font_content = pygame.font.Font(None, 40)
    selected_img = None
    is_game_over = False
    all_time = None
    rows = None
    cols = None
    cell_width = None
    cell_height = None
    cell_wh = list()
    cells = list()
    pause_im = pygame.image.load("data/pause.png")
    play_im = pygame.image.load("data/play.png")
    delta_time = 0
    play_again_text = font_title.render('You WIN!', True, WHITE)
    play_again_rect = play_again_text.get_rect()
    play_again_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    continue_text = font_content.render('Press Escape', True, WHITE)
    continue_rect = continue_text.get_rect()
    continue_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50)

    def start_game(mode):
        global cell_width, cell_height
        rows = mode
        cols = mode
        num_cells = rows * cols
        cell_width = 800 // rows
        cell_height = 450 // cols
        rand_indexes = list(range(0, num_cells))
        cell_wh.append(cell_width)
        cell_wh.append(cell_height)
        for i in range(num_cells):
            x = (i % rows) * cell_width
            y = (i // cols) * cell_height
            rect = pygame.Rect(x, y, cell_width, cell_height)
            rand_pos = random.choice(rand_indexes)
            rand_indexes.remove(rand_pos)
            cells.append({'rect': rect, 'border': WHITE,
                          'order': i, 'pos': rand_pos})

    bg = pygame.image.load(number)
    bg_rect = bg.get_rect()
    bg_rect.topleft = (0, 0)
    running = True
    start_game(num)
    while running:
        screen.fill(CRIMSON)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    if is_game_over:
                        return 1
                    else:
                        return 0
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not is_game_over:
                mouse_pos = pygame.mouse.get_pos()
                pos = mouse_pos
                if X - 50 < pos[0] < X and Y > pos[1] > Y - 50:
                    play_flag += 1
                    play_flag %= 2
                for cell in cells:
                    rect = cell['rect']
                    order = cell['order']
                    if rect.collidepoint(mouse_pos):
                        if not selected_img:
                            selected_img = cell
                            cell['border'] = RED
                        else:
                            current_img = cell
                            if current_img['order'] != selected_img['order']:
                                # swap images
                                temp = selected_img['pos']
                                cells[selected_img['order']
                                      ]['pos'] = cells[current_img['order']]['pos']
                                cells[current_img['order']]['pos'] = temp
                                cells[selected_img['order']]['border'] = WHITE
                                selected_img = None
                                # check if puzzle is solved
                                is_game_over = True
                                for cell in cells:
                                    if cell['order'] != cell['pos']:
                                        is_game_over = False
        else:
            if play_flag:
                screen.blit(pause_im, (X - 50, Y - 50))
            else:
                screen.blit(play_im, (X - 50, Y - 50))
            if not is_game_over:
                for i, val in enumerate(cells):
                    pos = cells[i]['pos']
                    img_area = pygame.Rect(
                        cells[pos]['rect'].x, cells[pos]['rect'].y, cell_wh[0], cell_wh[1])
                    screen.blit(bg, cells[i]['rect'], img_area)
                    pygame.draw.rect(
                        screen, cells[i]['border'], cells[i]['rect'], 1)

                if play_flag:
                    finish_time = time.time()
                    all_time = finish_time - start_time + delta_time
                    font = pygame.font.Font(None, 90)
                    text = font.render(
                        str(round(all_time)), True, WHITE)
                    screen.blit(text, (400, 475))
                else:
                    delta_time = all_time
                    start_time = time.time()
                    text = font.render(
                        str(round(delta_time)), True, WHITE)
                    screen.blit(text, (400, 475))
            else:
                font = pygame.font.Font(None, 90)
                text = font.render(str(round(all_time)), True, WHITE)
                screen.blit(text, (400, 475))
                screen.blit(bg, bg_rect)
                screen.blit(play_again_text, play_again_rect)
                screen.blit(continue_text, continue_rect)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    main('data/11.jpg', 3)
