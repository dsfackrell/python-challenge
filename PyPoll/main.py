#The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote
# Your analysis should align with the following results:


#### Start Here
# create variables

# read a row in the file
# add to total votes

# print the results to file

import csv
election_file_path = "PyPoll\Resources\election_data.csv"

totalVotes = 0

# open file
with open(election_file_path) as election_file:
    csv_file = csv.reader(election_file)
    next(csv_file) # skips the first row
    # read a row in the file
    for row in csv_file:
        # add to total votes
        totalVotes += 1

# print the results to screen
print(totalVotes)

##### End Here


# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette

