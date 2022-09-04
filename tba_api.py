import requests
import json
from pprint import pprint
import pandas as pd

# This application fetches data from the Blue Alliance API
# https://www.thebluealliance.com/apidocs/v3

class fetch_info():
    def __init__(self):
        self.tba_key = self.read_key()

    """Reads API key from file key.txt"""
    def read_key(self):
        with open("key.txt", "r") as f:
            return f.read()

    """
    Returns JSON data for the teams at a given competition based of off the event ID
    that is in the link to the event, ex:
    https://www.thebluealliance.com/event/2022mibb -> Event ID: 2022mibb
    """

    def get_teams_at_comp(self, event_key):
        req = requests.get(f"https://www.thebluealliance.com/api/v3/event/{event_key}/teams/simple", headers={"X-TBA-Auth-Key": self.tba_key})
        return req.json()

if __name__ == "__main__":
    # Init class
    info_grab = fetch_info()

    # TODO: Eventually make event ID a command line argument
    event = "2022mibb"
    team_nicks = []
    team_nums = []

    teams = info_grab.get_teams_at_comp(event)
    # TODO: Find a way to do this without a for loop
    for team in teams:
        team_nicks.append(team["nickname"])
        team_nums.append(team["team_number"])


    print(team_nicks)

# Init pandas dataframe with column 1 being team names and column 2 being team numbers
df = pd.DataFrame({'Team Name': team_nicks, 'Team Number': team_nums}, columns = ['Team Name', 'Team Number'])
print(df)

# Export to csv so you can import to a spreadsheet
df.to_csv(f'{event}-teams.csv', index=False)