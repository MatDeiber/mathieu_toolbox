import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import time
import random

import pandas as pd

pd.set_option("display.max_rows", None, "display.max_columns", None)

def coin_price(year,month,day):
    historical_date = date(year,month,day).strftime("%Y%m%d")
    page = requests.get(
        'https://coinmarketcap.com/historical/{}/'.format(historical_date),
        timeout=6)

    if page.status_code == 200:

        soup = BeautifulSoup(page.content, 'html.parser')
        all_lines = soup.find_all('tr', class_='cmc-table-row')
        parameters_dict = {
            'cmc_rank': [],
            'slug':[],
            'symbol': [],
            'market_cap':[],
            'price': [],
            'circulating_supply': [],
            'volume_24h': [],
            'percent_change_1h': [],
            'percent_change_24h': [],
            'percent_change_7d': []
        }

        for l in all_lines:
            all_cells = l.find_all('td', class_='cmc-table__cell')
            for param, c in zip(parameters_dict.keys(), all_cells):
                val = c.get_text()
                val = val.replace('$', '').replace(',', '').replace('%', '')
                parameters_dict[param].append(val)


        df = pd.DataFrame(parameters_dict)
        print(df)
        return df

    else:
        print(
            'Error getting data - Historical Date: {}'.format(historical_date))

if __name__ == "__main__":
    data = input('Enter year, month and day to get the price of the top 20 coins (e.g. 2020,7,3) : \n')
    year, month, day = data.split(',')
    coin_price(int(year), int(month), int(day))
