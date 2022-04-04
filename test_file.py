import matplotlib.pyplot as plt
import pandas as pd

csvReader = pd.read_csv('cachedFlightData.csv')
csvReader = csvReader["arr_iata"]
csvTouristReader = pd.read_csv('Data for tourists CSV.csv')
# csvTouristReader = csvTouristReader["Country", "TotalArrivals"]

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

print(len(airportDictionary))
airportDictionaryRestrictions = dict(airportDictionary)
for key, dictValue in airportDictionary.items():
    if airportDictionary[key] <= 50:
        del airportDictionaryRestrictions[key]
print(len(airportDictionaryRestrictions))

# OG Plot
destinations = []
incomingFlights = [1, 4, 9, 16, 25]

fig, axs = plt.subplots(1, 2, figsize=(10, 7))

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
for index,selectedCountries in enumerate(pd.read_csv("Data for tourists CSV.csv")["Country"]):
    try:
        countryDictionary[selectedCountries].append(pd.read_csv("Data for tourists CSV.csv")["TotalArrivals"][index])
    except:
        countryDictionary[selectedCountries] = [pd.read_csv("Data for tourists CSV.csv")["TotalArrivals"][index]]
    counter=counter+1
axs[1].plot(countryDictionary.keys(),countryDictionary.values())
axs[1].set_xticklabels(countryDictionary.keys(),rotation=90)
print(len(countryDictionary))

#countryDictionaryRestrictions = dict(countryDictionary)
#for key, dictionaryValue in countryDictionary.items():
  #  if countryDictionary[key] <= 1:
  #      del countryDictionaryRestrictions[key]
#print(len(countryDictionaryRestrictions))




# Line Graph
axs[1].set_title("Popular Tourist Destinations Based on Country")
axs[1].set_xlabel("Countries")
axs[1].set_ylabel("")
axs[1].plot()

plt.show()