# Chelsea Horton
#4/8/25
#P2HW1
# reformat previous program to enhance the display
print('This program calculates and displays travel expenses','\n')
budget = float(input('Enter Budget: '))
print('\n')
trav_dest = input('Enter your travel destination: ')
print('\n')
gas = float(input('How much will you spend on gas? '))
print('\n')
hotel = float(input('Appriximately, how much will you need for accommodation/hotel? '))
print('\n')
food = float(input('Last, how much do you need for food? '))
print('\n')
print('------------Travel Expenses------------')
print(f'{'Location:':20}{trav_dest}')
print(f'{'Initial Budget:':20} ${budget:.2f}')
print(f'{'Fuel:':20} ${gas:.2f}')
print(f'{'Accommodation:':20} ${hotel:.2f}')
print(f'{'Food:':20} ${food:.2f}')
print('----------------------------------------''\n')
total_expenses = gas + hotel + food
remain_bal = budget - total_expenses
print(f'{'Remaining Balance:':20} ${remain_bal:.2f}')