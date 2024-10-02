import csv     # imports the csv module
import sys     # imports the sys module

filename = 'week01/TB_burden_countries_2014-09-29.csv'  # replace with your CSV file name

# Count the number of rows
with open(filename, 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)  # skip the header line
    row_count = 0
    for row in csv_reader:
        row_count += 1

print(f'Number of rows: {row_count}')

