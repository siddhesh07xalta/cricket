from copy import deepcopy
from utils import validate_ball_outcome, validate_player_selection
from player import Player
from team import Team

class SuperOver:
    def __init__(self, team1, team2):
        self.original_team1 = team1
        self.original_team2 = team2

        self.team1 = self.create_super_over_team(team1)
        self.team2 = self.create_super_over_team(team2)

    def create_super_over_team(self, original_team):
        team = Team(original_team.name, original_team.num_players)
        for player_name, player in original_team.players.items():
            # Create a fresh player object with same name and role but reset stats
            new_player = Player(player.name, player.role)
            team.players[player.name] = new_player
        return team

    def setup_super_over(self, batting_team, bowling_team):
        print(f"Select 2 batsmen for {batting_team.name}'s Super Over:")
        batting_team.striker = validate_player_selection(batting_team.players, "Enter the Striker Name: ")
        batting_team.players_who_batted.append(batting_team.striker.name)

        batting_team.non_striker = validate_player_selection(
            batting_team.get_available_batsmen(),
            "Enter the Non Striker Name: ",
            players_dict=batting_team.players
        )
        batting_team.players_who_batted.append(batting_team.non_striker.name)

        print(f"Select a bowler for {bowling_team.name}'s Super Over:")
        batting_team.bowler = validate_player_selection(bowling_team.players, "Enter the bowler: ")

    
    def play_super_over(self, team, target=None):
        ball_number = 1
        striker = team.striker
        non_striker = team.non_striker
        bowler = team.bowler

        while ball_number <= 6:
            print(f"\nOver 0.{ball_number}: Striker: {striker.name}, Bowler: {bowler.name}")
            outcome = validate_ball_outcome()

            if outcome == "W":
                print(f"{striker.name} is OUT!")
                team.increment_wickets()
                striker.is_out = True
                break
            elif outcome in ["WD", "NB"]:
                print(f"{outcome} - Extra run!")
                team.update_score(1)
                if target and team.score > target:
                    print(f"{team.name} has chased down the target!")
                    return  # End early
                continue
            else:
                team.update_score(outcome)
                striker.bat(outcome)
                bowler.bowl(outcome)

                if outcome % 2 == 1:
                    striker, non_striker = non_striker, striker

            team.display_ball_scoreboard(bowler, striker, non_striker, 0, ball_number)
            if target and team.score > target:
                print(f"{team.name} has chased down the target!")
                return  # End early

            ball_number += 1

        team.overs_played = 1

    def display_super_over_summary(self, team):
        team.display_detailed_scoreboard()

    def play_and_display_super_overs(self):
        print("\n==============================")
        print("MATCH TIED! SUPER OVER TIME!")
        print("==============================\n")

        # Setup
        self.setup_super_over(self.team1, self.team2)
        self.setup_super_over(self.team2, self.team1)

        # Team 1 innings
        self.play_super_over(self.team1)
        self.display_super_over_summary(self.team1)

        # Team 2 innings with target
        target = self.team1.score
        self.play_super_over(self.team2, target=target)
        self.display_super_over_summary(self.team2)

        # Result
        self.final_decision()


    def final_decision(self):
        if self.team1.score > self.team2.score:
            print(f"{self.team1.name} wins the Super Over! 🎉")
        elif self.team2.score > self.team1.score:
            print(f"{self.team2.name} wins the Super Over! 🎉")
        else:
            team1_boundaries = sum([p.fours + p.sixes for p in self.team1.players.values()])
            team2_boundaries = sum([p.fours + p.sixes for p in self.team2.players.values()])

            print("\n🏏 The Super Over is also a TIE! Comparing boundary count...")

            if team1_boundaries > team2_boundaries:
                print(f"🏆 {self.team1.name} wins by boundary count! (Boundaries: {team1_boundaries})")
            elif team2_boundaries > team1_boundaries:
                print(f"🏆 {self.team2.name} wins by boundary count! (Boundaries: {team2_boundaries})")
            else:
                print("BOUNDARIES ARE ALSO EQUAL, IT'S A TIE!")
