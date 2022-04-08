from turtle import left, right
import numpy as np
import matplotlib.pyplot as plt

years = [1995, 1999, 2003, 2007, 2011, 2015, 2019]
SriLankatourists = [414, 465, 583, 592, 976, 1993, 2027]
UKtourists = [23537, 25394, 24715, 32778, 31886, 36792, 40857]
Bahamastourists = [3239, 3648, 4594, 4601, 5588, 6112, 7250]
Canadatourists = [41657, 49055, 38903, 30373, 25066, 27555, 32430]
Ukrainetourists = [6127, 10990, 15161, 26162, 24535, 13025, 13710]

fig, ax = plt.subplots()

ax.plot(years, SriLankatourists, 'mD:')
ax.plot(years, UKtourists, 'yo--')
ax.plot(years, Bahamastourists, 'bo--')
ax.plot(years, Canadatourists, 'rs--')
ax.plot(years, Ukrainetourists, 'gD:')

ax.set_xlabel("Years", fontsize=12)
ax.set_ylabel("Number of Tourists (thousands)", fontsize=12)

plt.gca().legend(('Sri Lanka','UK', 'Bahamas', 'Canada', 'Ukraine',)) 
plt.legend(bbox_to_anchor=(1.05, 1.0, 0.3, 0.2), loc='upper left')

plt.show()