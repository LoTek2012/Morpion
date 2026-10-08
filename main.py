from game.board import show_grid, create_grid
from game.player import ask_coordinates
from config import PLAYER_SYMBOL, AI_SIMBOL, FIRST_PLAYER, NB_CASE
from game.logic import winner_calculation, replay_game
from game.ai import choose_coordinates
import sys

def main():

    running = True
    while running == True :

        turn = FIRST_PLAYER
        grid = create_grid()

        for case in range(NB_CASE) :
    
            if turn == "Player":
                show_grid(grid)
                line, column = ask_coordinates(grid)
                grid[line][column] = PLAYER_SYMBOL
                turn = "AI"
        
            elif turn == "AI" :
                line, column = choose_coordinates(grid)
                grid[line][column] = AI_SIMBOL
                print(f"IA a joué {line, column}")
                turn = "Player"

            win, winner = winner_calculation(grid)
            
            if win == True :
                show_grid(grid)
                if winner == "Player" :
                    print("👏 Tu as gagné !")
                elif winner == "AI" :
                    print("👎 Tu as perdu !")
                break

        if win == False :
            print("🤝 ÉGALITÉ !")

        replay = replay_game()
        if replay == False :
            running = False


if __name__ == "__main__":
    main()

sys.exit()
