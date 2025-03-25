from player import Player
from utils import validate_input

class Team:
    def __init__(self, name):
        self.name = name
        self.players = {}
        self.score = 0
        self.wickets = 0
        self.overs_played = 0

    def add_player(self):
        try:
            players = 11
            for player in range(3):
                player_name = validate_input(f"Enter name for player {player+1}: ", str)
                
                print("Select role")
                print("1.Batsman")
                print("2.Bowler")

                role_choice = validate_input("Enter role number: ", int, 1,2,(1,2))

                role_dict = {
                    1: "Batsman",
                    2: "Bowler"
                }

                role = role_dict.get(role_choice)

                player = Player(player_name, role)

                self.players[player_name] = player

        except Exception as e:
            print(f'Error while taking input for team players, Error is {e}')

    def get_available_batsmen(self, exclude=[]):
        pass

    def get_available_bowlers(self):
        pass

    def select_openers(self):
        print(f"\nSelect opening batsmen for {self.name}:")

        # Display all players in the team
        for player in self.players:
            print(player)

        # Take input for opener
        while True:
            striker_name = validate_input("Enter the Striker Name: ", str)
            striker = self.players[striker_name]
            break

        # Take inpur for Non Striker
        while True:
            non_striker_name = validate_input("Enter the Non Striker Name: ", str)
            non_striker = self.players[non_striker_name]
            break
            

        print(
            f"\nOpening pair for {self.name}: {striker.name} (Striker), {non_striker.name} (Non-Striker)")

        return striker, non_striker

    def select_next_batsman(self):
        pass

    # the issue is that previous_bowler can bowl consecurtive overs
    def select_bowler(self, previous_bowler):
        print(f'Select bolwer from following for {self.name} team')

        all_players = self.players

        for player_id in all_players:
            player = all_players[player_id]

            player_info = f'{player_id}: {player.role}, Overs Bowled: {player.overs_bowled}'

            # check if the bowler has bowled previous over or not
            # if previous_bowler is not None and previous_bowler == player:
            #     player_info  += f'{player} bowled previous over'

            # print all bowlers info
            print(player_info)
            
        while True:
            try:
                selected_bowler_name = validate_input("Enter the bowler ", str)
                
                selected_bowler = all_players[selected_bowler_name]

                # print(selected_bowler)

                if previous_bowler is not None and selected_bowler == previous_bowler:
                        print(f"\n{selected_bowler.name} has bowled the previous over. Cannot bowl consecutive overs")
                        continue
                    
                elif selected_bowler != previous_bowler:
                    selected_bowler.set_overs_bowled()
                    # print(f'{selected_bowler} is the selected bowler')
                    return selected_bowler
            
            except Exception as e:
                print(f'Error in selecting bowler: {e}')

    
    def update_score(self, runs):
        self.score += runs

    def increment_wickets(self):
        self.wickets += 1

    def display_scoreboard(self):
        print("display scoreboard")

    def __str__(self):
        player_info = "\n".join([str(player) for player in self.players.values()])
        return f"Team: {self.name}\n Players: \n{player_info}"
