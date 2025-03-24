from player import Player


class Team:
    def __init__(self, name):
        self.name = name
        self.players = {}
        self.score = 0
        self.wickets = 0
        self.overs_played = 0

    def add_player(self):
        try:
            for player in range(3):
                player_name = input(
                    f"Enter name for player {player+1}: ").strip()
                print("Select role")
                print("1.Batsman")
                print("2.Bowler")

                role_choice = input("Enter role number: ").strip()

                role_dict = {
                    "1": "Batsman",
                    "2": "Bowler"
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
            try:
                striker_index = int(
                    input("Select the Striker (enter number): ")) - 1
                if striker_index >= 0 and striker_index <= len(self.players):
                    striker = list(self.players.keys())[striker_index]
                    striker = self.players[striker]
                    break
                else:
                    print("Invalid selection. Please select a valid player number.")
            except ValueError:
                print("Invalid input! Enter a number.")

        while True:
            try:
                non_striker_index = int(
                    input("Select the Non Striker (enter number): ")) - 1
                if non_striker_index >= 0 and non_striker_index <= len(self.players):
                    non_striker = list(self.players.keys())[
                        non_striker_index]
                    non_striker = self.players[non_striker]
                    break
                else:
                    print("Invalid selection. Please select a valid player number.")
            except ValueError:
                print("Invalid input! Enter a number.")

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
                selected_bowler_name = input("Enter the bowler ").strip()
                
                selected_bowler = all_players[selected_bowler_name]

                print(selected_bowler)

                if previous_bowler is not None and selected_bowler == previous_bowler:
                        print(f"\n{selected_bowler.name} has bowled the previous over. Cannot bowl consecutive overs")
                        continue
                    
                elif selected_bowler != previous_bowler:
                    selected_bowler.set_overs_bowled()
                    # print(f'{selected_bowler} is the selected bowler')
                    return selected_bowler
         
                else:
                    print("Invalid player ID, Please select from the available players")
            
            except Exception as e:
                print(e)

    #     # selected_bowler.set_overs_bowled()
    #     # print(f'{selected_bowler_id} is selected')

    #     # return selected_bowler

    
    def update_score(self, runs):
        self.score += runs

    def increment_wickets(self):
        self.wickets += 1

    def display_scoreboard(self):
        print("display scoreboard")

    def __str__(self):
        player_info = "\n".join([str(player)
                                for player in self.players.values()])
        return f"Team: {self.name}\n Players: \n{player_info}"
