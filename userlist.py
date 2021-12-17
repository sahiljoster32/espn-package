
from __future__ import annotations
from bs4 import BeautifulSoup

from url_provider import url_segments_cricket
from typing import *
import requests
import json
import datetime
import pprint  # should only be used for print

# properties going to be private!!
headings_values: List = []
headings_description: List = []
batting_data: List = []
main_data_dict = {}
meta_data_dict = {}

raw_data = {}

first_url: url_segments_cricket = url_segments_cricket(
    "batting",
    "high_scores",
    "test_match",
    "India"
)
source_url = first_url.get_absolute_url()
# print(source_url)
batting_oneDayInternationals_fetch_url: str = source_url

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
    Function to parse and fetch headings of each columns.
    """

    main_table_ele = unparsed_data.find("thead")
    heading_elements: List = main_table_ele.find_all("th")

    for head_element in heading_elements:

        head_text = head_element.get_text()
        if head_text != '':
            head_title_txt = head_element.get('title')

            headings_values.append(head_element.get_text())
            headings_description.append(head_title_txt)


def mainData_binder(headings: List, batting_data: List) -> NoReturn:
    """
    DOC: binds data with their respective field and supply it into dictionary format.
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


def metaData_binder(headings_values: List, headings_description: List) -> NoReturn:
    """
    DOC: This function fetch and populate meta data from site.
    """

    fields_description = {}
    current_date = datetime.datetime.now()

    meta_data_dict["current_stamp"] = f"{current_date}"

    if len(headings_description) == len(headings_values):
        for index, value in enumerate(headings_values):
            fields_description[headings_values[index]
                               ] = headings_description[index]
        fields_description['player_url'] = 'relative link of each player'

    meta_data_dict['field_description'] = fields_description
    meta_data_dict['source_url'] = source_url
    meta_data_dict['data_length'] = len(batting_data)
    meta_data_dict['keys'] = headings_values
    meta_data_dict['keys'].append('player_url')
    meta_data_dict['keys_length'] = len(headings_values)


def get_rawData(meta_data_dict: Dict[str, Any], main_data_dict: Dict[str, str]) -> NoReturn:
    """
    DOC: This returns raw data which was in python format.
    """
    raw_data['meta_data'] = meta_data_dict
    raw_data['data'] = main_data_dict


def get_json_data(raw_data: Dict[str, Dict[str, Any]]) -> str:
    """
    DOC: This function gives json formatted data,
    to send further.
    """
    return json.dumps(raw_data)


if __name__ == "__main__":
    cricket_data_parser(unparsed_data)
    cricket_data_heading(unparsed_data)
    mainData_binder(headings_values, batting_data)
    metaData_binder(headings_values, headings_description)
    get_rawData(meta_data_dict, main_data_dict)
    print(get_json_data(raw_data))


"""
task 2. class object for data 
task 4. fecthing data some kind async current data. like ipt or t20. ---- last priority
"""
