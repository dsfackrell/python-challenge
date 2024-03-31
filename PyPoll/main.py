
#### Start Here

# print the results to file

import csv
election_file_path = "PyPoll\Resources\election_data.csv"

totalVotes = 0

candidates = []
candidateVotes = []

# open file
with open(election_file_path) as election_file:
    csv_file = csv.reader(election_file)
    next(csv_file) # skips the first row
    # read a row in the file
    for row in csv_file:
        # add to total votes
        totalVotes += 1

        #Ballot ID,County,Candidate
        ballot_id = row[0]
        county = row[1]
        candidate = row[2]

        if candidate not in candidates:
            # add to list if not in there
            candidates.append(candidate)
            candidateVotes.append(1) # add the first vote
        else:
            candidateId = candidates.index(candidate)

            candidateVotes[candidateId] += 1

#find the winner
winningCandidate = ""
winningCandidateVotes = 0

for candidate in candidates:
    currentVotes = candidateVotes[candidates.index(candidate)]
    if currentVotes > winningCandidateVotes:
        winningCandidate = candidate
        winningCandidateVotes = currentVotes


# print the results to screen
print("Election Results")        

print('-------------------------')
print(f"Total Votes: {totalVotes}")
print('-------------------------')

for candidate in candidates:
    currentCandidateVotes = candidateVotes[candidates.index(candidate)]
    currentVotePct = (currentCandidateVotes / totalVotes) * 100
    currentVotePct = round(currentVotePct, 3)
    print(f"{candidate}: {currentVotePct}% ({currentCandidateVotes})")
print('-------------------------')
print(f"Winner: {winningCandidate}")


# Print results to file
outFilePath = "PyPoll\Analysis\election_results.txt"

with open(outFilePath, 'w') as fileOut:
    fileOut.write("Election Results\n")
    fileOut.write('-------------------------\n')
    fileOut.write(f"Total Votes: {totalVotes}\n")
    fileOut.write('-------------------------\n')

    for candidate in candidates:
        currentCandidateVotes = candidateVotes[candidates.index(candidate)]
        currentVotePct = (currentCandidateVotes / totalVotes) * 100
        currentVotePct = round(currentVotePct, 3)
        fileOut.write(f"{candidate}: {currentVotePct}% ({currentCandidateVotes})\n")
    fileOut.write('-------------------------\n')
    fileOut.write(f"Winner: {winningCandidate}\n")

##### End Here