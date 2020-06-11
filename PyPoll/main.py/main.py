# import modules for csv reader and operating system interaction

import os
import csv

#create lists for candidate list, candidate total results and candidate voting data
unique_candidate = []
results = []
candidate_results = []


total_votes_1 = 0
total_votes_2 = 0
total_votes_3 = 0
total_votes_4 = 0
highest_votes = 0

# Path to collect data from the Resources folder
election_csv = os.path.join('..', 'Resources', 'election_data.csv')

# Read in the CSV file
with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # ignore the 1st row
    header = next(csvreader)

    for row in csvreader:
        # set csv index for candidate and votes
        candidate = str(row[2])
        votes = int(row[0])

        # write unique candidates to list  
        if candidate not in unique_candidate:
            unique_candidate.append(candidate)
        
        #update lists  
        results.append(votes)
        results.append(candidate)

#tally votes by candidate    
for i in range (1,len(results)):
    if results[i] == unique_candidate[0]:
        total_votes_1 = total_votes_1 + 1
    elif results[i] == unique_candidate[1]:
        total_votes_2 = total_votes_2 + 1
    elif results[i] == unique_candidate[2]:
        total_votes_3 = total_votes_3 + 1
    elif results[i] == unique_candidate[3]:
        total_votes_4 = total_votes_4 + 1

# write total vote counts to a list
candidate_results.append(total_votes_1)
candidate_results.append(total_votes_2)
candidate_results.append(total_votes_3)
candidate_results.append(total_votes_4)

# find highest votes
winner_index = candidate_results.index(max(candidate_results))
winner = unique_candidate [winner_index]

# print report
total_votes = len(results)/2

print("\nElection Results")
print("----------------------------")
print(f"Total votes: {total_votes:.0f}")
print("----------------------------")
print(f"{unique_candidate[0]}: {total_votes_1/total_votes*100:.3f}% ({total_votes_1})")
print(f"{unique_candidate[1]}: {total_votes_2/total_votes*100:.3f}% ({total_votes_2})")
print(f"{unique_candidate[2]}: {total_votes_3/total_votes*100:.3f}% ({total_votes_3})")
print(f"{unique_candidate[3]}: {total_votes_4/total_votes*100:.3f}% ({total_votes_4})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------\n")

# write report
# write report
report_path = os.path.join('..', 'Analysis',"Analysis.txt")

my_file = open(report_path, 'w')

my_file.write("Election Results")
my_file.write("\n----------------------------")
my_file.write(f"\nTotal votes: {total_votes:.0f}")
my_file.write("\n----------------------------")
my_file.write(f"\n{unique_candidate[0]}: {total_votes_1/total_votes*100:.3f}% ({total_votes_1})")
my_file.write(f"\n{unique_candidate[1]}: {total_votes_2/total_votes*100:.3f}% ({total_votes_2})")
my_file.write(f"\n{unique_candidate[2]}: {total_votes_3/total_votes*100:.3f}% ({total_votes_3})")
my_file.write(f"\n{unique_candidate[3]}: {total_votes_4/total_votes*100:.3f}% ({total_votes_4})")
my_file.write("\n----------------------------")
my_file.write(f"\nWinner: {winner}")
my_file.write("\n----------------------------")
