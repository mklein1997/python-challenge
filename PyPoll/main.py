# Import modules
import os 
import csv

#Set path for csv read
csvpath = os.path.join("/Users/Michael/Documents/GT DA/python-challenge/PyPoll/Resources/election_data.csv")

# Define headers
voterid = []
county = []
candidate = []
# Read file
with open (csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header
    header = next(csvreader)
    
    # append columns
    for row in csvreader:

        voterid.append(float(row[0]))

        county.append(row[1])

        candidate.append(row[2])

# Total number of votes cast
totalvotes = (len(voterid))

#List of who received votes can be provided by using a set for candidate column

# Vote totals 
candidatelist = list(candidate)
correyvotes = candidatelist.count('Correy')
khanvotes = candidatelist.count('Khan')
livotes = candidatelist.count('Li')
otvotes = candidatelist.count("O'Tooley")

print(correyvotes)

# Vote percentages
cpercentage = correyvotes/totalvotes
kpercentage = khanvotes/totalvotes
lpercentage = livotes/totalvotes
opercentage = otvotes/totalvotes

# Format returns to display properly as percentages
cformat = "{:.0%}".format(cpercentage)
kformat = "{:.0%}".format(kpercentage)
lformat = "{:.0%}".format(lpercentage)
oformat = "{:.0%}".format(opercentage)

# Find winner

votecounts = {correyvotes, khanvotes, livotes, otvotes}
winner = max(votecounts)

# Print output
print("Election Results")
print("-------------------")
print(f"Total Votes Cast: {totalvotes}")
print("-------------------")
print(f"Khan: {kformat} ({khanvotes})")
print(f"Correy: {cformat} ({correyvotes})")
print(f"Li: {lformat} ({livotes})")
print(f"O'Tooley: {oformat} ({otvotes})")
print("-------------------")
print(f"Winner: Khan with {winner} votes")


# Print results to text file
output = os.path.join("/Users/Michael/Documents/GT DA/python-challenge/PyPoll/Analysis/electionresults.txt")

output = open(r"electionresults.txt", "w")

output.write("Election Results\n Total Votes Cast: 3521001\n Khan: 63% (2218231)\n Correy: 20% (704200)\n Li: 14% (492940)\n O'Tooley: 3% (105630)\n Winner: Khan with 2218231 votes.")
output.close()

   
