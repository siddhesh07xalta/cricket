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
        try: 
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
        
        except Exception as e:
            print(f'Error in start game function: {e}')

    # function to setup up teams
    def setup_teams(self):
        try:
            team_1_name = validate_input("Enter Team 1 name: ", str)
            team_2_name = validate_input("Enter Team 2 name: ", str)
            number_of_players = validate_input("Enter number of players per team: ", int, 2, 11) 

            self.team1 = Team(team_1_name, number_of_players)
            self.team2 = Team(team_2_name, number_of_players)

            print(f"\nEnter details for {team_1_name}:")
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
            print("\n--- Toss Time! ---\n")

            # Identify captains
            captains = []
            for team in [self.team1, self.team2]:
                for player_name, player in team.players.items():
                    if player.role == "Captain":
                        captains.append((player_name, team))

            # Ensure both teams have captains
            if len(captains) < 2:
                print("Error: Both teams must have a captain to conduct the toss.")
                

            # Assign captains
            tossing_captain, tossing_team = captains[0]
            calling_captain, calling_team = captains[1]

            # User selects who tosses and who calls
            print(f"Captains: {tossing_captain} ({tossing_team.name}) & {calling_captain} ({calling_team.name})")
            print("Who should toss the coin in the air?")
            print(f"1. {tossing_captain} ({tossing_team.name})")
            print(f"2. {calling_captain} ({calling_team.name})")

            toss_choice = validate_input("Enter choice (1 or 2): ", int, 1, 2)

            if toss_choice == 2:
                tossing_captain, calling_captain = calling_captain, tossing_captain
                tossing_team, calling_team = calling_team, tossing_team

            print(f"\n{tossing_captain} ({tossing_team.name}) will toss the coin.")
            print(f"{calling_captain} ({calling_team.name}) will call for the toss.")

            # Calling the toss
            print("\nTossing the coin... *flips coin in the air*")
            print(f"{calling_captain} ({calling_team.name}), call Heads or Tails!")

            call = validate_input("Enter 'Heads' or 'Tails': ", str)
            coin_result = random.choice(["Heads", "Tails"])

            print(f"\nThe coin lands... It's {coin_result}!")

            # Determine winner
            if call == coin_result:
                print(f"\n{calling_captain} ({calling_team.name}) wins the toss!")
                toss_winner = calling_team
            else:
                print(f"\n{tossing_captain} ({tossing_team.name}) wins the toss!")
                toss_winner = tossing_team

            # Toss-winning captain decides batting or bowling
            print(f"\n{toss_winner.name} won the toss! What would you like to do?")
            print("1. Bat first")
            print("2. Bowl first")

            decision = validate_input("Enter choice (1 or 2): ", int, 1, 2)

            if decision == 1:
                batting_team = toss_winner
                bowling_team = self.team1 if toss_winner == self.team2 else self.team2
                print(f"\n{toss_winner.name} elects to bat first!")
            else:
                batting_team = self.team1 if toss_winner == self.team2 else self.team2
                bowling_team = toss_winner
                print(f"\n{toss_winner.name} elects to bowl first! {batting_team.name} will bat first.")

            return batting_team  # Return the batting team

        except Exception as e:
            print(f"Error during toss: {e}")
            return None

    # function to play innings
    def play_innings(self, batting, bowling):
        try:
            batting_team = batting
            bowling_team = bowling
            striker, non_striker = batting_team.select_openers()
            previous_bowler = None

            for over_number in range(self.overs):
                if batting_team.wickets == len(batting_team.players) - 1:  # All players out
                    print(f'Innings Over! {batting_team.name} is all out')
                    break

                if self.target_score is not None and batting_team.score > bowling_team.score:
                    print(f'{batting_team.name} chased the target!')
                    return

                print(f'\nOver Number {over_number}')
                bowler = bowling_team.select_bowler(previous_bowler)
                previous_bowler = bowler

                over = Over(
                    bowler=bowler, striker=striker, non_striker=non_striker,
                    batting_team=batting_team, bowling_team=bowling_team,
                    over_number=over_number, target_score=self.target_score
                )

                over.play_over()
                batting_team.overs_played += 1
                batting_team.display_detailed_scoreboard()
                
        except Exception as e:
            print(f'Error in play innings function: {e}')


    def display_results(self):
        try:
            print("\n--- Match Results ---")
            
            if self.batting_team.score >= self.target_score:
                self.winner = self.batting_team
                print(f'{self.winner.name} won the match by {len(self.winner.players) - 1 - self.batting_team.wickets} wickets!')
            
            elif self.batting_team.wickets == len(self.batting_team.players) - 1:
                self.winner = self.bowling_team
                print(f'{self.winner.name} won the match by {self.target_score - self.batting_team.score} runs!')

            else:
                self.winner = self.bowling_team
                print(f'{self.winner.name} won the match by {self.target_score - self.batting_team.score} runs!')
            
            
        except Exception as e:
            print(f'Error in displaying results: {e}')


    def man_of_match(self):
        pass

    def highest_wicket_taker(self):
        pass
