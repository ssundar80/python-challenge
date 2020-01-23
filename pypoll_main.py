#Import the os module
import os
#Module for reading CSV files
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
#Reading using CSV module
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Read the header row
    #csv_header = next(csvreader)
    #print(f"csv header: {csv_header}")
    #Skip the header row
    row = next(csvreader)
    #Store variables
    total_votes = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
#Read each row in row[0] of data after the header
    for row in csvreader:
        #total number of votes cast
        total_votes += 1
        #total number of votes cast for Khan
        if row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        elif row[2] == "O'Tooley":
            otooley_votes += 1
    khan_pct = round(khan_votes/total_votes * 100,2)
    correy_pct = round(correy_votes/total_votes * 100,2)
    li_pct = round(li_votes/total_votes * 100,2)
    otooley_pct = round(otooley_votes/total_votes * 100,2)
    #Create Lists to store values
    candidates = ["Khan", "Correy", "Li", "O'Tooley"]
    total_pct = [khan_pct, correy_pct, li_pct, otooley_pct]
    #zip the lists candidates and total_pct into a dictionary
    canidates_total_pct = dict(zip(candidates, total_pct))
    #Use the max and get functions to find the max winning vote percent in the zipped dictionary for candidates_total_pct
    winner = max(canidates_total_pct, key=canidates_total_pct.get)
#Print out the results        
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
print(f"Khan: {khan_pct}% ({khan_votes})")
print(f"Correy: {correy_pct}% ({correy_votes})")
print(f"Li: {li_pct}% ({li_votes})")
print(f"O'Tooley: {otooley_pct}% ({otooley_votes})")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")
    
#Output a txt file
with open('election_data.txt', "w") as text:
    text.write("Election Results")
    text.write("--------------------------")
    text.write(f"Total Votes: {total_votes}")
    text.write("--------------------------")
    text.write(f"Khan: {khan_pct}% ({khan_votes})")   
    text.write(f"Correy: {correy_pct}% ({correy_votes})")
    text.write(f"Li: {li_pct}% ({li_votes})")
    text.write(f"O'Tooley: {otooley_pct}% ({otooley_votes})")
    text.write("--------------------------")
    text.write(f"Winner: {winner}")
    text.write("--------------------------")