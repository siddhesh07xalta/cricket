from player import Player

class Team:
    def __init__(self, name):
        self.name = name
        self.players = {}
        self.score = 0
        self.wickets_lost = 0
        self.overs_played = 0
        self.sixes = 0
        self.fours = 0


    def add_player(self):
        # player = input(f"Enter player name you wanto to end for team {self.name}: ")
        
        try: 
            for player in range(3):
                player_name = input(f"Enter name for player {player+1}: ").strip()
                print("Select role")
                print("1.Batsman")
                print("2.Bowler")
                print("3.All Rounder")
                print("4.Wicket Keeper")
                print("5.Captain")

                role_choice = input("Enter role number").strip()

                role_dict = {
                    "1":"Batsman",
                    "2":"Bowler",
                    "3":"All Rounder",
                    "4":"Wicket Keeper",
                    "5":"Captain",
                }

                role = role_dict.get(role_choice)

                player = Player(player_name,role)
                
                self.players[player_name] = player

        except Exception as e:
            print(f'Error while taking input for team players, Error is {e}')

    def get_available_bowlers(self):
        pass

    def get_available_batsmen(self):
        pass

    def increment_score(self):
        pass

    def wickets_lost(self):
        pass


   
    def __str__(self):
        player_info = "\n".join([str(player) for player in self.players.values()])
        return f"Team: {self.name}\n Players: \n{player_info}"
    
    # def print_team_members(self):

    #     # for x in self.players:
    #     #     print(x)
    #     #     for y in self.players[x]:
    #     #         print(y, ':', self.players[x][y])
    #     for key, value in self.players():
    #         print(f"Key: {key}, Value: {value}")
    
    