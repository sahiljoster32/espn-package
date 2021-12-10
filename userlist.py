
from __future__ import annotations
from bs4 import BeautifulSoup
# pending with annotations

from url_provider import url_segments_cricket
from typing import *
import requests
import json
import re # currently of no use
import pprint

# properties going to be private!!
headings: List = []
batting_data: List = []
main_data_dict = {}

# this first_url is temp object not meant be used in real scenario.
first_url = url_segments_cricket(
    "bowling", "most_wickets", "test_match", "India")
print(first_url.get_absolute_url())

batting_oneDayInternationals_fetch_url = first_url.get_absolute_url()

requested_data = requests.get(batting_oneDayInternationals_fetch_url)
unparsed_data = BeautifulSoup(requested_data.text, 'html.parser')


def cricket_data_parser(unparsed_data: list) -> List:
    """
    Function to fetch actual raw-data from site and
    supply it into the form of list.
    """

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


def cricket_data_heading(unparsed_data: list) -> NoReturn:
    """
    Function to parse or fetch headings of each columns.
    """

    main_table_ele = unparsed_data.find("thead")
    heading_elements: List = main_table_ele.find_all("th")

    for element_head in heading_elements:
        head_text = element_head.get_text()
        if head_text != '':
            headings.append(element_head.get_text())


def url_checker(Raw_url: str) -> str:
    """
    task: generat or raise error for invalid url. -- pending.
    """
    pass


def mainData_binder(headings: List, batting_data: List) -> NoReturn:
    """
    DOC: binds data with their respectie field and supply it into dictionary format.
    """
    headingsLen = len(headings)
    basicDataLen = len(batting_data[0])

    if headingsLen == (basicDataLen - 1):
        for player_id, data in enumerate(batting_data):
            temp_player_data = {}

            for index in range(headingsLen + 1):
                if index == 0:
                    temp_player_data["player_url"] = data[index]
                elif index != 0:
                    temp_player_data[headings[index - 1]] = data[index]

            main_data_dict[f"player_{player_id + 1}"] = temp_player_data

def metaData_binder():
    pass

# -------------main run code
# pprint.pprint(cricket_data_parser(unparsed_data))

cricket_data_parser(unparsed_data)
cricket_data_heading(unparsed_data)
# print( headings)
# pprint.pprint(batting_data)
data_binder(headings, batting_data)
pprint.pprint(main_data_dict)


"""
task 1. json dump for every player data based on some condition. -- after class object 
task 2. class object for data --- second priority after url check finished
task 3. connecting with url provider X done
task 4. fecthing data some kind async current data. like ipt or t20. ---- last priority
task 5. regex for url parameters.....
"""

"""
task to be resolved
ok with batting part but except high_scores's missed value.
"""