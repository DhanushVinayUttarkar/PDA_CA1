import requests
import pandas as pd
from pymongo import MongoClient
import config as cfg


# Creates a new stock market monthly dataset using the alpha-vantage api
def create_dataset():
    url = "https://alpha-vantage.p.rapidapi.com/query"

    querystring = {"symbol": "AAPL", "function": "TIME_SERIES_MONTHLY", "datatype": "csv"}

    # X-RapidAPI-Key contains your rapid API key
    headers = {
        "X-RapidAPI-Key": cfg.apikey,
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    with open('Time_Series_Stock_data.csv', 'w') as out:
        out.write(response.text)


def preprocess_dataset():
    df = pd.read_csv('Time_Series_Stock_data.csv')
    print(df.head())


def connect_to_database():
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(cfg.connection_string)

    # database and collection code goes here
    db = client.sample_guides
    coll = db.comets

    coll.drop()
    # insert code goes here
    docs = [
        {"name": "Halley's Comet", "officialName": "1P/Halley", "orbitalPeriod": 75, "radius": 3.4175, "mass": 2.2e14},
        {"name": "Wild2", "officialName": "81P/Wild", "orbitalPeriod": 6.41, "radius": 1.5534, "mass": 2.3e13},
        {"name": "Comet Hyakutake", "officialName": "C/1996 B2", "orbitalPeriod": 17000, "radius": 0.77671,
         "mass": 8.8e12},
    ]
    result = coll.insert_many(docs)
    # display the results of your operation
    print(result.inserted_ids, "\n")

    # find code goes here
    cursor = coll.find({"officialName": "1P/Halley"})

    # iterate code goes here
    for doc in cursor:
        print(doc)

    # Close the connection to MongoDB when you're done.
    client.close()


if __name__ == '__main__':
    # create_dataset()
    preprocess_dataset()
