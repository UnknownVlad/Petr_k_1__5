import random
import time

from some_data import data
from some_data.color import Color


class Auxiliary:

    @staticmethod
    def convert_to_xy(row: int, col: int) -> tuple:
        return (col * data.r() * 2, row * data.r() * 2)

    @staticmethod
    def convert_to_center(row: int, col: int) -> tuple:
        return (col * data.r() * 2 + data.r(), row * data.r() * 2+data.r())

    @staticmethod
    def convert_to_rowcol(x: int, y: int) -> tuple:
        return (y // (data.r()*2), x // (data.r()*2))

