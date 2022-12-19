import pymongo
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
    print(df.info())

    figure(figsize=(15, 8), dpi=80, linewidth=10)
    plt.plot(df['timestamp'], df['open'], color="red")
    plt.plot(df['timestamp'], df['close'], color="blue")
    plt.plot(df['timestamp'], df['high'], color="green")
    plt.plot(df['timestamp'], df['low'], color="cyan")
    plt.title('Missing value check')
    plt.xlabel('Years', fontsize=14)
    plt.ylabel('open, close, high, low', fontsize=14)
    plt.show()

    figure(figsize=(15, 8), dpi=80, linewidth=10)
    plt.plot(df['timestamp'], df['volume'], color="violet")
    plt.title('Missing value check')
    plt.xlabel('Years', fontsize=14)
    plt.ylabel('volume', fontsize=14)
    plt.show()

    return df


def create_database_and_store():
    # Create a connection using MongoClient
    client = MongoClient(cfg.connection_string)

    # database and collection code initialization code
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
    
    # print(df.head())
    # print(df.info())
    check_missing = df.isnull()
    # print(check_missing)
    for column in check_missing.columns.values.tolist():
        print(column)
        print(check_missing[column].value_counts())
        print("")

    # database operations

    # fetch data with the index value 3
    data = coll.find({"index": 3})
    for doc in data:
        print("The value in collection at index 3 is:", doc)
        print("\n")

    # Find the largest high and low value
    data1 = coll.find().sort("open", -1).limit(1)
    for doc1 in data1:
        print("The largest value at open in the collection is:", doc1)
        print("\n")

    data2 = coll.find().sort("close", -1).limit(1)
    for doc2 in data2:
        print("The largest value at close in the collection is:", doc2)
        print("\n")

    client.close()


if __name__ == '__main__':
    create_dataset()
    create_database_and_store()
