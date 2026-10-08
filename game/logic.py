# logic.py
from config import SIZE_GRID,PLAYER_SYMBOL, AI_SIMBOL, YES_ANSWER, NO_ANSWER

# ========== Calcule du gagnant ==========
def winner_calculation(grid):

    # Lignes
    for line in range(SIZE_GRID):
        for column in range(SIZE_GRID):
            if not grid[line][column] == PLAYER_SYMBOL :
                break
            elif column == SIZE_GRID - 1 :
                return True, 'Player'
    for line in range(SIZE_GRID):
        for column in range(SIZE_GRID):
            if not grid[line][column] == SIZE_GRID :
                break
            elif column == SIZE_GRID - 1 :
                return True, 'AI'
        
    # Colonnes
    for column in range(SIZE_GRID):
        for line in range(SIZE_GRID):
            if not grid[line][column] == PLAYER_SYMBOL :
                break
            elif line == SIZE_GRID - 1 :
                return True, 'Player'
    for column in range(SIZE_GRID):
        for line in range(SIZE_GRID):
            if not grid[line][column] == AI_SIMBOL :
                break
            elif line == SIZE_GRID - 1 :
                return True, 'AI'
        
    # Diagonal principale
    for line in range(SIZE_GRID):
        if not grid[line][line] == PLAYER_SYMBOL :
            break
        elif line == SIZE_GRID - 1 :
            return True, 'Player'
    for line in range(SIZE_GRID):
        if not grid[line][line] == AI_SIMBOL :
            break
        elif line == SIZE_GRID - 1 :
            return True, 'AI'
        
            
    # Diagonal secondaire
    for line in range(SIZE_GRID):
        column = SIZE_GRID - 1 - line
        if not grid[line][column] == PLAYER_SYMBOL :
            break
        elif line == SIZE_GRID - 1 :
            return True, 'Player'
    for line in range(SIZE_GRID):
        column = SIZE_GRID - 1 - line
        if not grid[line][column] == PLAYER_SYMBOL :
            break
        elif line == SIZE_GRID - 1 :
            return True, 'AI'
        
    return False, None

def replay_game():
    while True :
        answer = input("Veux tu refaire une partie (o/n) : ").lower()
        if answer in NO_ANSWER :
            print("Au revoir")
            return False
        elif answer in YES_ANSWER :
            print("🤩 OK on recommence !")
            return True
        else :
            print(f"ENTRÉ INVALIDE : Tu ne ne peut repondre uniquement par {YES_ANSWER} ou par {NO_ANSWER} !")
