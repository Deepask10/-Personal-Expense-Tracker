import csv
import os
from datetime import datetime


CSV_FILE = "expenses.csv"


# Create CSV file if it does not exist
def create_csv_file():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


# Add a new expense
def add_expense():
    print("\n===== Add Expense =====")

    date = input("Enter date (YYYY-MM-DD): ")

    # Validate date
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    category = input("Enter category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    description = input("Enter description: ").strip()

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("Expense added successfully!")


# View all expenses
def view_expenses():
    print("\n===== All Expenses =====")

    with open(CSV_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        expenses = list(reader)

        if not expenses:
            print("No expenses found.")
            return

        print("-" * 75)
        print(f"{'Date':<15}{'Category':<15}{'Description':<25}{'Amount':>10}")
        print("-" * 75)

        for expense in expenses:
            print(
                f"{expense['Date']:<15}"
                f"{expense['Category']:<15}"
                f"{expense['Description']:<25}"
                f"{float(expense['Amount']):>10.2f}"
            )

        print("-" * 75)


# Filter expenses by category
def filter_expenses():
    print("\n===== Filter Expenses =====")

    category = input("Enter category to filter: ").strip().lower()

    with open(CSV_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        found = False

        print("-" * 75)
        print(f"{'Date':<15}{'Category':<15}{'Description':<25}{'Amount':>10}")
        print("-" * 75)

        for expense in reader:
            if expense["Category"].lower() == category:
                found = True

                print(
                    f"{expense['Date']:<15}"
                    f"{expense['Category']:<15}"
                    f"{expense['Description']:<25}"
                    f"{float(expense['Amount']):>10.2f}"
                )

        print("-" * 75)

        if not found:
            print("No expenses found for this category.")


# Category summary
def category_summary():
    print("\n===== Category Summary =====")

    summary = {}

    with open(CSV_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            category = expense["Category"]
            amount = float(expense["Amount"])

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    if not summary:
        print("No expenses found.")
        return

    print("-" * 40)
    print(f"{'Category':<25}{'Total':>10}")
    print("-" * 40)

    grand_total = 0

    for category, total in summary.items():
        print(f"{category:<25}{total:>10.2f}")
        grand_total += total

    print("-" * 40)
    print(f"{'Grand Total':<25}{grand_total:>10.2f}")


# Main menu
def main():
    create_csv_file()

    while True:
        print("\n================================")
        print("     PERSONAL EXPENSE TRACKER")
        print("================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter by Category")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            filter_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("Thank you for using Personal Expense Tracker!")
            break

        else:
            print("Invalid choice. Please select 1 to 5.")


if __name__ == "__main__":
    main()