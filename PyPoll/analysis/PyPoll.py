# Import the module for reading CSV
import csv

import os

# Files to load and output
csvpath = os.path.join('Resources', 'election_data.csv')

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

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # Set month counter and winner vote count
    total_votes = 0
    greatest_vote_total = 0

# Set Path for Text File
    file_path = os.path.join("analysis","PyPoll.txt")

# Open Text File
    f = open(file_path,'w', encoding="utf8")


# Read each row of data from CSV file and tally votes
    for row in csvreader:
        sum_votes += 1
        candidate = str(row[2])
        candidate_data[candidate] = candidate_data[candidate] + 1

# Sort Dictionary by Decending Vote Count
desc_candidate_data = dict(sorted(candidate_data.items(), key=lambda x: (x[1]), reverse=True))
           
# Print Report Header and Total Votes to Terminal

print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {total_votes:,}")
print("-----------------------------------")

# Write Report Header and Total Votes to Text File

f.write("Election Results")
f.write("\n")
f.write("-----------------------------------")
f.write("\n")
f.write(f"Total Votes: {total_votes:,}")
f.write("\n")
f.write("-----------------------------------")
f.write("\n")

# Print Election Results to Terminal and Write Election Results to Text File

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


# Print Winner to Terminal and Write Winner to Text File 

print(f"Winner: {winner}")
print("-----------------------------------")
f.write("\n")
f.write(f"Winner: {winner}")
f.write("\n")
f.write("-----------------------------------")

 # Close Text File

f.close()