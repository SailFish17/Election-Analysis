# Module 3.4.1
# Objectives  The data we need to retrieve
# 	Total number of votes cast
#	A complete list of candidates who received votes
#	Total number of votes each candidate received
#	Percentage of votes each candidate won
#	The winner of the election based on popular vote


#access the file  its referring to folder path and file name.
# Resources/election_results.csv

#notes on DEPENDENCIES
#dependancies are modules, packages or programming scripts that someone else has written that allow you to increase functional programming of your code, speed or efficiency.
#import the datetime class from the datetime module.
#2nd time doing this we changed the datetime module to show "as dt" then changed it in the variable sentence to match.
# import datetime as dt
# #use the now() attribute on teh datetime class to get to teh present time.
# now = dt.datetime.now()
# #Print the present time
# print("the time right now is ", now)


#notes on PACKAGES
#Packages are folders that contain a set of Python modules.  the folders in the packages may contain various subpackages, or other folders.   Use the "import" statement to get them.

#Notes on MODULES
#Modules are separate sofware files, usually with a .py extension.  seems to be like a big macro.
#To use a specific function, class, or variable from a module, you use a statement like "from import".
#there is a csv module!


# open a direct path to the file Resources/election_results.csv
# assign a variable for the ile to load and the path
file_to_load = 'Resources/election_results.csv'
# file_to_load = election_data
import os

# #open the election results and read the file.
# #using the With statement to open() and close()
# election_data = open(file_to_load, 'r')
# # # To do: perform analysis.
# # # Close the file.
# election_data.close()

#use of the with statement
# #THIS DID NOT WORK
with open(file_to_load) as election_data:

#to do: perform analysis
    print(election_data)
    
# #close the file
election_data.close()


# #load a indirect path file
# #use os module
# #also DID NOT WORK.  May be file issue?
# import csv
# import os
# #talked with tech and she tested by adding a loop below.  Set the variable to zero.
# total_votes=0
# # #asssign variable for the file to load and the path
# file_to_load = os.path.join("resources", "election_results.csv")
# #open the election results and read the file.
# with open(file_to_load) as election_data:
#     reader=csv.reader(election_data)

    #print the file object.
#    print(election_data)
# # this is the loop the tech had me add to test if we were reading the file.  we were.  Just can't print the line above this one.
#     for row in reader:
#         total_votes+=1
# print(total_votes)

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")

# Close the file
# outfile.close()