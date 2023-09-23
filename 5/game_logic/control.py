import sys

import pygame


from game_logic import game_board
from game_logic.auxiliary import Auxiliary
from some_data import data


class control:
    def __init__(self):
        pass

    def events(self, board: game_board):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.update(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

            #board.choosed = Auxiliary.type_role(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        return True


