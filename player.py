class Player:
    def __init__(self, name, role):
        self.name  = name
        self.role = role
        self.runs = 0
        self.wickets_taken = 0
        self.balls_faced = 0
        self.is_out = False
        self.overs_bowled = 0
        self.runs_conceded = 0
        self.sixes = 0
        self.fours = 0
        self.strike_rate = 0
        self.economy = 0

    def bat(self, runs_scored):
        self.runs += runs_scored
        self.balls_faced += 1

    def bowl(self, runs_conceded):
        self.runs_conceded += runs_conceded

    def wicket(self):
        self.wickets_taken += 1
        pass
    
    def __str__(self):
        return f'{self.name}-{self.role} Runs: {self.runs}, Balls Faced: {self.balls_faced}, Wickets Taken: {self.wickets_taken} ' 



    