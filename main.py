from game import Game
from utils import validate_input

def main():
    try:
        print("Welcome to Cricket Game !")
        number_of_overs = validate_input("Enter number of overs you want to play :  ", str)
        # game class 
        game = Game(number_of_overs)

        # creating game object and starting game
        game.start_game()
        
    except Exception as e:
        print(f'Error in main function: {e}')

main()