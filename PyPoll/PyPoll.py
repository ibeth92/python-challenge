# Import the module for reading CSV
import csv

import os

# Files to load and output
dirname = os.path.dirname(__file__)

csvpath = os.path.join(dirname,'Resources', 'election_data.csv')

print (csvpath)

# Create a dictionary to store totals
candidate_data = {
    "Correy":0,
    "Khan":0,
    "Li":0,
    "O'Tooley":0
}

# Read CSV using CSV module
with open(csvpath) as csvfile:

# CSV reader specifies delimiter and variable
    csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first 
    csv_header = next(csvreader)

# Set month counter and winner vote count
    total_votes = 0
    greatest_vote_total = 0

# Set path for .txt file
    file_path = os.path.join("analysis","PyPoll.txt")

# Open .txt file
    f = open(file_path,'w', encoding="utf8")


# Read each row of data from CSV file and tally votes
    for row in csvreader:
        sum_votes += 1
        candidate = str(row[2])
        candidate_data[candidate] = candidate_data[candidate] + 1

# Sort dictionary by decending vote count
desc_candidate_data = dict(sorted(candidate_data.items(), key=lambda x: (x[1]), reverse=True))
           
# Print report header and total votes
print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {total_votes:,}")
print("-----------------------------------")

# Write Report Header and Total Votes to text file
f.write("Election Results")
f.write("\n")
f.write("-----------------------------------")
f.write("\n")
f.write(f"Total Votes: {total_votes:,}")
f.write("\n")
f.write("-----------------------------------")
f.write("\n")

# Print election results  and write election results to .txt file
for x in desc_candidate_data:
    name = str(x)
    votes = int(desc_candidate_data[x])
    percent_votes = round((votes/sum_votes)*100)
    print(f"{name}: {percent_votes}.000% ({votes:,})")
    f.write(f"{name}: {percent_votes}.000% ({votes:,})")
    f.write("\n")
    if votes > greatest_vote:
        greatest_vote = votes
        winner = str(x)

print("-----------------------------------")
f.write("-----------------------------------")


# Print winner and write to .txt file 
print(f"Winner: {winner}")
print("-----------------------------------")
f.write("\n")
f.write(f"Winner: {winner}")
f.write("\n")
f.write("-----------------------------------")

 # Close .txt file
f.close()