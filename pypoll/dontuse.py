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

    print(otooley_amount)
































#     # print(csvReader)

#     # Read the head
#     csv_header = next(csvReader)
#     # print(f"CSV Header: {csv_header}")

#     # Read each row of data after header
#     print(csvReader[0])
#     for row in csvReader:
#         # print(row)

        # candidate_votes = candidate_votes + 1

        # # Get the candidate name from each row.
        # candidates_name = row[2]

        # if candidates_name not in candidates:
    
        #     # Add candidate name to list
        #     candidates.append(row[2])

        #     # And begin tracking that candidate's voter count.
        #     candidate_votes[candidates] = 0

        # # Add a vote to that candidate's count
        # candidate_votes[candidates] += 1
        


    #  with open(election_data_csv, newline='') as csvFile:

    #     csvReader = csv.reader(csvFile, delimiter=",")
    
    #     for row in csvReader:
        


            # print(csvReader)



#------------------------------------------------------------------------------------------------------

# with open(election_data_csv) as ed_file:
#     reader = csv.reader(ed_file)

#     header = next(reader)
       
    # # Loop through ed_data
    # for row in reader:
    #     # print(header)
        
    
    


        # # A total number of votes cast
        # total_vote_cast = total_vote_cast + 1 
        # return total_vote_cast
    
    
    # header = next(ed_file)
    # print(f'header = {header}')



#From 34.31 in video 3.3
# print(f'{candidates["name"][0]}')
# print(f'{candidates["name"][1]}')
# print(f'{candidates["name"][2]}')
# print(f'{candidates["name"][3]}')
