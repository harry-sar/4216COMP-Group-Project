import matplotlib.pyplot as plt
import csv

destinations = [1, 2, 3, 4, 5]
incomingFlights = [1, 4, 9, 16, 25]
touristHistory = [5, 10, 15, 20, 25]

fig, axs = plt.subplots(1, 2)

axs.plot(destinations, incomingFlights, touristHistory)

axs[0].setTitle("Busiest Airports")
axs[1].setTitle("Popular Tourist Destinations")

axs[0].bar(destinations, incomingFlights)
axs[1].line(destinations, touristHistory)

plt.show()
