# Import necessary libraries
import csv
import os

# Define the path to the input CSV file for election data
file_data_path = os.path.join(".", "Resources", "election_data.csv")

# Open the input CSV file for reading
with open(file_data_path) as PyPoll_file:
    # Create a CSV reader object to iterate through the CSV data
    voter_it = csv.reader(PyPoll_file)
    
    # Read and store the header row
    header = next(voter_it)
    
    # Initialize variables to store election data
    voter_count = 0  # Total number of votes
    candidates = {}  # Dictionary to store candidate names and their vote counts
    cand_string =''  # String to store the election results as text
    
    # Iterate through each row in the CSV data
    for voter in voter_it:
        # Count the total number of votes
        voter_count = voter_count + 1
        
        # Check if the candidate is already in the candidates dictionary
        if voter[2] not in candidates:
            new_candidate = voter[2]
            candidates[new_candidate] = 0  # Initialize the vote count for the new candidate
        
        # Increment the vote count for the candidate
        if voter[2] in candidates:
            candidates[voter[2]] = candidates[voter[2]] + 1
    
    # Calculate the percentage of votes each candidate received
    for cand, votes in candidates.items():
        percentage = (votes / voter_count) * 100
        candidates[cand] = [votes, percentage]  # Store vote count and percentage
        cand_string = f'{cand_string} {cand}: {percentage:.3f}% ({votes})\n'  # Format the results
    
    # Find the winner based on the candidate with the most votes
    winner = max(candidates, key=lambda cand_name: candidates[cand_name][0])
    
    # Print the election results to the console
    print(f'Election Results\n-------------------------')
    print(f'Total votes: {voter_count}')
    print(f'-------------------------')
    print(cand_string)
    print(f'-------------------------')
    print(f'Winner: {winner}')
    print(f'-------------------------')
    
    # Define the path to the output text file for analysis results
    file_path_analysis = os.path.join('.', 'analysis', 'PyPoll_analysis.txt')
    
    # Open the output text file for writing
    with open(file_path_analysis, 'w') as PyPoll_analysis:
        # Write the election analysis summary to the output file
        PyPoll_analysis.write(f'Election Results\n-------------------------\n')
        PyPoll_analysis.write(f'Total votes: {voter_count}\n')
        PyPoll_analysis.write(f'-------------------------\n')
        PyPoll_analysis.write(cand_string)
        PyPoll_analysis.write(f'-------------------------\n')
        PyPoll_analysis.write(f'Winner: {winner}\n')
        PyPoll_analysis.write(f'-------------------------')