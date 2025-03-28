from player import Player
from utils import validate_input

class Team:
    def __init__(self, name, num_players):
        self.name = name
        self.players = {}
        self.score = 0
        self.wickets = 0
        self.overs_played = 0
        self.players_who_batted = []
        self.num_players = num_players  

    def add_player(self):
        try:
            for player in range(self.num_players):
                player_name = validate_input(f"Enter name for player {player+1}: ", str)
                print("\nSelect role")
                print("1.Batsman")
                print("2.Bowler")
                print("3.WicketKeeper")
                print("4.Captain")

                role_choice = validate_input("Enter role number: ", int, 1, 4, (1,2,3, 4))
                role_dict = {1: "Batsman", 2: "Bowler", 3: 'WicketKeeper', 4:'Captain'}
                role = role_dict.get(role_choice)

                player = Player(player_name, role)
                self.players[player_name] = player

        except Exception as e:
            print(f'Error while adding players: {e}')


    # function to return list of batsmen who are not out and openers 
    def get_available_batsmen(self):
        try:
            result = []
            for player in self.players.keys():
                if player not in self.players_who_batted:
                    result.append(player)

            return result

        except Exception as e:
            print(f'Error in get available function')

    def get_available_bowlers(self):
        pass

    # function to select openers
    def select_openers(self):
        try:
            print(f"\nSelect opening batsmen for {self.name}:")
            print()
            # Display all players in the team
            for player in self.players:
                print(player)

            # Take input for opener
            while True:
                striker_name = validate_input("Enter the Striker Name: ", str)
                if striker_name not in self.players:
                    continue
                self.striker = self.players[striker_name]
                self.players_who_batted.append(self.striker.name)
                break

            # Take inpur for Non Striker
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

    def select_next_batsman(self):
        pass

    # the issue is that previous_bowler can bowl consecurtive overs
    def select_bowler(self, previous_bowler):
        try: 
            print()
            print(f'Select bowler from following {self.name} team')

            # self.players

            for player_id in self.players:
                player = self.players[player_id]

                player_info = f'{player_id}: {player.role}, Overs Bowled: {player.overs_bowled}'

                # check if the bowler has bowled previous over or not
                # if previous_bowler is not None and previous_bowler == player:
                #     player_info  += f'{player} bowled previous over'

                # print all bowlers info
                print(player_info)
                
            while True:
                try:
                    print()
                    selected_bowler_name = validate_input("Enter the bowler ", str)
                    
                    selected_bowler = self.players[selected_bowler_name]

                    # print(selected_bowler)

                    if previous_bowler is not None and selected_bowler == previous_bowler:
                            print(f"\n{selected_bowler.name} has bowled the previous over. Cannot bowl consecutive overs")
                            continue
                        
                    elif selected_bowler != previous_bowler:
                        selected_bowler.set_overs_bowled()
                        # print(f'{selected_bowler} is the selected bowler')
                        return selected_bowler
                
                except Exception as e:
                    print(f'Error: {e}')

        except Exception as e:
            print(f'Error in selecting bowler function: {e} ')
    
    def update_score(self, runs):
        self.score += runs

    def increment_wickets(self):
        self.wickets += 1

    def display_ball_scoreboard(self, bowler, striker, non_striker, over_number, ball_number):
        print("\n" + "-" * 60)
        print(f"||  Over {over_number}.{ball_number}  ||  {self.name}  ||  {self.score}/{self.wickets}  ||")
        print("-" * 60)
        print(f"||  Batting: {self.name}  ||  Bowling: {bowler.name} ||")
        print(f"||  Striker: {striker.name} ({striker.runs} runs, {striker.balls_faced} balls, SR: {striker.strike_rate:.2f})  ||  Non-Striker: {non_striker.name} ({non_striker.runs} runs, {non_striker.balls_faced} balls)  ||")
        print(f"||  Bowler: {bowler.name} ({bowler.overs_bowled} overs, {bowler.wickets_taken} wickets, Economy: {bowler.economy:.2f})  ||")
        print("-" * 60)


    def display_detailed_scoreboard(self):
        print("\n" + "=" * 80)
        print(f"||  {self.name} - Scorecard  ||  Total: {self.score}/{self.wickets}  ||  Overs: {self.overs_played}  ||")
        print("=" * 80)
        print("||  Player Name      ||  Runs  ||  Balls  ||  Fours  ||  Sixes  ||  SR  ||")
        print("=" * 80)

        for player in self.players.values():
            if player.balls_faced > 0:  # Show only players who have batted
                print(f"||  {player.name:15} ||  {player.runs:5}  ||  {player.balls_faced:5}  ||  {player.fours:5}  ||  {player.sixes:5}  ||  {player.strike_rate:.2f}  ||")

       
        # print("||  Bowler Name      ||  Overs  ||  Wickets  ||  Runs  ||  Econ  ||")
        # print("=" * 60)

        # for player in self.players.values():

        #     print(f"||  {player.name:15} ||  {player.overs_bowled:5}  ||  {player.wickets_taken:5}  ||  {player.runs_conceded:5}  ||  {player.economy:.2f}  ||")
        #     print("=" * 80)

    def __str__(self):
        player_info = "\n".join([str(player) for player in self.players.values()])
        return f"Team: {self.name}\nPlayers: \n{player_info}"
