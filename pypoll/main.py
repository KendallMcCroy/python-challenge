import os
import csv

from numpy import get_include

# C:\Users\kdmcc\REPOS\Homework\python-challenge\pypoll\Resources\election_data.csv
basePath = 'C:\\Users\\kdmcc\\REPOS\\Homework\\python-challenge'
resourcePath = 'pypoll\\Resources'
csvPath2 = os.path.join(basePath, resourcePath, 'election_data.csv')
# print(csvPath2)

# total rows not including header
totalVotes = 0

votesPerCandidate = {}

with open(csvPath2, newline='') as csvfile:

    # CSV reader specifies delimiter and variale that hods contents
    csvreader = csv.reader(csvfile, delimiter=',')

# print(csvreader)
    csv_header = next(csvreader)

# Read each row of data after the header
    for row in csvreader:
        totalVotes += 1
        if row[2] not in votesPerCandidate:
            votesPerCandidate[row[2]] = 1
        else:
            votesPerCandidate[row[2]] += 1 


#Create title for report called Election Results
title = "Election Results"
print(title)
line = "-----------------------"
print(line)
print("Total Votes: " + str(totalVotes))
print(line)

# Found that part online....(https://gitlab.com/laurelstewart/python-challenge/-/blob/master/PyPoll/main.py)
for candidate, votes in votesPerCandidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    
print(line)

winner = max(votesPerCandidate, key=votesPerCandidate.get)
print (f"Winner: {winner}")

# write this to an output file 
f = open("election_results.txt", "w")
f.write("Election Results")
f.write('\n')
f.write("-------------------------")
f.write('\n')
f.write("Total Votes: " + str(totalVotes))
f.write('\n')
f.write("-------------------------")
f.write('\n')

for candidate, votes in votesPerCandidate.items():
    f.write(candidate + ": " + "{:.3%}".format(votes/totalVotes) + "   (" +  str(votes) + ")")
    f.write('\n')
  
f.write("-------------------------") 
f.write('\n')
f.write(f"Winner: {winner}")
f.write('\n')