import requests
import json
from pprint import pprint
import pandas as pd

# This application fetches data from the Blue Alliance API
# https://www.thebluealliance.com/apidocs/v3

class fetch_info():
    def __init__(self):
        self.tba_key = self.read_key()

    """ Self Explanatory """
    def ret_tba_key(self):
        return self.tba_key

    """Reads API key from file key.txt"""
    def read_key(self):
        with open("key.txt", "r") as f:
            return f.read()

    def fetch_info_for_event(self, event_id):
        req = requests.get(f"https://www.thebluealliance.com/api/v3/event/{event_id}/teams/statuses", headers={"X-TBA-Auth-Key": self.tba_key})
        with open("event_info.json", "w") as f:
            f.write(req.text)
        

    """
    Returns JSON data for the teams at a given competition based of off the event ID
    that is in the link to the event, ex:
    https://www.thebluealliance.com/event/2022mibb -> Event ID: 2022mibb
    """

    def get_teams_at_comp(self, event_key):
        req = requests.get(f"https://www.thebluealliance.com/api/v3/event/{event_key}/teams/simple", headers={"X-TBA-Auth-Key": self.tba_key})
        return req.json()

    def get_info_of_teams(self, team_nums):
        for team_num in team_nums:

            req = requests.get(f"https://www.thebluealliance.com/api/v3/teams/frc{team_num}", headers={"X-TBA-Auth-Key": self.tba_key})
            return req.json()

    def data_save(self, data):
        with open("./data/data.json", "w") as f:
            f.write(data)
            return
    
    

def team_list_to_csv():
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


    print(team_keys)

    # Init pandas dataframe with column 1 being team names and column 2 being team numbers
    df = pd.DataFrame({'Team Name': team_nicks, 'Team Number': team_nums}, columns = ['Team Name', 'Team Number'])
    print(df)

    # Export to csv so you can import to a spreadsheet
    df.to_csv(f'{event}-teams.csv', index=False)

if __name__ == "__main__":
#     info_grab = fetch_info()
#     tba_key = info_grab.ret_tba_key()
# 
#     team_key = "frc862" 
#     event_key = "2022mibb"
#     info = requests.get(f"https://www.thebluealliance.com/api/v3/event/{event_key}/oprs", headers={"X-TBA-Auth-Key": tba_key})
#     pprint(info.json())
    info = fetch_info()
    info.fetch_info_for_event("2022mibb")