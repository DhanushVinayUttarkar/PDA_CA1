import requests
import pandas as pd
import config


# Creates a new stock market monthly dataset using the alpha-vantage api
def create_dataset():
    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"symbol": "AAPL", "function": "TIME_SERIES_MONTHLY", "datatype": "csv"}

    # X-RapidAPI-Key contains your rapid API key
    headers = {
        "X-RapidAPI-Key": config.apikey,
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    with open('Time_Series_Stock_data.csv', 'w') as out:
        out.write(response.text)


def preprocess_dataset():
    df = pd.read_csv('Time_Series_Stock_data.csv')
    # print(df.head())
    # print(df.info())
    check_missing = df.isnull()
    # print(check_missing)
    for column in check_missing.columns.values.tolist():
        print(column)
        print(check_missing[column].value_counts())
        print("")


if __name__ == '__main__':
    create_dataset()
    preprocess_dataset()
