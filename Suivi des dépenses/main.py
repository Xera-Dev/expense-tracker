expenses = []

def add_expense(amount, category):
    expenses.append((amount, category))
    print("Expense added successfully!")

def display_expenses():
    print("Expenses:")
    for amount, category in expenses:
        print(f"{category}: ${amount}")

def calculate_total_expenses():
    total = sum(amount for amount, _ in expenses)
    print(f"Total expenses: ${total}")

def add_budget(budget):
    expenses.append((budget))
    print("Votre budget est défini à", budget)
    
    
# Fonction pour exécuter le programme
def main():
    while True:
        print("\n1. Add Expense")
        print("2. Display Expenses")
        print("3. Calculate Total Expenses")
        print("4. Add Budget")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            add_expense(amount, category)
        elif choice == "2":
            display_expenses()
        elif choice == "3":
            calculate_total_expenses()
        elif choice == "4":
            budget = float(input("Enter the budget:")
            add_budget(budget)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
