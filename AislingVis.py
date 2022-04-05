import matplotlib.pyplot as plt
import pandas as pd

csvReader = pd.read_csv('map_data/cachedFlightData.csv')
csvReader = csvReader["arr_iata"]
csvTouristReader = pd.read_csv('map_data/Data for tourists CSV.csv')

# Airport Dictionary
airportDictionary = {}
airportList = []
for let in csvReader:
    if let not in airportList:
        airportList.append(let)
for index, each in enumerate(csvReader):
    for eachPlace in airportList:
        if each == eachPlace:
            try:
                airportDictionary[eachPlace] += 1
            except KeyError:
                airportDictionary[eachPlace] = 1

airportDictionaryRestrictions = dict(airportDictionary)
for key, dictValue in airportDictionary.items():
    if airportDictionary[key] <= 50:
        del airportDictionaryRestrictions[key]

# OG Plot
destinations = []
incomingFlights = [1, 4, 9, 16, 25]

fig, axs = plt.subplots(1, 2, figsize=(10, 8))

# Bar Chart
axs[0].set_title("Amount of Flights Arriving to the Airports")
axs[0].set_xlabel("Airports")
axs[0].set_ylabel("Number of flights Arriving to the Airport")
axs[0].bar([str(airportName) for airportName, flightData in airportDictionaryRestrictions.items()], [int(yesAirportName) for noAirportName, yesAirportName in airportDictionaryRestrictions.items()])
axs[0].set_xticklabels([str(airportName) for airportName, flightData in airportDictionaryRestrictions.items()], rotation=90)
plt.savefig('Amount Of Flights.png')

# Country Dictionary
counter=0
countryDictionary = {}
for index,selectedCountries in enumerate(pd.read_csv("map_data/Data for tourists CSV.csv")["Country"]):
    try:
        countryDictionary[selectedCountries].append(pd.read_csv("map_data/Data for tourists CSV.csv")["TotalArrivals"][index])
    except:
        countryDictionary[selectedCountries] = [pd.read_csv("map_data/Data for tourists CSV.csv")["TotalArrivals"][index]]


dictV2={}

for eachCount,listValues in countryDictionary.items():
    if eachCount in ["Turkey","United Kingdom","United States of America","Spain","Bahrain"]:
        dictV2[eachCount]=listValues

years=[]
for year in range(20):
    years.append(2000+year)

countMe=0
dictV3=dict({})

for place,listValues in dictV2.items():
    for eachYearValue in listValues:
        if countMe>=5:
            try:
                if place=="United Kingdom":
                    dictV3["UK"].append(eachYearValue)
                elif place=="United States of America":
                    dictV3["USA"].append(eachYearValue)
                else:
                    dictV3[place].append(eachYearValue)
            except:
                if place=="United Kingdom":
                    dictV3["UK"]=[eachYearValue]
                elif place=="United States of America":
                    dictV3["USA"]=[eachYearValue]
                else:
                    dictV3[place] = [eachYearValue]
        countMe+=1
    countMe=0


axs[1].plot(dictV3.keys(),dictV3.values(),label=years)
axs[1].set_xticklabels(dictV3.keys(),rotation=90)
axs[1].legend(loc="upper right")

# Line Graph
axs[1].set_title("Popular Tourist Destinations Based on Country")
axs[1].set_xlabel("Countries")

def RunVis():
    plt.show()
if __name__=='__main__':
    RunVis()