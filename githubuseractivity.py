# Expense Tracker for Roadmap.sh Project

expenses_list = []


def add_expense():
    expense = {}
    expense['name'] = input("Enter the name of the expense: ")
    expense['amount'] = float(input("Enter the amount of the expense: "))
    expense['id'] = len(expenses_list) + 1  # Assign a new ID based on the current length of the list 
    expenses_list.append(expense)
    print(f"Expense '{expense['name']}' added successfully!")
    print(f"Expense ID: {expense['id']}, Amount: ${expense['amount']:.2f}")

def list_expenses():
    if not expenses_list:
        print("No expenses recorded.")
        return
    print("Expenses:")
    for i, expense in enumerate(expenses_list, start=1):
        print(f"{i}. {expense['name']}: ${expense['amount']:.2f}")

def delete_expense():
    if not expenses_list:
        print("No expenses to delete.")
        return
    else:
        index = int(input("Enter the ID of the expense to delete: "))
        for len in expenses_list:
            if index == expenses_list[index - 1]['id']:
                deleted_expense = expenses_list.pop(index - 1)
                print(f"Expense '{deleted_expense['name']}' deleted successfully!")
            else:
                print("Invalid ID. No expense deleted.")

def main():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. List Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            list_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
