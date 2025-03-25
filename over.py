from utils import validate_input

class Over:
    def __init__(self, bowler, striker, non_striker, batting_team, bowling_team, over_number):
        self.bowler = bowler
        self.striker = striker
        self.non_striker = non_striker
        self.batting_team = batting_team
        self.bowling_team = bowling_team
        self.balls_bowled = 0
        self.over_number = over_number

    def play_over(self):
        legal_balls = 0
        print(f"\n*** {self.bowler.name} is bowling ***")

        while legal_balls < 6:
            print(f"\n Over {self.over_number} Ball {legal_balls + 1}: Striker: {self.striker.name} | Non-Striker: {self.non_striker.name} | Bowler: {self.bowler.name} |")
            # using normal input of validate input because of special case
            ball_input = input("Enter runs scored (or 'W' for Wicket, 'WD' for Wide, 'NB' for No ball): ").strip()

            if ball_input.upper() == 'WD':
                print("Wide ball! +1 run.")
                self.batting_team.update_score(1)
                self.bowler.bowl(1)
                continue

            elif ball_input.upper() == 'NB':
                print("No ball! +1 run.")
                self.batting_team.update_score(1)
                self.bowler.bowl(1)
                continue

            elif ball_input.upper() == 'W':
                print(f"{self.striker.name} is OUT!")
                self.striker.is_out = True
                self.batting_team.increment_wickets()
                self.bowler.wicket()
                
                # gets all the batsmen who are not out
                next_batsman = self.batting_team.get_available_batsmen()
 
                if len(next_batsman) == 0:
                    return 
                
                print()
                print("Following are the available batsman")
                for available_batsman in next_batsman:
                    print(available_batsman)
                
                self.all_players = self.batting_team.players

                print()
                next_batsman_name = validate_input("Enter batsman from above players: ", str)

                # getting batsman object from the dictionary using name(key)
                next_batsman = self.all_players[next_batsman_name]
                # setting the striker to new batsman object
                self.striker = next_batsman

                # appending the new striker to the list who have batted
                self.batting_team.players_who_batted.append(next_batsman_name)

                # increasing the balls
                legal_balls += 1

            else:
                try:
                    runs = int(ball_input)
                    self.striker.bat(runs)
                    self.batting_team.update_score(runs)
                    self.bowler.bowl(runs)

                    print()
                    print("Runs scored till now")
                    print(f'{self.striker.name}:{self.striker.runs}')
                    print(f'{self.non_striker.name}:{self.non_striker.runs}')

                    if runs % 2 == 1:
                        # Odd run: rotate strike
                        print("strike change")
                        self.swap_strikers()

                    legal_balls += 1
                
                except Exception as e:
                    print(f'Issue while playing over. The issue is {e}')

        
        print("strike change")
        self.swap_strikers()

    def swap_strikers(self):
        self.striker, self.non_striker = self.non_striker, self.striker
