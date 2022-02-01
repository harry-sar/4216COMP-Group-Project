import requests,json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def get_flight_data(api_key,type):
    main_url="https://airlabs.co/api/v9/flights"
    api_key="api_key="+api_key
    get_flight_pos="?&_fields=reg_number,lat,lng"
    if type=="all":
        final_url=main_url+"?"+api_key
        print(final_url)
    elif type=="basic":
        final_url=main_url+get_flight_pos+"&"+api_key

    get_req=requests.get(final_url).json()
    print(get_req)


def save_flight_data(api_key):
    main_url = "https://airlabs.co/api/v9/flights?api_key="+api_key
    print(main_url)
    request_data=requests.get(main_url).json()["response"]
    req_data=json.dumps(request_data)
    dataFile=pd.read_json(req_data)
    dataFile.to_csv('cachedFlightData.csv',encoding='utf-8',index=False)

    return dataFile

def load_cached_data():
    return pd.read_csv('cachedFlightData.csv')

if __name__=="__main__":
    flight_api_key = ""
    dataFile=save_flight_data("")
