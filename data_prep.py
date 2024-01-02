import pandas as pd
import numpy as np


# from currency_scraper import currency_scraper


def data_prep():
    df = pd.read_csv('csv/watchlist_scrape.csv')
    df = df.assign(Amount=[0.002537, 20678250,221, 1175, 0.0462, 70, 1.5])
    df = df.assign(Invested=[100, 100, 100, 100, 100, 100, 100])
    df['Value, Eur'] = df['Price'] * df['Amount'] * 1.044
    df['Value, Eur'] = df["Value, Eur"].round(2)
    df['%'] = ((df['Value, Eur'] - df['Invested']) / df['Invested']) * 100
    df['%'] = df['%'].round(1)
    df_sorted = df.sort_values('%', ascending=False)
    df_sort_val = df.sort_values('Value, Eur', ascending=False)

    df.loc['Total'] = df.sum(numeric_only=True)

    df.to_csv('csv/prep_data.csv', index=False)
    # print(df_sort_val.to_string())
    # print(df_sorted.to_string())
    print('New "prep_data.csv" saved')

# data_prep()