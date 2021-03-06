# add our dependencies
import csv
import os

#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to same the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter.
total_votes = 0

#New list for candidates names called candidaate_options
candidate_options = []

#Open the election results and read the file.
with open(file_to_load) as election_data:
        file_reader = csv.reader(election_data)

        #read the header row.
        headers = next(file_reader)

        #print each row in the CSV file.
        for row in file_reader:
            #2 add to the total vote count.
            total_votes += 1

            #print the candidate name for each row.
            candidate_name = row[2]

            #if the candidate does not match any existing candidate...
            if candidate_options not in candidate_options:
                    #add it to the list of candidates.
                    candidate_options.append(candidate_name)

            #add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

#3 print candidate list.
print (candidate_options)

