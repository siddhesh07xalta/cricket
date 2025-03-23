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
                player_name = input(f"Enter name for player {player+1}: ").strip()
                print("Select role")
                print("1.Batsman")
                print("2.Bowler")

                role_choice = input("Enter role number: ").strip()

                role_dict = {
                    "1":"Batsman",
                    "2":"Bowler"
                }

                role = role_dict.get(role_choice)

                player = Player(player_name,role)
                
                self.players[player_name] = player

        except Exception as e:
            print(f'Error while taking input for team players, Error is {e}')


    def get_available_batsmen(self, exclude=[]):
        pass
    
    def get_available_bowlers(self):
        pass


    def select_openers(self):
        print(f"\nSelect opening batsmen for {self.name}:")
        
        # Display all players in the team with their index
        index = 1
        for player in self.players:
            print(player, index)
            index+=1

        # Take input for opener
        while True:
            try:
                striker_index = int(input("Select the Striker (enter number): ")) - 1
                if striker_index > 0 and striker_index <= len(self.players):
                    striker = list(self.players.keys())[striker_index - 1]
                    striker = self.players[striker]
                    break
                else:
                    print("Invalid selection. Please select a valid player number.")
            except ValueError:
                print("Invalid input! Enter a number.")

        while True:
            try:
                non_striker_index = int(input("Select the Non Striker (enter number): ")) - 1
                if non_striker_index > 0 and non_striker_index <= len(self.players):
                    non_striker = list(self.players.keys())[non_striker_index - 1]
                    non_striker = self.players[non_striker]
                    break
                else:
                    print("Invalid selection. Please select a valid player number.")
            except ValueError:
                print("Invalid input! Enter a number.")

        print(f"\nOpening pair for {self.name}: {striker.name} (Striker), {non_striker.name} (Non-Striker)")

        return striker, non_striker
    

    def select_next_batsman(self, striker, non_striker):
        pass
    
    def select_bowler(self, previous_bowler):
        pass

    def update_score(self, runs):
        self.score += runs

    def increment_wickets(self):
        self.wickets += 1

    def display_scoreboard(self):
        print("display scoreboard")

    def __str__(self):
        player_info = "\n".join([str(player) for player in self.players.values()])
        return f"Team: {self.name}\n Players: \n{player_info}"