class Over:
    def __init__(self, bowler, striker, non_striker, batting_team, bowling_team, game):
        self.bowler = bowler
        self.striker = striker
        self.non_striker = non_striker
        self.batting_team = batting_team
        self.bowling_team = bowling_team
        self.game = game
        self.balls_bowled = 0

    # def play_over(self):
    #     legal_balls = 0
    #     print(f"\n*** {self.bowler.name} is bowling ***")
        
    #     while legal_balls < 6:
    #         print(f"\nBall {legal_balls + 1}: Bowler: {self.bowler.name} | Striker: {self.striker.name}")
    #         ball_input = input("Enter runs scored (or 'W' for Wicket, 'WD' for Wide, 'NB' for No ball): ").strip().upper()

    #         if ball_input.lower() == 'WD':
    #             print("Wide ball! +1 run.")
    #             self.batting_team.update_score(1)
    #             self.bowler.bowl(1)
    #             continue

    #         elif ball_input.lower() == 'NB':
    #             print("No ball! +1 run.")
    #             self.batting_team.update_score(1)
    #             self.bowler.bowl(1)
    #             continue

    #         elif ball_input.lower() == 'W':
    #             print(f"{self.striker.name} is OUT!")
    #             self.striker.is_out = True
    #             self.batting_team.increment_wickets()
    #             self.bowler.add_wicket()

    #             # Select next batsman
    #             next_batsman = self.batting_team.select_next_batsman(self.striker, self.non_striker)
    #             if not next_batsman:
    #                 print("All batsmen are out! End of innings.")
    #                 break
    #             self.striker = next_batsman
    #             legal_balls += 1

    #         else:
    #             try:
    #                 runs = int(ball_input)
    #                 self.striker.bat(runs)
    #                 self.batting_team.update_score(runs)
    #                 self.bowler.bowl(runs)

    #                 if runs % 2 == 1:
    #                     # Odd run: rotate strike 
    #                     self.swap_strikers()

    #                 legal_balls += 1

    #             except ValueError:
    #                 print("Invalid input! Enter a number, W, Wd, or Nb.")

    #     # After the over ends, swap striker/non-striker again
    #     self.bowler.increment_overs()
    #     self.swap_strikers()

    # def swap_strikers(self):
    #     self.striker, self.non_striker = self.non_striker, self.striker