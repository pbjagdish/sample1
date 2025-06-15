import csv
from datetime import datetime

FILENAME = "expenses.csv"

def load_expenses():
    try:
        with open(FILENAME, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(FILENAME, mode='w', newline='') as file:
        fieldnames = ["Date", "Category", "Description", "Amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Transport, etc.): ")
    description = input("Enter description: ")
    amount = input("Enter amount: ")

    expense = {
        "Date": date,
        "Category": category,
        "Description": description,
        "Amount": amount
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added successfully!")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp['Date']} | {exp['Category']} | {exp['Description']} | ₹{exp['Amount']}")
    print()

def filter_by_category():
    category = input("Enter category to filter: ").strip()
    expenses = load_expenses()
    filtered = [e for e in expenses if e['Category'].lower() == category.lower()]
    if not filtered:
        print("No expenses found in this category.")
        return
    print(f"\n--- Expenses in {category} ---")
    for exp in filtered:
        print(f"{exp['Date']} | {exp['Description']} | ₹{exp['Amount']}")
    print()

def monthly_summary():
    expenses = load_expenses()
    summary = {}
    for exp in expenses:
        month = exp['Date'][:7]  # YYYY-MM
        summary[month] = summary.get(month, 0) + float(exp['Amount'])
    print("\n--- Monthly Summary ---")
    for month, total in summary.items():
        print(f"{month}: ₹{total:.2f}")
    print()

def delete_expense():
    view_expenses()
    try:
        idx = int(input("Enter the number of the expense to delete: ")) - 1
        expenses = load_expenses()
        if 0 <= idx < len(expenses):
            deleted = expenses.pop(idx)
            save_expenses(expenses)
            print(f"Deleted: {deleted['Description']} - ₹{deleted['Amount']}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n==== Personal Expense Tracker ====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Monthly Summary")
        print("5. Delete an Expense")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            filter_by_category()
        elif choice == '4':
            monthly_summary()
        elif choice == '5':
            delete_expense()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

