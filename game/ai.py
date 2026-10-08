from config import EMPTY_SYMBOL, SIZE_GRID
from random import randint

def choose_coordinates(grid):
    while True :
        line = randint(0, SIZE_GRID-1)
        column = randint(0, SIZE_GRID-1)

        if grid[line][column] == EMPTY_SYMBOL :
            return line, column
    