# Your task is to create a Python script that analyzes the records to calculate each of the following values:

# The total number of months included in the dataset - Done

# The net total amount of "Profit/Losses" over the entire period - Done

# The changes in "Profit/Losses" over the entire period, and then the average of those changes 

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

import csv
election_file_path = "PyBank\Resources\budget_data.csv"

totalNumMonths = 0
netTotal = 0
totalChanges = 0
numChanges = 0

previousChange = 0

# open file
with open(election_file_path) as election_file:
    csv_file = csv.reader(election_file)
    next(csv_file) # skips the first row
    # read a row in the file
    for row in csv_file:
        # get the total number of months
        totalNumMonths += 1

        # Date,Profit/Losses
        date = row[0]
        profitLosses = row[1]

        # Get the net total amount
        netTotal += profitLosses

        






        




# Your analysis should align with the following results:

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)