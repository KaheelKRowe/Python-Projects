from RLleague import League
from RLui import display_teams

league = League()

display_teams(league)

print(f"\nFree Agents: {len(league.free_agents)}")

