# Initialize CSV module and CSV files
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
total_months = 0
net_profit_loss = 0
previous_profit_loss = None
changes = []
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

# Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    header = next(csvreader)

    # Extract date and profit/loss    
    for row in csvreader:
        date = row[0]
        profit_loss = int(row[1])
        
        # Calculate total number of months
        total_months += 1
        
        # Calculate net total of profit/loss
        net_profit_loss += profit_loss
        
        # Calculate change in profit/loss
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            
            # Check for greatest increase and decrease
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change
        
        previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(changes) / len(changes)

# Print the financial analysis results
print("")
print("--------------------------")
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Export the financial analysis results to a text file
output_path = os.path.join('Analysis', 'financial_analysis.txt')
with open(output_path, "w") as text_file:
    text_file.write("--------------------------\n")
    text_file.write("Financial Analysis\n")
    text_file.write("--------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${net_profit_loss}\n")
    text_file.write(f"Average Change: ${average_change:.2f}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")

print("")
print("Results exported to financial_analysis.txt'")