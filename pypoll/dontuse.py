import os
import csv
import numpy
from numpy.lib import diff
# from numpy import get_include

# election_data_csv = os.path.join("..", "Resources", "election_data.csv")
# file_path = "Resources\election_data.csv"
# print(election_data_csv)
basePath = 'C:\\Users\\kdmcc\\REPOS\\Homework\\python-challenge'
resourcePath = 'pypoll\\Resources'
file_path = os.path.join(basePath, resourcePath, 'election_data.csv')

# create tite for report called Election Results
title = "Election Results"
print(title)

# Create a line of dashes to seperate the title from the election results
line = "-----------------------"
print(line)


# Get total votes
with open(file_path) as csvFile:
            headerline = csvFile.__next__() 
            vote_total = csvFile.readlines()

print(f"Total Votes: {len(vote_total)}") 

# Create a line of dashes to seperate the title from the election results
line = "-----------------------"
print(line)

with open( file_path, newline='' ) as csvFile:
    headerline = csvFile.__next__() 
    # Csv reader specifies delimiter and variable that holds contents
    csvReader = csv.reader(csvFile, delimiter=',')

    # Complete a list of candidates who received votes
    votes = []
    khan_amount = 0
    khan_percentage = 0
    correy_amount = 0
    correy_percentage = 0
    li_amount = 0
    otooley_amount = 0
    candidate_votes = []

    # Created candidate list
    for row in csvReader:
        v = row[2]
        votes.append(v)

        if row[2] == "Khan":
            # Count
            khan_amount = khan_amount + 1

            # Sum
            # khan_amount = khan_amount + int(row[0])

        if row[2] == "Correy":
            # Count
            correy_amount = correy_amount + 1

        if row[2] == "Li":
            # Count
            li_amount = li_amount + 1

        if row[2] == "O'Tooley":
            # Count
            otooley_amount = otooley_amount + 1

    votes_total = len(votes)

    khan_percentage = khan_amount / votes_total
    correy_percentage = correy_amount / votes_total
    li_percentage = li_amount / votes_total
    otooley_percentage = otooley_amount / votes_total



print(f"Khan: {khan_percentage:.3%} ({khan_amount})")
print(f"Correy: {correy_percentage:.3%} ({correy_amount})")
print(f"Li: {li_percentage:.3%} ({li_amount})")
print(f"O'Tooley: {otooley_percentage:.3%} ({otooley_amount})")


