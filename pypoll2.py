import os

# open a direct path to the file Resources/election_results.csv
# assign a variable for the ile to load and the path
file_to_load = 'Resources/election_results.csv'

# # #THIS Does NOT WORK
# with open(file_to_load) as election_data:

# #to do: perform analysis
#     print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World")




