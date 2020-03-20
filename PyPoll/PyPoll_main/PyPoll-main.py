#Import modules/Dependencies
import os
import csv

#Set path for file
csvpath = os.path.join("..", "Resources", "election_data.csv")

#Variables
total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0

#Open and Read csv file
with open(csvpath) as file:

    #CSV reader Specifications
    csvreader = csv.reader(file, delimiter=",")

    #Read the header Row
    csv_header = next(csvreader)
    row = next(csvreader)

    total_votes += 1
    Khan_votes +=1

    #Read the each row
    for row in csvreader:

        #Calculate total  votes
        total_votes += 1

        #Calculate total number of votes each candidate won
        if (row[2] == "Khan"):
            Khan_votes += 1
        elif (row[2] == "Correy"):
            Correy_votes += 1
        elif (row[2] == "Li"):
            Li_votes += 1
        else:
            OTooley_votes += 1 

    #Calculate Percentage of votes for each candidate
    Khan_Percent = (Khan_votes / total_votes) * 100
    Correy_Percent = (Correy_votes / total_votes) * 100
    Li_Percent = (Li_votes / total_votes) * 100
    OTooley_Percent = (OTooley_votes / total_votes) * 100

    #Calculate the winner
    Winner = max(Khan_votes, Correy_votes, Li_votes, OTooley_Percent)
    
    if Winner == Khan_votes :
        Winner_name = "Khan"
    elif Winner == Correy_votes :
        Winner_name = "Correy"
    elif Winner == Li_votes :
        Winner_name = "Li"
    else:
        Winner_name = "O'Tooley"

#Print Analysis
print("Election Results")  
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: {Khan_Percent:.3f}% ({Khan_votes})")
print(f"Correy: {Correy_Percent:.3f}% ({Correy_votes})")
print(f"Li: {Li_Percent:.3f}% ({Li_votes})")
print(f"O'Tooley: {OTooley_Percent:.3f}% ({OTooley_votes})")
print("-------------------------")
print(f"Winner: {Winner_name}")
print("-------------------------")

output_file = os.path.join("election_data_Output.text")


with open(output_file, "w") as textfile:

    textfile.write("Election Results\n")  
    textfile.write("-------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Khan: {Khan_Percent:.3f}% ({Khan_votes})\n")
    textfile.write(f"Correy: {Correy_Percent:.3f}% ({Correy_votes})\n")
    textfile.write(f"Li: {Li_Percent:.3f}% ({Li_votes})\n")
    textfile.write(f"O'Tooley: {OTooley_Percent:.3f}% ({OTooley_votes})\n")
    textfile.write("-------------------------\n")
    textfile.write(f"Winner: {Winner_name}\n")
    textfile.write("-------------------------\n")