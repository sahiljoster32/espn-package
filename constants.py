
from __future__ import annotations

# constants for maintaining data 

pre_html_temp: str = None
class_segment_temp : str = None

# data related to url
category_const = {
    "batting": {
        "most_runs": "batting/most_runs_career",
        "high_scores": "batting/most_runs_innings",
        "highest_averages": "batting/highest_career_batting_average"
    },
    "bowling": {
        "most_wickets": "bowling/most_wickets_career",
        "best_bowling_figures": "bowling/best_figures_innings",
        "best_averages": "bowling/best_career_bowling_average"
    }
}
subclass_const = {
    "test_match": "1",
    "one_day_internationals": "2",
    "20_20_internationals": "3"
}

def country_url_str(pre_html, class_segment, country_key) :
    
    country_data_const = {
        'Afghanistan': f"/ci/engine/records/{pre_html}.html?{class_segment}id=40;type=team",
        'Africa XI': f"/ci/engine/records/{pre_html}.html?{class_segment}id=4058;type=team",
        'Asia XI': f"/ci/engine/records/{pre_html}.html?{class_segment}id=106;type=team",
        'Australia': f"/ci/engine/records/{pre_html}.html?{class_segment}id=2;type=team",
        'Bangladesh': f"/ci/engine/records/{pre_html}.html?{class_segment}id=25;type=team",
        'Bermuda': f"/ci/engine/records/{pre_html}.html?{class_segment}id=12;type=team",
        'Canada': f"/ci/engine/records/{pre_html}.html?{class_segment}id=17;type=team",
        'East Africa': f"/ci/engine/records/{pre_html}.html?{class_segment}id=14;type=team",
        'England': f"/ci/engine/records/{pre_html}.html?{class_segment}id=1;type=team",
        'Hong Kong': f"/ci/engine/records/{pre_html}.html?{class_segment}id=19;type=team",
        'ICC World XI': f"/ci/engine/records/{pre_html}.html?{class_segment}id=140;type=team",
        'India': f"/ci/engine/records/{pre_html}.html?{class_segment}id=6;type=team",
        'Ireland': f"/ci/engine/records/{pre_html}.html?{class_segment}id=29;type=team",
        'Kenya': f"/ci/engine/records/{pre_html}.html?{class_segment}id=26;type=team",
        'Namibia': f"/ci/engine/records/{pre_html}.html?{class_segment}id=28;type=team",
        'Nepal': f"/ci/engine/records/{pre_html}.html?{class_segment}id=32;type=team",
        'Netherlands': f"/ci/engine/records/{pre_html}.html?{class_segment}id=15;type=team",
        'New Zealand': f"/ci/engine/records/{pre_html}.html?{class_segment}id=5;type=team",
        'Oman': f"/ci/engine/records/{pre_html}.html?{class_segment}id=37;type=team",
        'Pakistan': f"/ci/engine/records/{pre_html}.html?{class_segment}id=7;type=team",    
        'Papua New Guinea': f"/ci/engine/records/{pre_html}.html?{class_segment}id=20;type=team",
        'Scotland': f"/ci/engine/records/{pre_html}.html?{class_segment}id=30;type=team",
        'South Africa': f"/ci/engine/records/{pre_html}.html?{class_segment}id=3;type=team",
        'Sri Lanka': f"/ci/engine/records/{pre_html}.html?{class_segment}id=8;type=team",
        'United Arab Emirates': f"/ci/engine/records/{pre_html}.html?{class_segment}id=27;type=team",
        'United States of America': f"/ci/engine/records/{pre_html}.html?{class_segment}id=11;type=team",
        'West Indies': f"/ci/engine/records/{pre_html}.html?{class_segment}id=4;type=team",
        'Zimbabwe': f"/ci/engine/records/{pre_html}.html?{class_segment}id=9;type=team"
    }

    return country_data_const.get(country_key)
