import requests,json,re
import matplotlib.pyplot as plt
import pandas as pd

class harrysVis:

    def __init__(self):
        self.years = []
        self.planesInAir={}
        self.overnightPlotData={}

    def get_flight_data(self,api_key,type):
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

    def save_flight_data(self,api_key):
        main_url = "https://airlabs.co/api/v9/flights?api_key="+api_key
        print(main_url)
        request_data=requests.get(main_url).json()["response"]
        req_data=json.dumps(request_data)
        dataFile=pd.read_json(req_data)
        dataFile.to_csv('map_data/cachedFlightData.csv',encoding='utf-8',index=False)

        return dataFile

    def load_cached_data(self):
        return pd.read_csv('map_data/cachedFlightData.csv')

    def load_tourism(self):
        return pd.read_csv('map_data/Data for tourists CSV.csv')

    def mapLiveFlights(self,api_key,cacheBool,place,saveToFile):
        try:
            if cacheBool==True:
                dataFile=self.load_cached_data()
            else:
                try:
                    dataFile=self.save_flight_data(api_key)
                except:
                    print("Problem Accessing API")
                    quit(0)
        except:
            dataFile=self.load_cached_data()

        if place.upper() in ["UK"]:
            figure, mapLd = plt.subplots(figsize=(10, 10))
            BBox = ((-12.05, 2.62, 49.88, 61.13))
            map = plt.imread('map_data/uk_map.jpeg')
            mapLd.set_title = ("UK live flight data")
        elif place.upper() in ["WORLD"]:
            figure, mapLd = plt.subplots(figsize=(10, 10))
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

    def initaliseGraphAnalysis(self,cacheBool,apiKey,tourismData,saveToFile):
        try:
            if cacheBool == True:
                flightFile = self.load_cached_data()
            else:
                try:
                    flightFile = self.save_flight_data(apiKey)
                except:
                    print("Problem Accessing API")
                    quit(0)
        except:
            flightFile = self.load_cached_data()

        figure,axes = plt.subplots(1,2,figsize=(10,12))

        # Gets the overnight stay data for a number of popular countries
        for amt,data in enumerate(tourismData["Country"]):
            if data=="Cyprus":
                try:
                    self.overnightPlotData["Cyprus"].append(tourismData["overnightStay"][amt])
                except:
                    self.overnightPlotData["Cyprus"]=[tourismData["overnightStay"][amt]]
                self.years.append(tourismData["years"][amt])
            if data=="Czech Republic":
                try:
                    self.overnightPlotData["Czech Republic"].append(tourismData["overnightStay"][amt])
                except:
                    self.overnightPlotData["Czech Republic"] = [tourismData["overnightStay"][amt]]
            if data=="Hong Kong - China":
                try:
                    self.overnightPlotData["Hong Kong - China"].append(tourismData["overnightStay"][amt])
                except:
                    self.overnightPlotData["Hong Kong - China"] = [tourismData["overnightStay"][amt]]
            if data=="Italy":
                try:
                    self.overnightPlotData["Italy"].append(tourismData["overnightStay"][amt])
                except:
                    self.overnightPlotData["Italy"] = [tourismData["overnightStay"][amt]]
            if data=="United States of America":
                try:
                    self.overnightPlotData["United States of America"].append(tourismData["overnightStay"][amt])
                except:
                    self.overnightPlotData["United States of America"] = [tourismData["overnightStay"][amt]]
            if data == "United Kingdom":
                try:
                    self.overnightPlotData["United Kingdom"].append(tourismData["overnightStay"][amt])
                except:
                    self.overnightPlotData["United Kingdom"] = [tourismData["overnightStay"][amt]]
        # Regex for getting amount of flights currently in the air
        for icao in flightFile["flight_icao"]:
            if re.search('^RYR',str(icao)):
                try:
                    self.planesInAir["Ryan Air"]+=1
                except KeyError:
                    self.planesInAir["Ryan Air"]=1
            if re.search('^BA',str(icao)):
                try:
                    self.planesInAir["British Airways"] += 1
                except KeyError:
                    self.planesInAir["British Airways"] = 1
            if re.search('^EZY',str(icao)):
                try:
                    self.planesInAir["easyJet"] += 1
                except KeyError:
                    self.planesInAir["easyJet"] = 1
            if re.search('^UAE',str(icao)):
                try:
                    self.planesInAir["Emirates"] += 1
                except KeyError:
                    self.planesInAir["Emirates"] = 1
            if re.search('^UAE',str(icao)):
                try:
                    self.planesInAir["Emirates"] += 1
                except KeyError:
                    self.planesInAir["Emirates"] = 1
            if re.search('^DAL',str(icao)):
                try:
                    self.planesInAir["Delta"] += 1
                except KeyError:
                    self.planesInAir["Delta"] = 1
            if re.search('^MAS',str(icao)):
                try:
                    self.planesInAir["Malaysia Airlines"] += 1
                except KeyError:
                    self.planesInAir["Malaysia Airlines"] = 1
            if re.search('^CCA',str(icao)):
                try:
                    self.planesInAir["Air China"] += 1
                except KeyError:
                    self.planesInAir["Air China"] = 1

        figure.suptitle("Plot of stay data leading up to COVID-19 & Current Flights Airbourne after COVID-19",fontsize=10)
        axes[0].set_ylabel("Amount of Overnight Visitors (x10^7)")
        axes[0].set_xlabel("Years")
        for daKey,daValue in self.overnightPlotData.items():
            axes[0].plot(self.years,self.overnightPlotData[daKey],label=daKey)
        axes[0].legend(loc="upper left")

        axes[1].set_ylabel("Amount of flights currently in the air")
        axes[1].set_xlabel("Airline Company")
        axes[1].bar([key for key,value in self.planesInAir.items()],[value for key,value in self.planesInAir.items()])
        axes[1].set_xticklabels([key for key,value in self.planesInAir.items()],rotation=90)

        if saveToFile==True:
            plt.savefig('COVID19 Effect.png')
        plt.show()
if __name__=="__main__":
    api_key = "018ec34c-8a03-4cd6-aa66-026d1a0385cf"
    harryVisObj=harrysVis()

    cacheSelect = input("please enter [true|false] do you want to use cached data? >>")
    if cacheSelect in ["true", "false"]:
        cacheSelect = cacheSelect.lower() in ["true"]
        harryVisObj.initaliseGraphAnalysis(cacheSelect, api_key, harryVisObj.load_tourism(),
                                           True)
    overlaySelect = input("Please enter place to map [world|uk] >>")
    if overlaySelect.lower() in ["uk", "world"]:
        harryVisObj.mapLiveFlights(api_key, cacheSelect, overlaySelect, True)

    if overlaySelect.lower() not in ["uk", "world"]:
        print("Invalid Data!, Try Again.")

