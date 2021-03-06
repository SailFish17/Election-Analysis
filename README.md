# Election-Analysis

## Purpose

A Colorado Board of Elections is worried that it will be sued by a candidate over the election results.   They have asked for a bullet proof code to audit the recent elections.  Public tension is rampent and the stakes are huge in the Mile High state.
The code should answer the following questions:

 1. Calculate the total number of votes cast.
 2. Get a complete list of candidates who received votes.
 3. Calculate the total number of votes each candidates received.
 4. Calculate the percentage of veotes each candidate won.
 5. Determine the winner of the election based on popular vote.

## Resources and Challenges

The code is written in Python 3.9.x with the use of VSCODE, an IDE by Microsoft.  Both of these resources proved to be completely unreliable and confounding despite significant help with the platforms.   Over 5 hours with the askBCS help group did not result in any appreciable change to known code problems and issues.  A complete computer rebuild is pending in order to review and ensure futher computational work is sound.  The code did spit out the results in the a txt file as asked but would not upload to GitHub until a further 2 hour session with the BCS helpdesk worked thru several problems that were encountered.

## Results:
The following analysis was output to the txt file.  The analysis the election show that:

  - There were 369,711 votes cast in the election.
    	
    - The candidates were:
     
      - Charles Casper Stockham
      - Diana DeGette
      - Raymon Anthony Doane
    
    - The candidate Results were:
     - Charles Casper Stockham recieved 23.0% of the votes and 85,213 number of votes.
     - Diana DeGette recieved 73.8% of the votes and 272,892 number of votes.
     - Raymon Anthony Doane recieved 3.1% of the votes and 11,606 number of votes. 
        
    - The winner of the election was:
        
        - Diana DeGetter who recieved 73.8% of the votes and 272,892 number of votes.

## Scope Creep
As is usual in these types of situations, scope creep was inevitable.  The Commission was fearful of the additional scrutiny due to the issues the code and platform had caused. The following information was requested to complete the audit:

6. The voter turnout for each county
7. The percentage of votes from each county out of the total count
8. the county with the highest turnout.

### Results of Scope Creep
The results returned for items 6-8 are:

The voter turnout for each county:

     - Jefferson had 10.5% of votes and 38,855 people voted.
      
     - Denver had 82.8% of votes and 306,055 people voted. 
      
     - Arapahoe had 6.7% of votes and 24,801 people voted.
      
The county with the highest turnout:
     
     -Denver had the highest voter turnout with 82.8% of votes which is equivalent to 306,055 voters.


## Summary and Analysis

Election-Audit Summary
•	The following script PyPoll_Challenge.py can be modified for use for any election.  

This can be done in two simple ways;  with the input() function and def my_function().   Changes made to the beginning of the script where the string file_1 = input ('file_1: ') and file_2 = input ('file_2: ') can be replaced by a with statement that has a syntax with open(file_1)as election_data and with open(file_2, "w") as txt_file, where file_1 is the file_to_load and file_2 is file_save.   The input function will generate an output in the terminal asking what is the location for file_to_load and file_to_save. 

The def my_function () can also be used generate other election data while using the same script. For example (def election_test(file_1, file_2):), change the (with) statements as we did with the input() function, can be used at the beginnging with the rest of the script below and at the end election_test("folder/election data", "folder/election data txt file").

The use of this code for other elections can be had on a SaaS basis with low market rates and a menu of ad hoc charges that should slowly siphon Opex budgets for years to come.  This income will of course be used to further refine the hardware, software and the code itself to delver complete and trustworthy election results for years to come.
