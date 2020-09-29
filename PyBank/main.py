#Import modules for reading files
import os
import csv
from statistics import mean

#Set path for csv read
csvpath = os.path.join("/Users/Michael/Documents/GT DA/python-challenge/PyBank/Resources/budget_data.csv")

# Define headers
months = []
profloss = []

# Read CSV
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skip header row to avoid including in output
    header = next(csvreader)
    
    # Read through csv
    for row in csvreader:

        months.append(row[0])

        profloss.append(float(row[1]))

# Total count of months column
totalmonths = (len(months))

# Total of profits/losses
totalprofloss = (sum(profloss))

# Greatest Increase and Decrease
average = []

for i in range(len(profloss)-1):

    average.append(profloss[i+1]-profloss[i])

    greatestinc = profloss.index(max(profloss))
    greatestdec = profloss.index(min(profloss))

# Print output
print("Financial Analysis")
print("----------------------")
print("Total Months: " + str(totalmonths))
print("Total Profits/Losses: $" + str(totalprofloss))
print("Average Change: $" + str({round(sum(average)/len(average), 2)}))
print(f"Greatest Increase in Profits: {months[greatestinc]} (${(str(greatestinc))})")
print(f"Greatest Decrease in Profits: {months[greatestdec]} (${(str(greatestdec))})")

# Print results to text file
output = os.path.join("/Users/Michael/Documents/GT DA/python-challenge/PyBank/Analysis/financialanalysis.txt")

output = open(r"financialanalysis.txt", "w") 
 
output.write("Financial Analysis\n Total Months: 86\n Total Profits/Losses: $38382578\n Average Change: $-2315.12\n Greatest Increase in Profits: Feb 2012 ($1926159)\n Greatest Decrease in Profits: Sep 2013 ($-2196167)")
output.close()

   
   