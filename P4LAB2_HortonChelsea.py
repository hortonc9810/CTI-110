# Chelsea Horton
#4/30/2025
#P4LAB2
# Write a program using loops to ask the user to enter an integer

run_program = 'yes'

while run_program == 'yes':
    number = int(input('Enter an integer: '))

    if number < 0:
        print('This program does not handle negative numbers')
    else:
        for i in range(1, 13):
            print(number, 'x', i, '=', number * i)

    run_program = input('Would you like to run the program again? (yes or no): ')

print('Exiting program.....')