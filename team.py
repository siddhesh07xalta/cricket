from player import Player
from utils import validate_input

class Team:
    def __init__(self, name, num_players):
        self.name = name  # Team name
        self.players = {}  # Dictionary to hold players in the team
        self.score = 0  # Total score of the team
        self.wickets = 0  # Number of wickets lost by the team
        self.overs_played = 0  # Number of overs played by the team
        self.players_who_batted = []  # List of players who have batted
        self.num_players = num_players  # Number of players in the team  

    def add_player(self):
        try:
            captains_count = 0  # To ensure only one captain is added

            for player in range(self.num_players):
                player_name = validate_input(f"Enter name for player {player+1}: ", str)
                
                # Role selection process
                print("\nSelect role")
                print("1. Batsman")
                print("2. Bowler")
                print("3. Captain")

                # Loop until a valid role is selected
                while True:
                    role_choice = validate_input("Enter role number: ", int, 1, 3, (1, 2, 3))
                    role_dict = {1: "Batsman", 2: "Bowler", 3: "Captain"}
                    role = role_dict.get(role_choice)

                    # If role is Captain, check if there's already a captain
                    if role == "Captain":
                        captains_count += 1
                        if captains_count > 1:
                            print("Error: A team can only have one captain. Please choose a different role.")
                            continue  # Ask for role again if more than one captain is selected

                    # Create a new player and add to the team
                    player = Player(player_name, role)
                    self.players[player_name] = player
                    break  # Exit loop once a valid role is assigned

        except Exception as e:
            print(f'Error while adding players: {e}')


    # Function to return list of batsmen who are not out and openers
    def get_available_batsmen(self):
        try:
            result = []
            for player in self.players.keys():
                if player not in self.players_who_batted:
                    result.append(player)
            return result

        except Exception as e:
            print(f'Error in get available batsmen function: {e}')

    # Function to select openers for the team
    def select_openers(self):
        try:
            print(f"\nSelect opening batsmen for {self.name}:")
            # Display all players in the team
            for player in self.players:
                print(player)

            # Take input for opener (striker)
            while True:
                striker_name = validate_input("Enter the Striker Name: ", str)
                if striker_name not in self.players:
                    continue
                self.striker = self.players[striker_name]
                self.players_who_batted.append(self.striker.name)
                break

            # Take input for non-striker
            while True:
                non_striker_name = validate_input("Enter the Non Striker Name: ", str)
                if non_striker_name not in self.players:
                    continue
                self.non_striker = self.players[non_striker_name]
                self.players_who_batted.append(self.non_striker.name)
                break

            print(f"\nOpening pair for {self.name}: {self.striker.name} (Striker), {self.non_striker.name} (Non-Striker)")

            return self.striker, self.non_striker
        
        except Exception as e:
            print(f'Error in selecting openers: {e}')

    # Function to select a bowler from the available bowlers in the team
    def select_bowler(self, previous_bowler):
        try: 
            print(f'\nSelect bowler from following {self.name} team:')
            # Display all players and their bowling details
            for player_id in self.players:
                player = self.players[player_id]
                player_info = f'{player_id}: {player.role}, Overs Bowled: {player.overs_bowled}'
                print(player_info)
                
            while True:
                try:
                    selected_bowler_name = validate_input("Enter the bowler: ", str)
                    selected_bowler = self.players[selected_bowler_name]

                    # Check if the selected bowler is the same as the previous bowler
                    if previous_bowler is not None and selected_bowler == previous_bowler:
                        print(f"\n{selected_bowler.name} has bowled the previous over. Cannot bowl consecutive overs.")
                        continue
                    
                    # If the selected bowler is valid, set the overs bowled and return the bowler
                    selected_bowler.set_overs_bowled()
                    return selected_bowler

                except Exception as e:
                    print(f'Error: {e}')

        except Exception as e:
            print(f'Error in selecting bowler function: {e}')
    
    # Function to update team score
    def update_score(self, runs):
        self.score += runs

    # Function to increment the number of wickets
    def increment_wickets(self):
        self.wickets += 1

    # Function to display scoreboard for each ball in the over
    def display_ball_scoreboard(self, bowler, striker, non_striker, over_number, ball_number):
        print("\n" + "-" * 60)
        print(f"||  Over {over_number}.{ball_number}  ||  {self.name}  ||  {self.score}/{self.wickets}  ||")
        print("-" * 60)
        print(f"||  Batting: {self.name}  ||  Bowling: {bowler.name} ||")
        print(f"||  Striker: {striker.name} ({striker.runs} runs, {striker.balls_faced} balls, SR: {striker.strike_rate:.2f})  ||  Non-Striker: {non_striker.name} ({non_striker.runs} runs, {non_striker.balls_faced} balls)  ||")
        print(f"||  Bowler: {bowler.name} ({bowler.overs_bowled} overs, {bowler.wickets_taken} wickets, Economy: {bowler.economy:.2f})  ||")
        print("-" * 60)

    # Function to display detailed scoreboard
    def display_detailed_scoreboard(self):
        print("\n" + "=" * 80)
        print(f"||  {self.name} - Scorecard  ||  Total: {self.score}/{self.wickets}  ||  Overs: {self.overs_played}  ||")
        print("=" * 80)
        print("||  Player Name      ||  Runs  ||  Balls  ||  Fours  ||  Sixes  ||  SR  ||")
        print("=" * 80)

        for player in self.players.values():
            if player.balls_faced > 0:  # Show only players who have batted
                print(f"||  {player.name:15} ||  {player.runs:5}  ||  {player.balls_faced:5}  ||  {player.fours:5}  ||  {player.sixes:5}  ||  {player.strike_rate:.2f}  ||")

    # Function to return a string representation of the team
    def __str__(self):
        player_info = "\n".join([str(player) for player in self.players.values()])
        return f"Team: {self.name}\nPlayers: \n{player_info}"
