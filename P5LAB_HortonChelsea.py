# Chelsea Horton
# 5/8/25
# P5LAB
# Incorpate loops, functions and module in a previous program that simulates a self-checkout machine.

import random

def disperse_change(amount_of_money):
    cents = int(round(amount_of_money * 100))

    if cents == 0:
        print('No change')
        return

    dollars = cents // 100
    cents %= 100
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5
    pennies = cents

    if dollars == 1:
        print('1 Dollar')
    elif dollars > 1:
        print(f'{dollars} Dollars')
    if quarters == 1:
        print('1 Quarter')
    elif quarters > 1:
        print(f'{quarters} Quarters')
    if dimes == 1:
        print('1 Dime')
    elif dimes > 1:
        print(f'{dimes} Dimes')
    if nickels == 1:
        print('1 Nickel')
    elif nickels > 1:
        print(f'{nickels} Nickels')
    if pennies == 1:
        print('1 Penny')
    elif pennies > 1:
        print(f'{pennies} Pennies')

def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed:.2f}")
    
    cash_given = float(input("How much cash will you put in the self-checkout? "))
    change = round(cash_given - amount_owed, 2)

    if change < 0:
        print("Not enough money entered.")
    else:
        print(f"Change is: ${change:.2f}")
        disperse_change(change)

main()