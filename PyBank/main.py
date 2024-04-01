# Your task is to create a Python script that analyzes the records to calculate each of the following values:

# The total number of months included in the dataset - Done

# The net total amount of "Profit/Losses" over the entire period - Done

# The changes in "Profit/Losses" over the entire period, and then the average of those changes - Done

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

import csv
election_file_path = "PyBank/Resources/budget_data.csv"

totalNumMonths = 0
netTotal = 0
totalChanges = 0
numChanges = 0

previousChange = 0
averageChange = 0

greatestIncrease = 0
greatestIncDate = ""

greatestDecrease = 0
greatestDecDate = ""

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
        profitLosses = int(row[1])

        currentChange = 0

        # Get the net total amount
        netTotal += profitLosses

        # The changes in profit and losses and average of those changes
        # get the first the data for the first row
        if totalNumMonths == 1:
            previousChange = profitLosses
        else:
            currentChange = profitLosses - previousChange
            totalChanges += currentChange
            numChanges += 1
            previousChange = profitLosses

        # Get the greatest increase and decrease
        if(profitLosses > greatestIncrease):
            greatestIncrease = profitLosses
            greatestIncDate = date
        if(profitLosses < greatestDecrease):
            greatestDecrease = profitLosses
            greatestDecDate = date

averageChange = totalChanges / numChanges
averageChange = round(averageChange, 2)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalNumMonths}")
print(f"Total: ${netTotal}")
print(f"Average Change: ${averageChange}")
print(f"Greatest Increase in Profits: {greatestIncDate} (${greatestIncrease})")
print(f"Greatest Decrease in Profits: {greatestDecDate} (${greatestDecrease})")




outFilePath = "PyBank\Analysis\Financial_Analysis.txt"

with open(outFilePath, 'w') as fileOut:
    fileOut.write("Financial Analysis\n")
    fileOut.write('-------------------------\n')
    fileOut.write(f"Total Months: {totalNumMonths}\n")
    fileOut.write(f"Total: ${netTotal}\n")
    fileOut.write(f"Average Change: ${averageChange}\n")
    fileOut.write(f"Greatest Increase in Profits: {greatestIncDate} (${greatestIncrease})\n")
    fileOut.write(f"Greatest Decrease in Profits: {greatestDecDate} (${greatestDecrease})")

# Your analysis should align with the following results:

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)