# board.py

from config import SIZE_GRID, EMPTY_SYMBOL

# ========== Création de la grille ===========
def create_grid():
    return [[EMPTY_SYMBOL for i in range(SIZE_GRID)] for i in range(SIZE_GRID)]

# ========== Affichage de la grille ===========
        
def show_grid(grid):
    print()
    for column in range(SIZE_GRID):
        print(f" {column}  ", end="")

    print()

    for line in range(SIZE_GRID):
        
        for column in range(SIZE_GRID):
            if column == SIZE_GRID - 1 :
                print(f" {grid[line][column]}   {line}")
            else :
                print(f" {grid[line][column]} |", end="")
        
        if not line == SIZE_GRID - 1 :
            
            for column in range(SIZE_GRID):
                if column == SIZE_GRID - 1 :
                    print("---")
                else :    
                    print("---+", end="")
    print()

