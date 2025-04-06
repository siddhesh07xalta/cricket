from game import Game
from utils import validate_input
# main function of the program
def main():
    try:
        print("Welcome to Cricket Game !")
        number_of_overs = validate_input("Enter number of overs you want to play :  ", int, 1)
        
        # game object
        game_obj = Game(number_of_overs)

        # creating game object and calling start game function
        game_obj.start_game()
    
    except Exception as e:
        print(f'Error in main function: {e}')

main()