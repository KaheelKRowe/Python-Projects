import random

from RLplayer import Player
from RLdata import player_first, player_last, position, conferences
from RLteam import Team

class League:
    def __init__(self):
        self.teams = []
        self.free_agents = []
        self.all_players = []
        self.generate_teams()
        self.generate_players()
        self.distribute_players()
        self.user_team = None
        self.season = 1
    
    # Takes a list of team names and creates Team objects aswell as adding teams to their respective conferences
    def generate_teams(self):
        for conference, teams in conferences.items():
            for team_name in teams:
                team = Team(team_name, conference)
                self.teams.append(team)
    
    # Creates a list of Player objects and adds them to the free agents pool and all players list
    def generate_players(self, num_players=400):
        for _ in range(num_players):
            player = Player(player_first, player_last, position)
            self.free_agents.append(player)
            self.all_players.append(player)

    # Distributes players to teams based on their contract value, with higher value players being distributed first to create a more balanced league. If a team cannot afford a player or has no roster spots, the player is returned to the free agents pool.
    def distribute_players(self):
        self.free_agents.sort(key=lambda p: p.salary, reverse=True)
        random.shuffle(self.teams)

        for i in range(12):
            for team in self.teams:
                if self.free_agents:
                    player = self.free_agents.pop(0)
                    if not team.add_player(player):
                        self.free_agents.append(player)

    # Display the roster of a team based on user input, allowing them to select a team by either name or ID. If the team is found, their roster is displayed along with payroll and cap space information. If not found, an error message is shown.
    def get_team_roster(self, team_name):
        for team in self.teams:
            if team.team_name == team_name or team.team_id == team_name:
                print(f"\n{team.team_id} | {team.team_name} | {team.conference} | Payroll: ${team.payroll:,} | Cap Space: ${team.available_salary():,}")
                print("-" * 60)
                for player in team.roster:
                    print(f"{player.player_id} | {player.player_first} {player.player_last} | {player.position} | Age: {player.age} | OVR: {player.overall} | Pot: {player.get_potential_grade()} | Salary: ${player.salary:,} | Years: {player.contract_years}")
                return
        print(f"Team '{team_name}' not found.")