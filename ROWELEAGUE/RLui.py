from RLleague import League

# Displays a list of the teams in the league to the user and prompts them to choose one, will provide an error if an invalid name or id is entered and prompts the user to try again until a valid team is selected.
def display_teams(league):
    league.teams.sort(key=lambda t: t.team_id)
    print(f"{'Team ID':<10} {'Team Name':<20} {'Conference':<10}")
    print("-" * 60)
    for team in league.teams:
        print(f"{team.team_id:<10} {team.team_name:<20} {team.conference:<10}")
    while True:
        team_choice = input("\nEnter a Team ID or Name to choose it: ")
        for team in league.teams:
            if team.team_name == team_choice or team.team_id == team_choice:
                league.get_team_roster(team_choice)
                league.user_team = team
                break
        if True:
            print(f"\nYou have selected the {league.user_team.team_name}!")
            break
        else:
            print(f"Invalid choice. Please enter a valid Team ID or Name.")