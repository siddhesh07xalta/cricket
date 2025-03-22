class Team:
    def __init__(self, name, team_members):
        self.name = name
        self.players = team_members
        self.score = 0
        self.wickets_lost = 0
        self.overs_played = 0
        self.sixes = 0
        self.fours = 0


    def add_player(self):
        pass

    def get_available_bowlers(self):
        pass

    def get_available_batsmen(self):
        pass

    def increment_score(self):
        pass

    def wickets_lost(self):
        pass

    
    # def __str__(self):
    #     player_info = "\n".join([str(player) for player in self.players.values()])
    #     return f"Team: {self.name}\n Players: \n{player_info}"
    
    # def print_team_members(self):

    #     # for x in self.players:
    #     #     print(x)
    #     #     for y in self.players[x]:
    #     #         print(y, ':', self.players[x][y])
    #     for key, value in self.players():
    #         print(f"Key: {key}, Value: {value}")
    
    