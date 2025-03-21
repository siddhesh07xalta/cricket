class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.score = 0
        self.wickets_lost = 0
        self.overs_played = 0

    def __str__(self):
        return f'Team Name: {self.name}, Team Players: {self.players}, Team Score: {self.score}, Team Wickets Lost: {self.wickets_lost}, Overs Played {self.overs_played}'

