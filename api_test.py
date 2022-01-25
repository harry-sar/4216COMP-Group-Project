import requests,json

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


if __name__=="__main__":
    flight_api_key = ""
    get_flight_data(flight_api_key,"basic")

