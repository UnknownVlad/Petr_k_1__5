import random
import time

import pygame


from game_logic.auxiliary import Auxiliary
from some_data import data

from some_data.color import Color


class Game_board:

    def __init__(self, row, col, score):
        self.matrix = [
            [None for i in range(row)] for j in range(col)
        ]
        self.__fill_matrix()
        self.row = row
        self.col = col
        self.score = score
        self.tmp_score = 0
        self.start_time = time.time()
        self.choosed = None


    def __get_rnd_color(self):

        r = random.randint(0, 100)
        if data.chance_white()[0] <= r <= data.chance_white()[1]:
            return list(Color)[3]
        elif data.chance_black()[0] <= r <= data.chance_black()[1]:
            return list(Color)[4]
        else:
            return list(Color)[random.randint(0, data.valid_colors()-1)]

    def __fill_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == None:
                    self.matrix[i][j] = self.__get_rnd_color()

    def output(self, screen):
        if self.choosed is not None:
            self.__draw_borders(screen)
        self.__draw_board(screen)

    def __draw_board(self, screen):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == None:
                    continue
                if self.matrix[i][j].value == Color.WHITE.value:
                    self.__draw_white_circle(screen, i, j)
                elif self.matrix[i][j].value == Color.BLACK.value:
                    self.__draw_black_circle(screen, i, j)
                else:
                    self.__draw_defult_circle(screen, i, j)
                #Rect(self.matrix[i][j].value, Auxiliary.convert_to_xy(i, j)).output(screen)

    def __draw_defult_circle(self, screen, i, j):
        pygame.draw.circle(screen, self.matrix[i][j].value, Auxiliary.convert_to_center(i, j), data.r()-4)

    def __draw_white_circle(self, screen, i, j):
        pygame.draw.circle(screen, self.matrix[i][j].value, Auxiliary.convert_to_center(i, j), data.r()-4, 5)

    def __draw_black_circle(self, screen, i, j):
        c = Auxiliary.convert_to_center(i, j)
        pygame.draw.circle(screen, self.matrix[i][j].value, c, data.r()-4, 5)
        pygame.draw.circle(screen, self.matrix[i][j].value, c, data.r() - 20, 5)

    def __draw_rect(self, screen, i, j):
        v = Auxiliary.convert_to_xy(i, j)
        pygame.draw.rect(screen, data.fill_color(), (v[0], v[1], data.r()*2, data.r()*2) )



    def __draw_borders(self, screen):
        for row, col in self.choosed:
            self.__draw_rect(screen, row, col)


    def update(self, x, y):
        i, j = Auxiliary.convert_to_rowcol(x, y)
        if self.choosed is None:
            if self.matrix[i][j] != Color.BLACK:
                self.choosed = self.__find_reachable_positions(i, j)
                if(len(self.choosed) < 3):
                    self.choosed = None
            else:
                print("+++++")
                self.choosed = [
                    (i, j),
                    (i-1, j),
                    (i, j-1),
                    (i-1, j-1),
                    (i+1, j),
                    (i, j+1),
                    (i+1, j+1),
                    (i-1, j+1),
                    (i+1, j-1),
                    (i+2, j),
                    (i, j+2),
                    (i-2, j),
                    (i, j-2)
                ]
        elif Auxiliary.convert_to_rowcol(x, y) not in self.choosed:
            print(Auxiliary.convert_to_rowcol(x, y))
            print(self.choosed)
            print(self.choosed)
            self.choosed = None
        else:
            self.tmp_score+=len(self.choosed)**2
            self.__kill_cells()
            self.__group_blocks()
            self.__fill_matrix()

    def __kill_cells(self):
        for row, col in self.choosed:
            if not self.__check_borders(row, col):
                continue
            self.matrix[row][col] = None
        self.choosed = None
    def __check_borders(self, r, c):
        return 0 <= r < self.row and 0 <= c < self.col
    def __group_blocks(self):
        blocks = []
        for col in range(len(self.matrix[0])):
            block = self.__get_not_empty_blocks_row(col)
            if len(block) != 0:
                blocks.append(block)

        self.matrix = [[None for j in range(self.col)] for i in range(self.row)]
        for col in range(len(blocks)):
            self.__gule(col, blocks[col])

    def __gule(self, col: int, blocks: list):
        for i in range(len(blocks)):
            self.matrix[len(self.matrix) - i - 1][col] = blocks[i]

    def __clear_pos_row(self, col: int):
        for i in range(len(self.matrix)):
            self.matrix[i][col] = None

    def __get_not_empty_blocks_row(self, col: int) -> list:
        blocks = []
        for i in range(len(self.matrix)):
            if self.matrix[i][col] != None:
                blocks.insert(0, self.matrix[i][col])
        return blocks

    def __find_reachable_positions(self, start_row, start_col):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        visited = [[False] * cols for _ in range(rows)]
        reachable_positions = []

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            if visited[row][col]:
                return
            if self.matrix[start_row][start_col] != self.matrix[row][col] and self.matrix[row][col] != Color.WHITE:
                return

            visited[row][col] = True
            reachable_positions.append((row, col))

            # Движение вправо
            dfs(row, col + 1)
            # Движение вниз
            dfs(row + 1, col)
            # Движение влево
            dfs(row, col - 1)
            # Движение вверх
            dfs(row - 1, col)

        dfs(start_row, start_col)
        return reachable_positions

    def __reconstruct(self, r, c, sub):
        for i in range(2):
            for j in range(2):
                self.matrix[i+r][j+c] = sub[i][j]
    def __sub_matrix(self, r: int, c:int):
        return  [row[c:c+2] for row in self.matrix[r:r+2]]
    def __rotate_matrix(self, sub):
        transposed = list(zip(*sub))
        rotated = [list(row[::-1]) for row in transposed]
        return rotated

    def __is_equalse_color(self, sub):
        return len(set([element for row in sub for element in row])) == 1

    def is_winner(self):
        return self.__is_equalse_color(self.__sub_matrix(0, 0)) \
            and self.__is_equalse_color(self.__sub_matrix(2, 0)) \
            and self.__is_equalse_color(self.__sub_matrix(2, 2)) \
            and self.__is_equalse_color(self.__sub_matrix(0, 2))


