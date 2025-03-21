class Player:
    def __init__(self, name, role):
        self.name  = name
        self.role = role
        self.runs = 0
        self.wickets = 0
        self.balls_faces = 0
        self.overs_bowled = 0
        self.runs_conceded = 0

    def __str__(self):
        return f'{self.name}-{self.role}' 

    