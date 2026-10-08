from config import EMPTY_SYMBOL, SIZE_GRID

# =========== Demander au joueur d'écrir les coordonné de son coup ==========
def ask_coordinates(grid):
    
    while True:
        
        try:
            line, column = input("Entre les coordonnés de ton coup (ex : 1 2) : ").split()
            line = int(line)
            column = int(column)

            if not line < SIZE_GRID or not column < SIZE_GRID :
                print("ENTRÉ INVALIDE : Position hors de la grille !")
                
            elif not grid[line][column] == EMPTY_SYMBOL :
                print("ENTRÉ INVALIDE : Case déjà occupé !")
                print(line, column)
                               
            else : return line, column

        except ValueError or IndexError : # IndexError pour int() et ValueError pour .split()
            print("ENTRÉ INVALIDE : Veuillez saisir deux nombre entier !")

        

        