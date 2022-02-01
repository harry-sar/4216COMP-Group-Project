import requests,json
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
    dataFile.to_csv('map_data/cachedFlightData.csv',encoding='utf-8',index=False)

    return dataFile

def load_cached_data():
    return pd.read_csv('map_data/cachedFlightData.csv')

def matLibShow(api_key,cacheBool,place,saveToFile):
    try:
        if cacheBool==True:
            dataFile=load_cached_data()
        else:
            try:
                dataFile=save_flight_data(api_key)
            except:
                print("Problem Accessing API")
                quit(0)
    except:
        dataFile=load_cached_data()

    # boundingBox = ((dataFile.lng.min(), dataFile.lng.max(),
    #          dataFile.lat.min(), dataFile.lat.max()))

    if place.upper() in ["UK"]:
        figure, mapLd = plt.subplots(figsize=(10, 10))
        BBox = ((-12.05, 2.62, 49.88, 61.13))
        map = plt.imread('map_data/uk_map.jpeg')
        mapLd.set_title = ("UK live flight data")
    elif place.upper() in ["WORLD"]:
        figure, mapLd = plt.subplots(figsize=(20, 20))
        BBox = ((dataFile.lng.min(), dataFile.lng.max(),
                 dataFile.lat.min(), dataFile.lat.max()))
        map=plt.imread('map_data/world_map.jpeg')
        mapLd.set_title = ("World map live flight data")
    else:
        print("invalid location")
        quit(0)
    mapLd.scatter(dataFile.lng,dataFile.lat,alpha=0.4,c='#900603')
    mapLd.set_xlim(BBox[0],BBox[1])
    mapLd.set_ylim(BBox[2],BBox[3])
    mapLd.imshow(map,zorder=0,extent=BBox,aspect='equal')
    if saveToFile==True:
        plt.savefig('live_flight_data.png')
    plt.show()

if __name__=="__main__":
    api_key = "018ec34c-8a03-4cd6-aa66-026d1a0385cf"
    matLibShow(api_key,True,"uk",True)

