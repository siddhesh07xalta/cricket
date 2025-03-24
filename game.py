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

    # main function to start game
    def start_game(self):

        # Setup teams
        self.setup_teams()

        # Conduct toss
        # return the team who has or not win the toss but has to bat first
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

    # function to setup up teams
    def setup_teams(self):

        try:
            team_1_name = input("Enter Team 1 name: ")
            team_2_name = input("Enter Team 2 name: ")

            # creating team objects
            self.team1 = Team(team_1_name)
            self.team2 = Team(team_2_name)

            print(f"\nEnter details for {team_1_name}:")
            # function to add players
            self.team1.add_player()
            print(self.team1)

            print(f"\nEnter details for {team_2_name}:")
            self.team2.add_player()
            print(self.team2)
        
        except Exception as e:
            print(f'Error in setup teams function: {e}')

    # function for conducting toss
    def conduct_toss(self):

        try:
            toss_winner = random.choice([self.team1, self.team2])
            print(f"\n{toss_winner.name} won the toss!")

            choice = int(input(f"What does {toss_winner.name} want to do?\n1. Bat\n0. Bowl\nChoice: "))

            # conidition to select the batting team first
            if choice == 1:
                batting_first_team = toss_winner
            else:
                batting_first_team = self.team1 if toss_winner == self.team2 else self.team2

            print(f"\n{batting_first_team.name} will bat first.\n")
            return batting_first_team

        except Exception as e:
            print(f'Error in conduct_toss function: {e}')

    # function to play innings
    def play_innings(self, batting, bowling):

        try:
            batting_team = batting
            bowling_team = bowling

            # selecting striker and non striker 
            striker, non_striker = batting_team.select_openers()

            previous_bowler = None

            for over_number in range(1, self.overs+1):
                print(f'{over_number}')
            
                bowler = bowling_team.select_bowler(previous_bowler)

                previous_bowler = bowler

                if not bowler:
                    print("issue with getting bowler")
                    break

                over = Over(bowler=bowler, striker=striker, non_striker=non_striker, batting_team=batting_team, bowling_team=bowling_team, game= self)
                
                over.play_over()
        
        except Exception as e:
            print(f'Error in play innings function: {e}')

            
    def display_results(self):
        pass

    def man_of_match(self):
        pass

    def highest_wicket_taker(self):
        pass
