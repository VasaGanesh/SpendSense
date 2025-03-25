import pandas as pd
import matplotlib.pyplot as pt
import seaborn as sns

CSV_FILE='finance_data_100_with_type.csv'

# Function to load data from CSV
def load_data():
    return pd.read_csv(CSV_FILE)

def summarize_data(df):
    total_income = df[df['Type'] == 'Income']['Amount'].sum()
    total_expense = df[df['Type'] == 'Expense']['Amount'].sum()
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expense}")
    print(f"Net Savings: {total_income - total_expense}")

# Function to visualize expenses by category
def plot_expenses_by_category(df):
    expense_data = df[df['Type'] == 'Expense']
    sns.barplot(x='Category', y='Amount', data=expense_data, estimator=sum)
    pt.title('Total Expenses by Category')
    pt.xticks(rotation=45)
    pt.show()

# Function to visualize monthly income vs expenses
def plot_income_vs_expenses(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.to_period('M')

    income_vs_expense = df.groupby(['Month', 'Type'])['Amount'].sum().unstack().fillna(0)
    income_vs_expense.plot(kind='bar', stacked=True)
    pt.title('Monthly Income vs Expenses')
    pt.ylabel('Amount')
    pt.xticks(rotation=45)
    pt.show()

# Main function to run analysis and visualization
def main():
    df = load_data()

    # Display the summary
    summarize_data(df)

    # Visualize expenses by category
    plot_expenses_by_category(df)

    # Visualize monthly income vs expenses
    plot_income_vs_expenses(df)

if __name__ == "__main__":
    main()