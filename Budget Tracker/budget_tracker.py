
'''
Enter income, expense name, expense amount, add another expense, show budget
'''

'''Enter income and 1st expense'''
print("\n\n")
income = float(input("Enter your monthly income: $"))

expense_name_list = []
expense_name = input("Enter the expense name (EX: rent): ")
expense_name_list.append(expense_name)

expense_amount_list = []
expense_amount = float(input("Enter the expense amout: $"))
expense_amount_list.append(expense_amount)


budget = income 
budget -= expense_amount
'''Subtract expenses from input not array. Use array for print out.'''

choice = int(input("1. Add another expense\n2. Show budget\nChoice: "))

expenses = 1
while choice == 1:
    expense_name = input("Enter the expense name (EX: rent): ")
    expense_name_list.append(expense_name)

    expense_amount = float(input("Enter the expense amout: $"))
    expense_amount_list.append(expense_amount)

    budget -= expense_amount
    expenses += 1

    choice = int(input("1. Add another expense\n2. Show budget\nChoice: "))

print("\n\nMonthly income: $", income)
i = 0
while i < expenses:
    print(expense_name_list[i], ":", "$", expense_amount_list[i])
    i+=1

print("Monthly budget: $", round(budget, 2))
