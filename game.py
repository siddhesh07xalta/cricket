from team import Team
from player import Player
from over import Over
import random

class Game:
    def __init__(self, overs):
        self.team1 = None
        self.team2 = None
        self.batting_team = None
        self.bowling_team = None
        self.target_score = None
        self.overs = overs

    def start_game(self):
        
        # Setup teams
        self.setup_teams()

        # Conduct toss
        batting_first_team = self.conduct_toss()
        bowling_first_team = self.team1 if batting_first_team == self.team2 else self.team2

        # First Innings
        self.batting_team = batting_first_team
        self.bowling_team = bowling_first_team
        
        print(f"\n--- First Innings: {self.batting_team.name} batting ---\n")
        self.play_innings(self.batting_team, self.bowling_team)

        # self.target_score = self.batting_team.score + 1
        # print(f"\nTarget for {self.bowling_team.name}: {self.target_score} runs to win\n")

        # # Second Innings
        # self.batting_team, self.bowling_team = self.bowling_team, self.batting_team
        
        # print(f"\n--- Second Innings: {self.batting_team.name} batting ---\n")
        # self.play_innings(self.batting_team, self.bowling_team)

        # # Show results
        # self.display_results()

    def setup_teams(self):
        team_1_name = input("Enter Team 1 name: ")
        team_2_name = input("Enter Team 2 name: ")

        self.team1 = Team(team_1_name)
        self.team2 = Team(team_2_name)

        print(f"\nEnter details for {team_1_name}:")
        self.team1.add_player()
        print(self.team1)

        print(f"\nEnter details for {team_2_name}:")
        self.team2.add_player()
        print(self.team2)

    def conduct_toss(self):
        toss_winner = random.choice([self.team1, self.team2])
        print(f"\n{toss_winner.name} won the toss!")

        choice = int(input(f"What does {toss_winner.name} want to do?\n1. Bat\n0. Bowl\nChoice: "))

        if choice == 1:
            batting_first_team = toss_winner
        else:
            batting_first_team = self.team1 if toss_winner == self.team2 else self.team2

        print(f"\n{batting_first_team.name} will bat first.\n")
        return batting_first_team

    def play_innings(self, batting, bowling):
        batting_team = batting
        bowling_team = bowling

        striker, non_striker = batting_team.select_openers()

       

    def display_results(self):
        pass

    def man_of_match(self):
        pass

    def highest_wicket_taker(self):
        pass