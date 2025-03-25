from datetime import datetime
import csv
from idlelib.pyparse import trans
from random import choice

from unicodedata import category

CSV_FILE='finance_data_100_with_type.csv'

def initialize_csv():
    try:
        with open(CSV_FILE,'r') as file:
            pass
    except FileNotFoundError:
        with open(CSV_FILE,'w',newline='') as file:
            writer=csv.writer(file)
            writer.writerow(['Date','Category','Amount','Description','Type'])

def add_transaction(date,category,amount,description,type):
    with open(CSV_FILE,'a',newline='')as file:
        writer=csv.writer(file)
        writer.writerow([date,category,amount,description,type])

def date_str_validate():
    """
    Validate date format from user's input
    """
    while True:
        date = input("Enter the date (YYYY-MM-DD) or 'today': ")
        if (date == 'today' or date == 'Today'):
            date = datetime.date.today()
            break
        try:
            date = datetime.date.fromisoformat(date)
            break
        except:
            print("Incorrect data format, should be YYYY-MM-DD")
            continue
    return date

def main():
    print("Personal Finance tracker")
    print("Options: [1] Add Transaction [2] Exit")

    while True:
        choice=int(input("Enter your choice: "))
        if choice==1:
            date=date_str_validate()
            category=int("Enter category ")
            amount=float(input("Enter amount :"))
            desc=input("Enter the description")
            trans_type=input("Enter type(Income/expense)")
            add_transaction(date,category,amount,desc,trans_type)
            print("Transcation added successfully")
        elif choice=='2':
            print("Exiting program..")
            break
        else:
            print("Invalid choice, please try again")
if __name__=="__main__":
    initialize_csv()
    main()




