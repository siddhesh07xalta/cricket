from team import Team
from player import Player
from over import Over

class Game:
    def __init__(self):
        self.team1 = None
        self.team2 = None
    
    def start_game(self):
        print("Welcome to Cricket Game")
        # function to setup teams
        self.setup_teams()
        
    def setup_teams(self):
        team_1_name = input("Enter Team 1 name: ")
        team_2_name = input("Enter Team 2 name: ")

        # creating two team objects for two teams
        self.team1 = Team(team_1_name)
        self.team2 = Team(team_2_name)

        print(f'\n Enter details for {team_1_name}')
        self.team1.add_player()

        print(f'\n Enter details for {team_2_name}')
        self.team2.add_player()


        print(self.team1)

        print(self.team2)

    def create_teams(self):
        pass

    def conduct_toss(self):
        pass
    
    def play_innings(self):
        pass

    def select_bowler(self):
        pass

    def select_batsman(self):
        pass

    def show_scoreboard(self):
        pass

    def display_results(self):
        pass

    def man_of_match(self):
        pass

    def highest_wicket_taker(self):
        pass