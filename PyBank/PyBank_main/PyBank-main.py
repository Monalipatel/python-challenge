#Import Modules/Dependencies
import os
import csv

#Set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

#Variables
total_months = 0
total_amount =0
monthly_change = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

#Open and Read csv file
with open(csvpath) as file:

     #CSV reader Specifications
    csvreader = csv.reader(file, delimiter=",")

    #Read the header Row
    csv_header = next(csvreader)
    row = next(csvreader)

    previous_row = int(row[1])
    total_months += 1
    total_amount += int(row[1])
    
    #Read the each row
    for row in csvreader:
        
        # Calculate Total Number Of Months Included In Dataset
        total_months += 1

        # Calculate Net Amount Of "Profit/Losses"
        total_amount += int(row[1])

        # Calculate Change From Current Month To Previous Month
        change = int(row[1])- previous_row
        monthly_change.append(change)
        previous_row = int(row[1])

        # Calculate The Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        # Calculate The Greatest Decrease
        if int(row[1]) < greatest_decrease:
             greatest_decrease = int(row[1])
             greatest_decrease_month = row[0]

    # Calculate The Average & The Date
    Average_change = sum(monthly_change)/len(monthly_change)

    highest = max(monthly_change)
    lowest = min(monthly_change)

#Print Analysis
print("Financial Analysis")  
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average  Change: ${Average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${highest})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${lowest})")

output_file = os.path.join("budget_data_output.text")


with open(output_file, "w") as textfile:

    textfile.write("Financial Analysis\n")  
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total_amount}\n")
    textfile.write(f"Average  Change: ${Average_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${highest})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${lowest})\n")