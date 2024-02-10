import json

# Charger les données de dépenses à partir d'un fichier s'il existe
try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = {}

def add_expense(amount, category):
    if category in expenses:
        expenses[category].append(amount)
    else:
        expenses[category] = [amount]
    print("Expense added successfully!")
    save_expenses()

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

def display_expenses():
    print("Expenses:")
    for category, amounts in expenses.items():
        total_amount = sum(amounts)
        print(f"{category}: ${total_amount}")

def calculate_total_expenses():
    total = sum(sum(amounts) for amounts in expenses.values())
    print(f"Total expenses: ${total}")

def add_budget():
    if "Salary" not in expenses or "Invoice" not in expenses:
        print("Please set up your salary/invoice first.")
        return
        
    salary = expenses["Salary"][0]
    invoice = expenses["Invoice"][0]
    device = expenses["Device"][0]
    budget_total = salary - invoice
        
    budget_a = budget_total / 3
    budget_a_name = input(f"A quoi voulez vous destiner la premiere partie de votre budget({budget_a}{device}): ")
    expenses[f"Budget {budget_a_name}"] = [budget_a]
    print(f"Budget {budget_a_name} = {budget_a}")
        
    budget_b = budget_total / 3
    budget_b_name = input(f"A quoi voulez vous destiner la deuxieme partie de votre budget({budget_b}{device}): ")
    expenses[f"Budget {budget_b_name}"] = [budget_b]
    print(f"Budget {budget_b_name} = {budget_b}")

    budget_c = budget_total / 3
    budget_c_name = input(f"A quoi voulez vous destiner la derinière partie de votre budget({budget_c}{device}): ")
    expenses[f"Budget {budget_c_name}"] = [budget_c]
    print(f"Budget {budget_c_name} = {budget_c}")
    save_expenses()

def setup(device, salary, invoice):
    expenses["Device"] = [device]
    print(f"Your device is set to ${device}")
    expenses["Salary"] = [salary]
    print(f"Your salary is set to ${salary}")
    expenses["Invoice"] = [invoice]
    print(f"Your invoice is set to ${invoice}")
    save_expenses()

# Fonction pour exécuter le programme
def main():
    while True:
        print("\n0. Setup")
        print("1. Add Expense")
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
        elif choice == "0":
            device = input("Enter the device ( $ / £ / € ): ")
            salary = float(input("Enter your salary (for make special budget): "))
            invoice = float(input("Enter your invoice (for make special budget): "))
            setup(device, salary, invoice)
        elif choice == "3":
            calculate_total_expenses()
        elif choice == "4":
            add_budget()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
