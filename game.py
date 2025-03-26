from team import Team
from over import Over
import random
from utils import validate_input

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

        # print(f"--- Stats for {self.batting_team.name} ---")
        # self.batting_team.display_scoreboard()

        self.target_score = self.batting_team.score + 1
        print(f"\nTarget for {self.bowling_team.name}: {self.target_score} runs to win\n")

        # Second Innings
        self.batting_team, self.bowling_team = self.bowling_team, self.batting_team

        print(f"\n--- Second Innings: {self.batting_team.name} batting ---\n")
        self.play_innings(self.batting_team, self.bowling_team)

        # Show results
        self.display_results()

    # function to setup up teams
    def setup_teams(self):

        try:
            team_1_name = validate_input("Enter Team 1 name: ", str)
            team_2_name = validate_input("Enter Team 2 name: ", str)

            # creating team objects
            self.team1 = Team(team_1_name)
            self.team2 = Team(team_2_name)

            print(f"\nEnter details for {team_1_name}:")
            # function to add players
            self.team1.add_player()
            print()

            print(f"\nEnter details for {team_2_name}:")
            self.team2.add_player()
            print()
        except Exception as e:
            print(f'Error in setup teams function: {e}')

    # function for conducting toss
    def conduct_toss(self):

        try:
            toss_winner = random.choice([self.team1, self.team2])
            print(f"\n{toss_winner.name} won the toss!")

            choice = validate_input(f"What does {toss_winner.name} want to do?\n1.Bat\n0.Bowl\nChoice: ", int, 0,1, (1,0))

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

            for over_number in range(0, self.overs):
    
                # change it here to 10
                if batting_team.wickets == 3:
                    print(f'Innings Over ! {batting_team.name} is all out')
                    break
        
                
                if self.target_score is not None and self.batting_team.score >= self.bowling_team.score:
                    print(f'{self.batting_team.name} chased the target')
                    return

                print()
                print(f'Over Number {over_number}')
            
                bowler = bowling_team.select_bowler(previous_bowler)

                previous_bowler = bowler
                # creating over objects with the required parameters
                over = Over(bowler=bowler, striker=striker, non_striker=non_striker, batting_team=batting_team, bowling_team=bowling_team, over_number = over_number, target_score = self.target_score)
                
                # function that simulates playing over
                over.play_over()

                # adding over count to team function
                batting_team.overs_played += 1

                # print batting dashboard after every over
                batting_team.display_scoreboard()
        
        except Exception as e:
            print(f'Error in play innings function: {e}')

            
    def display_results(self):
        try:
            print()
            print()
            print("--- Match Results ---")

            if self.batting_team.score >= self.target_score:
                self.winner = self.batting_team
                # change 4 to 10
                print(f'{self.winner.name} won the match by {4 - self.batting_team.wickets} wickets !')
                print(self.winner)

            # all out
            elif self.batting_team.wickets == 3:
                self.winner = self.bowling_team
                print(f'{self.winner.name} won the match by {self.target_score - self.batting_team.score}')
                print()
                print("Player Stats")
                print(self.winner)
            
            # target not reached due to overs completion
            else:
                self.winner = self.bowling_team
                print(f'{self.winner.name} won the match by {self.target_score - self.batting_team.score}')
                print()
                print("Player Stats")
                print(self.winner)

        except Exception as e:
            print(f'Error in Displaying results: {e}')


    def man_of_match(self):
        pass

    def highest_wicket_taker(self):
        pass
