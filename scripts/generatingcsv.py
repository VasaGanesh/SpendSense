import pandas as pd
import random
from datetime import timedelta, datetime

# Define categories and descriptions for income and expenses
expense_categories = ["Groceries", "Rent", "Utilities", "Entertainment", "Transportation", "Dining", "Healthcare",
                      "Insurance", "Education", "Miscellaneous"]
income_categories = ["Salary", "Freelancing", "Investments", "Rental Income"]
expense_descriptions = ["Weekly groceries", "Monthly rent", "Electricity bill", "Movie tickets", "Bus fare",
                        "Dinner out", "Doctor's visit", "Car insurance", "Online course", "Miscellaneous expense"]
income_descriptions = ["Monthly salary", "Freelance payment", "Investment returns", "Rental property income"]

# Generate 100+ records with random dates and amounts
start_date = datetime(2024, 1, 1)
data = {
    "Date": [],
    "Category": [],
    "Amount": [],
    "Description": [],
    "Type": []
}

for i in range(120):
    # Randomly decide if it's an income or expense
    trans_type = random.choice(["Income", "Expense"])

    if trans_type == "Expense":
        category = random.choice(expense_categories)
        description = random.choice(expense_descriptions)
        amount = round(random.uniform(20.0, 2000.0), 2)  # Random expense amount
    else:
        category = random.choice(income_categories)
        description = random.choice(income_descriptions)
        amount = round(random.uniform(500.0, 5000.0), 2)  # Random income amount

    # Append data to lists
    data["Date"].append(start_date + timedelta(days=i))
    data["Category"].append(category)
    data["Amount"].append(amount)
    data["Description"].append(description)
    data["Type"].append(trans_type)

# Create DataFrame
df_transactions = pd.DataFrame(data)

# Save to CSV file
csv_file_path = 'finance_data_100_with_type.csv'
df_transactions.to_csv(csv_file_path, index=False)

print(f"CSV file '{csv_file_path}' generated successfully.")
