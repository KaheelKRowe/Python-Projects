from RLdata import player_first, player_last, team_name, conferences, position
from RLplayer import Player

class Team:
    id_counter = 0
    def __init__(self, team_name, conference):
        Team.id_counter += 1
        self.team_id = f"T{Team.id_counter:03d}"
        self.team_name = team_name
        self.conference = conference
        self.roster = []
        self.salary_cap = 140_000_000
        self.payroll = 0
    
    # add player to team if roster spots and salary cap allow
    def add_player(self, player):
        if len(self.roster) < 12 and self.payroll + player.salary <= self.salary_cap:
            self.roster.append(player)
            self.payroll += player.salary
            return True
        return False
    
    # remove player from team and adjust payroll
    def remove_player(self, player_id):
        for player in self.roster:
            if player.player_id == player_id:
                self.roster.remove(player)
                self.payroll -= player.salary
                return True
        return False
    
    # calculate available salary
    def available_salary(self):
        return self.salary_cap - self.payroll