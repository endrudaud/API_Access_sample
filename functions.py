import requests
import time
import pandas as pd

def get_estates_data(category_main_cb, category_type_cb, page, locality_region_id=10):
    category_main_cb_dict = {'flat':1, 'house':2, 'land':3 }
    category_type_cb_dict = {'sell':1,'rent':2}

    try:
        category_main_cb_value = category_main_cb_dict[category_main_cb]
        category_type_cb_value = category_type_cb_dict[category_type_cb]
    except KeyError:
        return "Invalid category_main_cb or category_type_cb"

    base_url = 'https://www.sreality.cz/api/cs/v2/estates'
    params = {
        'category_main_cb': category_main_cb_value,
        'category_type_cb': category_type_cb_value,
        'locality_region_id': locality_region_id,
        'per_page': 60,
        'page': page
    }

    r = requests.get(base_url, params=params)
    time.sleep(0.5)

    if r.status_code == 200:
        return r.json()
    else:
        return "Error: " + str(r.status_code)
    
def json_to_dataframe(json_data):
    df = pd.json_normalize(json_data['_embedded']['estates'])
    return df