# Chelsea Horton
#4/23/2025
#P3HW2
#create a program designed to display employee information and calculate wages

# Gather the employee's identifying information
name_employee = input("Enter employee's name: ")
work_hours = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

#determine if employee has worked overtime
if work_hours > 40:
    overtime = work_hours - 40
    norm_hours = 40
else:
    overtime = 0
    norm_hours = work_hours

# Calculate overtime and normal pay
norm_pay = norm_hours * pay_rate
overtime_pay = overtime * (pay_rate * 1.5)
gross_pay = norm_pay + overtime_pay

# print the outputs
print('\n-----------------------------------')
print('Employee name: ', name_employee)
print('\n')
print('Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay     ')
print('\n--------------------------------------------------------------------------------------')
print(f'{work_hours:<15.1f}{pay_rate:<11.1f}{overtime:<12.1f}{overtime_pay:<15.2f}{norm_pay:<13.2f}{gross_pay:.2f}')
