import matplotlib.pyplot as plt
import tourismdataloader

years = [1995, 1999, 2003, 2007, 2011, 2015, 2019, ]
SriLankatourists = [414, 465, 583, 592, 976, 1993, 2027]
UKtourists = [23537, 25394, 24715, 32778, 31886, 36792, 40857]
Bahamastourists = [3239, 3648, 4594, 4601, 5588, 6112, 7250]
Canadatourists = [41657, 49055, 38903, 30373, 25066, 27555, 32430]


fig, ax = plt.subplots()

ax.plot(years, SriLankatourists, 'mD:')
ax.plot(years, UKtourists, 'yo--')
ax.plot(years, Bahamastourists, 'bD:')
ax.plot(years, Canadatourists, 'rs--')

ax.set_xlabel("Years", fontsize=12)
ax.set_ylabel("Number of Tourists (thousands)", fontsize=12)

plt.show()