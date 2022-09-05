import requests
import json
import pathlib
from pprint import pprint


class Sandstone():
    def __init__(self):
        self.tba_key = self.get_tba_key()
        self.year = 2022


    """
    Gets api key from file key.txt 
    """
    def get_tba_key(self):
        with open("key.txt", "r") as f:
            return f.read()
    
    """
    Loads file from path and returns it as a json object. 
    """
    def load_data(self, file: str):
        
        with open(file, "r") as f:
            return json.load(f)

    """
    Saves json data from text as a json file
    """    
    def save_data(self, data, path: str, file_name: str):
        pathlib.Path(path).mkdir(parents=True, exist_ok=True)
        with open(f"{path}{file_name}.json", "w") as f:
            f.write(data)

    """
    Gets teams at competition. Name of json file reflects the function name. This will be a standard for all functions.
    """ 
    def teams_at_comp(self, event_key: str):
        req = requests.get(f"https://www.thebluealliance.com/api/v3/event/{event_key}/teams/simple", headers={"X-TBA-Auth-Key": self.tba_key})
        path = f"data/{self.year}/events/{event_key}/"
        self.save_data(req.text, path, "teams_at_comp")
        return path + "teams_at_comp.json" 

    """
    Probably re-inventing the wheel here, but I'm going to keep it around for now anyways. 
    Function loads json file from given event and data type (ex. "teams_at_comp")
    """
    def get_path(self, event_key: str, data_type: str):
        return f"data/{self.year}/events/{event_key}/{data_type}.json"

    


if __name__ == "__main__":
    sandstone = Sandstone()
    loaded_json = sandstone.load_data(sandstone.get_path("2022mibb", "teams_at_comp"))

    

