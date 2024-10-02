import csv     # imports the csv module
import sys     # imports the sys module

f = open('week01/TB_burden_countries_2014-09-29.csv') # opens the csv file
for row in csv.reader(f):
    print(row)