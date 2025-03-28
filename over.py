from utils import validate_input

class Over:
    def __init__(self, bowler, striker, non_striker, batting_team, bowling_team, over_number, target_score):
        self.bowler = bowler
        self.striker = striker
        self.non_striker = non_striker
        self.batting_team = batting_team
        self.bowling_team = bowling_team
        self.balls_bowled = 0
        self.over_number = over_number
        self.target_score = target_score
        

    def play_over(self):
        try:
            legal_balls = 0
            print(f"\n*** {self.bowler.name} is bowling ***")

            while legal_balls < 6:

                if self.target_score is not None and self.batting_team.score > self.bowling_team.score:
                    print(f'{self.batting_team.name} chased the target!')
                    return
                    
                print(f"\nOver {self.over_number} Ball {legal_balls + 1}: Striker: {self.striker.name} | Non-Striker: {self.non_striker.name} | Bowler: {self.bowler.name}")
                
                ball_input = input("Enter runs scored (or 'W' for Wicket, 'WD' for Wide, 'NB' for No ball): ").strip()

                if ball_input.upper() == 'WD':
                    print("Wide ball! +1 run.")
                    self.batting_team.update_score(1)
                    self.bowler.bowl(1)
                    self.batting_team.display_ball_scoreboard(self.bowler, self.striker, self.non_striker, self.over_number, legal_balls)
                    continue

                elif ball_input.upper() == 'NB':
                    print("No ball! +1 run.")
                    self.batting_team.update_score(1)
                    self.bowler.bowl(1)
                    self.batting_team.display_ball_scoreboard(self.bowler, self.striker, self.non_striker, self.over_number, legal_balls)
                    continue

                elif ball_input.upper() == 'W':
                    print(f"{self.striker.name} is OUT!")
                    self.striker.is_out = True
                    self.batting_team.increment_wickets()
                    self.bowler.wicket()

                    next_batsman = self.batting_team.get_available_batsmen()
        
                    if len(next_batsman) == 0:
                        return 
                        
                    print("\nAvailable batsmen:")
                    for available_batsman in next_batsman:
                        print(available_batsman)
                        
                    next_batsman_name = validate_input("Enter batsman from above players: ", str)
                    next_batsman = self.batting_team.players[next_batsman_name]
                    self.striker = next_batsman
                    self.batting_team.players_who_batted.append(next_batsman_name)
                    legal_balls += 1

                else:
                    try:
                        runs = int(ball_input)
                        self.striker.bat(runs)
                        self.batting_team.update_score(runs)
                        self.bowler.bowl(runs)

                        if runs == 4:
                            self.striker.fours += 1
                        elif runs == 6:
                            self.striker.sixes += 1

                        if runs % 2 == 1:
                            self.swap_strikers()

                        legal_balls += 1
                    
                    except Exception as e:
                        print(f'Issue while selecting option. The issue is {e}')
                
                # **Show scoreboard after every ball**
                self.batting_team.display_ball_scoreboard(self.bowler, self.striker, self.non_striker, self.over_number, legal_balls)

            self.swap_strikers()

        except Exception as e:
            print(f'Issue while playing over: {e}')


    def swap_strikers(self):
        self.striker, self.non_striker = self.non_striker, self.striker
