
from __future__ import annotations
from typing import *
import json

from constants import *


class url_segments_cricket:

    subclass: Dict(str, str) = subclass_const
    category: Dict(str, Dict(str, str)) = category_const
    # country_data: Dict(str, str) = country_data_const
    """
    Above Predefined constants are not meant to be touched
    """

    def __init__(self, category_sub_1: str, category_sub_2: str, subclass_query: str, country: str) -> None:
        self._category_sub_1 = category_sub_1
        self._category_sub_2 = category_sub_2
        self._subclass_query = subclass_query
        self._country = country

    def _data_binding(self, pre_html1, class_segment, country_key):
        # Get error for keywords defined in constants.py.
        return country_url_str(pre_html1, class_segment, country_key)

    def _get_subclass_number(self) -> str:
        return self.subclass.get(self._subclass_query)

    def _get_category(self) -> str:
        return self.category.get(self._category_sub_1).get(self._category_sub_2)

    def _get_url_class_segment(self) -> str:
        self._subclass_query_num = self._get_subclass_number()
        return f"class={self._subclass_query_num};"

    def get_relative_url(self) -> str:
        class_segment = self._get_url_class_segment()
        pre_html = self._get_category()

        return self._data_binding(pre_html, class_segment, self._country)

    def get_absolute_url(self) -> str:
        class_segment = self._get_url_class_segment()
        pre_html = self._get_category()
        # print(class_segment, pre_html)

        return 'https://stats.espncricinfo.com' + self._data_binding(pre_html, class_segment, self._country)


# first_url = url_segments("batting", "most_runs", "test_match", "India")
# print(first_url.get_absolute_url())
