import json
import matplotlib.pyplot as plt
import pandas as pd
import requests

def ryanVisualisation(df):
    aircraftCountry = ["US","CN","IE","UK","IN"]
    values = [0,0,0,0,0]
    for x in df["flag"]:
        if x == "US":
            values[0] += 1
        elif x == "CN":
            values[1] += 1
        elif x == "IE":
            values[2] += 1
        elif x == "UK":
            values[3] += 1
        elif x == "IN":
            values[4] += 1
        else:
            None
    fig, axs = plt.subplots(1, 2,sharey = True)
    axs[0].set_title("Scatter Graph\nTop 5 Air Traffic Countries")
    axs[0].scatter(aircraftCountry, values)
    axs[0].set_xlabel("Country Codes")
    axs[0].set_ylabel("Number of Active Flights")
    axs[1].set_title("Bar Chart\nTop 5 Air Traffic Countries")
    axs[1].bar(aircraftCountry,values)
    axs[1].set_xlabel("Country Codes")
    axs[1].set_ylabel("Number of Active Flights")
    plt.show()

def ryanHeatmap():
    figure, mapLd = plt.subplots(figsize=(10,10))
    boundingBox = (67.39, 35.99, -25.12, 48.20)
    map = plt.imread('mapEurope.png')
    mapLd.set_title = ("European Flights Heatmap")
    plt.show()

def load_cached_data():
    return pd.read_csv('cachedFlightData.csv')

if __name__ == "__main__":
    flight_api_key = "018ec34c-8a03-4cd6-aa66-026d1a0385cf"
    df = load_cached_data()
    ryanVisualisation(df)