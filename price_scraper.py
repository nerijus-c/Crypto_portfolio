from urllib.parse import urlencode
import pandas as pd
import requests
import time
from datetime import datetime


def web():
    timestamp = time.time()
    date = datetime.fromtimestamp(timestamp)
    str_date = date.strftime("%Y-%b-%d")


    query_string = [
        ('start', '1'),
        ('limit', '2500'),
        ('sortBy', 'market_cap'),
        ('sortType', 'desc'),
        ('convert', 'EUR'),
        ('cryptoType', 'all'),
        ('tagType', 'all'),
    ]

    base = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?"
    response = requests.get(f"{base}{urlencode(query_string)}").json()

    results = [
        [
            currency["name"],
            round(currency["quotes"][0]["price"], 8),
        ]
        for currency in response["data"]["cryptoCurrencyList"]
    ]


    headers=("Currency", "Price")
    df = pd.DataFrame(results, columns=headers)
    # print(tabulate(results, headers=["Currency", "Price"]))
    # print(df.to_string())

    my_list = ['Bitcoin', 'Ethereum', 'Solana', 'Immutable', 'Decentraland', 'Dogecoin', 'Bonk']

    mask = df['Currency'].isin(my_list)
    watchlist = df[mask]
    watchlist = watchlist[['Currency', 'Price']].reset_index(drop=True)
    watchlist = watchlist.sort_values(by=['Currency']).reset_index(drop=True)

    watchlist.to_csv('csv/watchlist_scrape.csv', index=False)
    print("New data saved to: watchlist_scrape.csv")

#     print(watchlist)
#
# web()