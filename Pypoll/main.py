# Initialize CSV module and CSV files
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Initialize variables

total_votes = 0
candidates = {}
winner_name = ""
winner_votes = 0

# Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    header = next(csvreader)

    # Calculate the votes and winner
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name in candidates:
                candidates[candidate_name] += 1
        else:
                candidates[candidate_name] = 1

        if candidates[candidate_name] > winner_votes:
                winner_name = candidate_name
                winner_votes = candidates[candidate_name]

# Print election analysis results
print("")
print("-------------------------")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print(f"Winner: {winner_name}")

# Write election analysis results to a text file
output_path = os.path.join('Analysis', "election_results.txt")
with open(output_path, "w") as text_file:
    text_file.write("-------------------------\n")
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        text_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    text_file.write(f"Winner: {winner_name}\n")
    
print("")
print("Results exported to election_results.txt")
