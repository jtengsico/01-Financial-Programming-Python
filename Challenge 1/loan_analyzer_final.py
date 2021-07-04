
# import the CSV library 
# imports are always at the top of code (formatting)
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.
Automate the calculations for the loan portfolio summaries."""

loan_costs = [500, 600, 200, 1000, 450]

# The number of loans in the list is below.
total_number_loans = len(loan_costs)
print(f"There total number of loans is: {total_number_loans}.") 

# The total value of the loans is below. 
sum_of_loans = sum(loan_costs)
print(f"The total value of the loans is: ${sum_of_loans}.")

#The average loan amount is below. 
average_loan_amount = sum_of_loans/total_number_loans
print(f"The average loan price is: ${average_loan_amount}.")



"""Part 2: Analyze Loan Data.
Analyze the loan to determine the investment evaluation."""

# Use the following loan data to calculate the present value for the loan.
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Get() was used on the dictionary to extract Future Value and Remaining Months on the loan. 
# Note about get(): Makes the code more efficient. 
future_value = loan.get("future_value") 
print(f"The future value is: {future_value}.")

remaining_months = loan.get("remaining_months")
print(f"The remaining months are: {remaining_months}.")
 
# The formula below for present value is used to calculate a "fair value" of the loan.
# The formula below uses a discount rate of 20%. 
discount_rate = 0.20 
present_value = future_value / (1+discount_rate/12)**remaining_months
print(f"The present value is: ${present_value:.2f}.")

# Present value equals what the loan is really worth ("fair value")
# If the present value is greater than or equal to the cost, then just buy the loan. 
# Else, if the present value of the loan is less than the cost (loan price), then do not buy the loan. 
if present_value >= loan.get("loan_price"):
    print("The loan is worth the cost. Just buy it.")
else:
    print("The loan is expensive and not worth the price!")



"""Part 3: Perform Financial Calculations.
Perform financial calculations using functions."""

# Using the following loan data, calculate present value. 
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# The function defines present value.
def calculate_present_value(future_value, annual_discount_rate, remaining_months):
    present_value = future_value / (1+annual_discount_rate/12)**remaining_months
    future_value = new_loan.get("future_value")
    remaining_months = new_loan.get("remaining_months")
    return present_value

# Calculate the present value of the new loan using an annual discount rate of 20% 
annual_discount_rate = 0.20
present_value_new_loan= calculate_present_value(new_loan["future_value"], annual_discount_rate, new_loan["remaining_months"])
print(f"The present value of the new loan is: ${present_value_new_loan:.2f}.")



"""Part 4: Conditionally filter lists of loans.
In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans."""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# An empty list 'inexpensive_loans' for adding values 
inexpensive_loans = [] 

# Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan_price in loans:
    if loan_price["loan_price"] <= 500:
        inexpensive_loans.append(loan_price)

# Print the `inexpensive_loans` list
print(inexpensive_loans)



"""Part 5: Save the results.
Output this list of inexpensive loans to a csv file."""

# Path to new CSV file
csvpath = Path("inexpensive_loans.csv")

# Header for CSV file
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Output path for the file
output_path = Path("inexpensive_loans.csv")

# Open the output CSV file path using `with open`
with open(csvpath, "w", newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)

    # Loop for dictionary values in 'inexpensive_loans' 
    # loop will add values to a row in the CSV file 
    for loan_price in inexpensive_loans:
        csvwriter.writerow(loan_price.values())


"""Note: Instructions for the challenge have been removed in order to increase readability of the code. """