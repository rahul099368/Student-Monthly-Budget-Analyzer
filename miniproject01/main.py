#Student monthly budget analyzer
std_name = input("enter student name:")
monthly_income = float(input("Enter monthly income(RS):"))
food_expense = float(input("Food expenses(RS):"))
travel_expense = float(input("Travel expenses(RS):"))
study_material_expense = float(input("Study materials(RS):"))
mobile_internet_expense = float(input("Mobile/internet expenses(RS):"))
other_expense = float(input("Other expenses(RS):"))
    

#implementation
print(f"\n-----MONTHLY BUDGET REPORT-----")
print(f"Student: {std_name}")
print(f"Monthly income: {monthly_income}")
print(f"Food expenses: {food_expense}")
print(f"Travel expenses: {travel_expense}")
print(f"Study materials: {study_material_expense}")
print(f"Mobile/internet expenses: {mobile_internet_expense}")
print(f"Other expenses: {other_expense}")
#to find total expense
total_expense = food_expense+travel_expense+study_material_expense+mobile_internet_expense+other_expense
print(f"Total expenses: {total_expense}")
#to find total balance
remaining_balance = monthly_income - total_expense
print(f"Remaining balance: {remaining_balance}")
#to find saving rate
if monthly_income > 0:
    saving = (remaining_balance/monthly_income)*100
    print(f"Saving rate: {saving}")
else:
    print(f"your monthly income is zero, please enter correct salary...")
