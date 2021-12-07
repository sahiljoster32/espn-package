
from __future__ import annotations
from bs4 import BeautifulSoup
# pending with annotations

from url_provider import url_segments_cricket
from typing import *
import requests
import json
import pprint

batting_data = []

first_url = url_segments_cricket("batting", "high_scores", "test_match", "India")
# print(first_url.get_absolute_url())

# batting_testMatch_fetch_url = "https://stats.espncricinfo.com/ci/engine/records/batting/most_runs_career.html?class=1;id=6;type=team"
batting_oneDayInternationals_fetch_url = first_url.get_absolute_url()

requested_data = requests.get(batting_oneDayInternationals_fetch_url)
unparsed_data = BeautifulSoup(requested_data.text, 'html.parser')

# use pretiffy for prefect html representation.

def batting_data_parser(unparsed_data: list): # ok

    # Player_elem was collection of many "td" elements.
    # Player_data_elem was list version of player_elem. 
    batting_data_unparsed: list = unparsed_data.find_all(class_="data1")

    for player_elem in batting_data_unparsed:
        
        player_data: list = []

        player_data_elem = player_elem.find_all(nowrap="nowrap")
        player_link = player_data_elem[0].a["href"]

        player_data.append(player_link)

        for data in player_data_elem:
            player_data.append(data.get_text())

        batting_data.append(player_data)
    
    return batting_data

"""
task 1. json dump for every player data based on some condition.
task 2. class object for data
task 3. connecting with url provider
task 4. fecthing data some kind async current data. like ipt or t20. 
"""

pprint.pprint(batting_data_parser(unparsed_data))
