name = input("Enter your name: ")
starting_budget = int(input("Whats your starting budget: "))
expenses = {}
while True:
    item = input("Enter your expense (type 'done' to stop):" ).strip()
    if item.lower() == "done":
        break
    amount = int(input(f"Enter amount for {item}: "))
    expenses[item] = amount 

total_expenses = sum(expenses.values())
rem_budget = starting_budget - total_expenses

if len(expenses) == 0:
    average_expenses = "No expense was entered"
    most_expensive_expense = "None"
    most_expensive_amount = "None"
else:
    average_expenses = total_expenses / len(expenses)
    most_expensive_expense = max(expenses, key=expenses.get)
    most_expensive_amount = expenses[most_expensive_expense]
print("========== EXPENSE TRACKER ==========")
print(f"Name: {name}")
print(f"Starting Budget: ₦{starting_budget}")
print(expenses)
print(f"Total expenses: ₦{total_expenses}")
print(f"Remaining Budget: ₦{rem_budget}")
print(f"Average expenses: ₦{average_expenses}")
print(f"The most expensive expense: {most_expensive_expense}: {most_expensive_amount}")

