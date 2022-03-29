import json
import matplotlib.pyplot as plt
import pandas as pd
import requests
import matplotlib


def get_flight_data(api_key, type):
    main_url = "https://airlabs.co/api/v9/flights"
    api_key = "api_key=" + api_key
    get_flight_pos = "?&_fields=reg_number,lat,lng"
    if type == "all":
        final_url = main_url + "?" + api_key
        print(final_url)
    elif type == "basic":
        final_url = main_url + get_flight_pos + "&" + api_key

    get_req = requests.get(final_url).json()
    print(get_req)


def save_flight_data(api_key):
    main_url = "https://airlabs.co/api/v9/flights?api_key=" + api_key
    print(main_url)
    request_data = requests.get(main_url).json()["response"]
    req_data = json.dumps(request_data)
    dataFile = pd.read_json(req_data)
    dataFile.to_csv('cachedFlightData.csv', encoding='utf-8', index=False)

    return dataFile


def load_cached_data():
    return pd.read_csv('cachedFlightData.csv')


def load_all_flights(df):
    print(df.to_string())


def load_specific_flight(df):
    userFlightNum = input("Please enter the flight number that you'd like the information for: ")
    print((df[df["flight_icao"] == userFlightNum]).to_string())


def load_flight_status(df):
    userStatus = int(input("Please choose one of the following status types:\n1. Currently Airborne\n2. On the "
                           "Ground\n?: "))
    if userStatus == 1:
        print((df[df["status"] == "en-route"]).to_string())
    elif userStatus == 2:
        print((df[df["status"] == "landed"]).to_string())
    else:
        print("That option was invalid, please try again.")
        load_flight_status(df)

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


if __name__ == "__main__":
    flight_api_key = "018ec34c-8a03-4cd6-aa66-026d1a0385cf"
    df = load_cached_data()
    # dataFile=save_flight_data("")
    # load_specific_flight(df)
    # load_all_flights(df)
    # load_flight_status(df)
    # ryanVisualisation(df)
    ryanHeatmap()