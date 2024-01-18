import os

import csv

candidates = {}
voter = []

total_votes = 0

csvpath = os.path.join('.'/'Python-Challenge'/'Pypoll'/'Resources'/'election_data.csv')

text_path = "results.txt"

with open('election_data.csv') as file:

    csvreader = csv.reader(file, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        candidate = row[2]
        total_votes += 1
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

print("Total Votes:", total_votes)

print("Candidates who received votes:")
for candidate, votes in candidates.items():
    average_votes = votes / total_votes * 100
    print(candidate, ":", average_votes, "%", "(", votes, ")")


winner = max(candidates, key=candidates.get)
print("Winner:", winner)

with open("results.txt", "w") as file:

    file.write("Total Votes: " + str(total_votes) + "\n")
    
    file.write("Candidates who received votes:\n")
    for candidate, votes in candidates.items():
        average_votes = votes / total_votes * 100
        file.write(candidate + ": " + str(average_votes) + "%" + " (" + str(votes) + ")\n")
    
    winner = max(candidates, key=candidates.get)
    file.write("Winner: " + winner + "\n")

