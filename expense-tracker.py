
from expense import Expense
import calendar
import datetime

def main():
    print(f"Running Expense Tracker")
    expense_file_path = "expenses.csv"
    budget = 1000.00
    #1. user to input expense 
    expense = get_user_input_expense()
    #2. write the expense into a file
    save_expense_to_file(expense, expense_file_path)
    #3. read file and summarize expenses 
    summarize_expenses(expense_file_path, budget)
    

def get_user_input_expense():
    print(f" Getting User Expense")
    expense_name = input("Enter expense name : ")
    expense_amount = float(input("Enter amount : "))

    expense_categories = [
        "Food", "Home", "Work", "Fun", "Misc"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"  {i+1}.{category_name}")

        value_range = f"[1 - {len(expense_categories)}]"

        ## TODO : try catch block for non int entries
        selected_index = int(input(f"Enter a category nmber {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            new_expense = Expense(name=expense_name, category=expense_categories[selected_index], amount=expense_amount)
            return new_expense
        else:
            print("Enter a valid number")

##use hints by giving class name in args, editor suggests the variables
def save_expense_to_file(expense: Expense, expense_file_path):
    print(f" Save Expense to File : {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expenses(expense_file_path, budget):
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines: 
            expense_name, expense_amount, expense_category = line.strip().split(',')

            line_expense = Expense(name=expense_name, amount=float(expense_amount), category=expense_category)
            expenses.append(line_expense)
        
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    
    print("Expense Summary")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ₹{amount:.2f}")

    total_spent = sum([x.amount for x in expenses])
    remaining_budget = budget - total_spent
    print(f"You've spent this much amount : {total_spent:.2f} and Remaining budget is {remaining_budget:.2f}")

    #get remaining days in month
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    daily_budget = remaining_budget / remaining_days
    print(green(f"Budget Per Day: ₹{daily_budget:.2f}")) 

def green(text):
    return f"\033[92m{text}\033[0m"

## Run only when file is run directly and not with import
if __name__ == '__main__':
    main()