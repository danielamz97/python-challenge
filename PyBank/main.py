# Import necessary libraries
import csv
import os

# Define the path to the input CSV file
file_path_data = os.path.join('.', 'Resources', 'budget_data.csv')

# Open the input CSV file for reading
with open(file_path_data) as PyBank_file:
    # Create a CSV reader object to iterate through the CSV data
    csv_iterable = csv.reader(PyBank_file)
    
    # Read and store the header row
    header = next(csv_iterable)
    
    # Initialize variables to keep track of financial data
    total_months = 0
    total = 0
    prev_row = None
    total_change = 0
    g_change = 0
    l_change = 0

    # Iterate through each row in the CSV data
    for row in csv_iterable:
        # Count the total number of months
        total_months = total_months + 1
        
        # Calculate the total profit/loss
        total = total + int(row[1])

        # Convert profit/loss to a floating-point number for change calculations
        pl = float(row[1])
        
        # Calculate the change in profit/loss compared to the previous month
        if prev_row is not None:
            prev_pl = float(prev_row[1])
            change = pl - prev_pl

            # Track the greatest increase and decrease in profits
            if change >= g_change:
                g_change = change
                g_change_month = row[0]
            if change <= l_change:
                l_change = change
                l_change_month = row[0]

            # Accumulate total change for later calculation
            total_change = total_change + change

        # Store the current row as the previous row for the next iteration
        prev_row = row

    # Print the financial analysis summary
    print(f'Financial Analysis\n----------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${total}')
    
    # Calculate and print the average change (excluding the first month)
    av_change = total_change / (total_months - 1)
    print(f'Average Change: ${av_change:.2f}')

    # Print the greatest increase and decrease in profits
    print(f'Greatest Increase in Profits: {g_change_month} (${int(g_change)})')
    print(f'Greatest Decrease in Profits: {l_change_month} (${int(l_change)})')

    # Define the path to the output text file for analysis results
    file_path_analysis = os.path.join('.', 'analysis', 'PyBank_analysis.txt')

    # Open the output text file for writing
    with open(file_path_analysis, 'w') as PyBank_analysis:
        # Write the financial analysis summary to the output file
        PyBank_analysis.write(f'Financial Analysis\n----------------------------\nTotal Months: {total_months}\nTotal: ${total}\nAverage Change: ${av_change:.2f}\nGreatest Increase in Profits: {g_change_month} (${int(g_change)})\nGreatest Decrease in Profits: {l_change_month} (${int(l_change)})')
