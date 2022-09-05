from tba_api import fetch_info
import requests
import json
from pprint import pprint

info_grab = fetch_info()

tba_key = info_grab.ret_tba_key()

file = open("event_info.json", "r")
data = json.load(file)

pprint(data)