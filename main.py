from game import Game


def main():
    print("Welcome to Cricket Game!")
    overs = 3
    # game class 
    game = Game(overs)
    game.start_game()

main()