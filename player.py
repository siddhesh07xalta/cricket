class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.runs = 0
        self.wickets_taken = 0
        self.balls_faced = 0
        self.is_out = False
        self.overs_bowled = 0
        self.runs_conceded = 0
        self.sixes = 0
        self.fours = 0

    @property
    def strike_rate(self):
        return (self.runs / self.balls_faced) * 100 if self.balls_faced else 0

    @property
    def economy(self):
        return (self.runs_conceded / self.overs_bowled) if self.overs_bowled else 0

    def bat(self, runs_scored):
        self.runs += runs_scored
        self.balls_faced += 1
        if runs_scored == 4:
            self.fours += 1
        elif runs_scored == 6:
            self.sixes += 1

    def bowl(self, runs_conceded):
        self.runs_conceded += runs_conceded

    def wicket(self):
        self.wickets_taken += 1

    def set_overs_bowled(self):
        self.overs_bowled += 1

    def __str__(self):
        return (f'{self.name} - {self.role} | Runs: {self.runs}, Balls Faced: {self.balls_faced}, '
                f'Wickets: {self.wickets_taken}, SR: {self.strike_rate:.2f}, Economy: {self.economy:.2f}')
