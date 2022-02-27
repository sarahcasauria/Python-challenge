#First import modules
import os
import csv

#Grab file path
pyroll_csv = os.path.join('Resources','election_data.csv')

#With open function to read the csv
with open (pyroll_csv, encoding='utf-8') as csvfile:
    pyroll_csv_reader = csv.reader(csvfile, delimiter = ',')
    # print('--------------------------------')
    # print(pyroll_csv_reader)
    #Skip reading the header
    next(pyroll_csv_reader, None)
    
#--------------------------
#----DEFINING VARIABLES----
#--------------------------    
    
    #Create a list to store the votes (using ballot ID in this case)
    vote_count = []
    
    #Define list to store candidates
    candidates_list = []
    
    #Create dictionary to store the candidates as keys and their votes as values
    each_candidate_votes = {}

#---PRINT OUTPUT TITLE----
    print('Election Results')
    print('--------------------------------------------')

    for row in pyroll_csv_reader:
        
#-------------------
#----TOTAL VOTES----
#-------------------
        #Append this vote ID to the vote count list
        vote_count.append(row[0])
        
        #Create variable to store total count of votes
        total_votes = int(len(vote_count))
        
#--------------------------
#----LIST OF CANDIDATES----
#--------------------------
        
        #Define the current candidate for the row
        current_candidate = row[2]
        
        #To create list of candidates, only append list if current row candidate is NOT already in the list
        if current_candidate not in candidates_list:
            candidates_list.append(current_candidate)

#-----------------------------
#----CANDIDATES VOTE COUNT----
#-----------------------------
            #When a new candidate is added to the list as above, we now make the candidate name the key in the dictionary by putting it in square brackets.
            #Make their vote count value start at zero.
            each_candidate_votes[current_candidate]=0
            
        #For every row in the csv, overwrite the row candidate's vote count by 1 each time. 
        #Since the candidate has already been defined in the dictionary, it will just keep adding to the previous loop value by overwriting previous value.
        each_candidate_votes[current_candidate]+=1
    
#----PRINT TOTAL NUMBER VOTES----
    print(f'Total number of votes cast: {total_votes} votes')
    # print('-----------------------------------')
    # print(candidates_list)
    # print(each_candidate_votes)

#--------------------------   
#----FINDING THE WINNER----
#--------------------------
    
    #Predefine winner variables and set as zero
    winner_vote_count =0
    winner_name = str()

    print('--------------------------------------------')
    #Using the candidate dictionary as a loop...
    for each_candidate in each_candidate_votes:
        
        #Calculate each candidate percentage of votes over total votes to two decimal places
        candidate_percentage = "{:.2f}".format(each_candidate_votes[each_candidate] / total_votes * 100.00)
        
#----PRINT EACH CANDIDATE IN LOOP WITH PERCENTAGE OF VOTES AND NUMBER OF VOTES----
        print(f'{each_candidate}: {candidate_percentage}% ({each_candidate_votes[each_candidate]})')
        
        #Find the winner. If number of votes for current each_candidate loop is larger than winner_vote_count...
        if each_candidate_votes[each_candidate] > winner_vote_count:
            
            #Replace winner_vote_count with the vote counts for the current candidate in loop and replace winner name with the key
            winner_vote_count = each_candidate_votes[each_candidate]
            winner_name = each_candidate
            
#----PRINT WINNER----
    print('--------------------------------------------')
    print(f'Winner: {winner_name} with {winner_vote_count} votes')
    print('--------------------------------------------') 

#-------------------------        
#----WRITE TO TXT FILE----
#-------------------------
with open('analysis/pyroll_output_file.txt', 'w', encoding = 'utf-8') as f:
    f.write("Election Results\n" + "--------------------\n" + 
                "Total Number of Votes Cast: " + str(total_votes) + "\n" +
                "--------------------\n")
    for each_candidate in each_candidate_votes:
        #Calculate each candidate percentage of votes over total votes to two decimal places.
        #Have to calculate the percentage again because for some reason was only saying 3.14% for each candidate.
        candidate_percentage = "{:.2f}".format(each_candidate_votes[each_candidate] / total_votes * 100.00)
        f.write(f'{each_candidate}: {candidate_percentage}% ({each_candidate_votes[each_candidate]})\n')
                
    f.write("--------------------\n" +
            "Winner: " + winner_name + " with " + str(winner_vote_count) + " votes.\n" +
            "--------------------\n")
    f.close()

        
    