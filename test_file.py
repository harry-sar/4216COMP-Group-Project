import csv
from gettext import install

import matplotlib

with open('unwto-inbound-arrivals-data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    header_row = next(csv_reader)
print(header_row)

import matplotlib.pyplot as plt

plt.plot(xAxis,yAxis)
plt.title('title name')
plt.xlabel('xAxis name')
plt.ylabel('yAxis name')
plt.show()