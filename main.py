import requests
import pandas as pd
from pymongo import MongoClient
import config as cfg
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt


# Creates a new stock market monthly dataset using the alpha-vantage api
def create_dataset():
    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"symbol": "AAPL", "function": "TIME_SERIES_MONTHLY", "datatype": "csv"}

    # X-RapidAPI-Key contains the rapid API key
    headers = {
        "X-RapidAPI-Key": cfg.apikey,
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    with open('Time_Series_Stock_data.csv', 'w') as out:
        out.write(response.text)


def preprocess_data():
    df = pd.read_csv('Time_Series_Stock_data.csv')
    # print(df.info(), "\n")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    # print(df.info())
    print("before sorting\n", df.head())
    df.sort_values(by=['timestamp'], inplace=True, ascending=True)
    print("\nafter sorting\n", df.head(), "\n")

    figure(figsize=(15, 8), dpi=80, linewidth=10)
    plt.plot(df['timestamp'], df['volume'], color="r")
    plt.title('Missing value check')
    plt.xlabel('Years', fontsize=14)
    plt.ylabel('volume of shares sold', fontsize=14)
    plt.show()

    return df


def create_database_and_store():
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(cfg.connection_string)

    # database and collection code goes here
    db = client.stockmarket_timeseries
    coll = db.Apple_stock

    coll.drop()
    df = preprocess_data()
    # print(df.head())
    df.reset_index(inplace=True)
    data_dict = df.to_dict('records')
    # print(data_dict)
    coll.insert_many(data_dict)
    # print(client.list_database_names())

    # find code goes here
    cursor = coll.find({"index": 3})

    # iterate code goes here
    for doc in cursor:
        print(doc)

    client.close()
    
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
    preprocess_data()
    create_database_and_store()
