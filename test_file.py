import csv

with open('unwto-inbound-arrivals-data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    header_row = next(csv_reader)
print(header_row)