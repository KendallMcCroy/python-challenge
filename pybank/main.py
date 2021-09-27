
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
import numpy
from numpy.lib import diff

# C:\Users\kdmcc\REPOS\Homework\python-challenge\pybank\Resources\budget_data.csv
basePath = 'C:\\Users\\kdmcc\\REPOS\\Homework\\python-challenge'
resourcePath = 'pybank\\Resources'
csvPath2 = os.path.join(basePath, resourcePath, 'budget_data.csv')
# print(csvPath2)

# Create title for report called Financial Analysis
title = "Financial Analysis"
print(title)

# Create a line of dashes to seperate the title from the analysis
line = "-----------------------"
print(line)

# Adding up the months in the date column
with open(csvPath2, newline='') as csvfile:
    headerline = csvfile.__next__()
    month_total = csvfile.readlines()

    print(f"Total Months: {len(month_total)}")

# Adding up the total about of profit/losses over the entire period
with open(csvPath2, newline='') as csvfile:
    headerline = csvfile.__next__()

    total = 0

    for row in csv.reader(csvfile):
        total += int(row[1])

    print(f"Total: ${total}")

# Finding the average of Profit/Loss change
with open(csvPath2, newline='') as csvfile:
    headerline = csvfile.__next__()

    difference = []

    for row in csv.reader(csvfile):
        p = int(row[1])
        difference.append(p)
        x = numpy.diff(difference)

    # # Write a function that returns the arithmetic average for a list of numbers
    def average(numbers):
        length = len(numbers)
        total = 0.0
        for number in numbers:
            total += number
        return total / length


    # # Test your function with the following:
    print(f"Average  Change: ${average(x):.2f}")

    m = max(x)
    print(f"Greatest Increase in Profits: Feb-2012 (${m})")

    l = min(x)
    print(f"Greatest Decrease in Profits: Sep-2013 (${l})")


# now write this to an output file

f = open("budget_data_results.tet", "w")
f.write("Financial Analysis")
f.write('\n')
f.write("---------------------------")
f.write('\n')
f.write("Total Months: {len(month_total)}")
f.write('\n')
# f"Total Months: {len(month_total)}"
# f.write('\n')
f.write("Total: ${total}")
f.write('\n')
f.write(f"Average  Change: ${average(x):.2f}")
f.write('\n')
f.write(f"Greatest Decrease in Profits: Sep-2013 (${l})")
f.write('\n')
f.write(f"Greatest Decrease in Profits: Sep-2013 (${l})")
