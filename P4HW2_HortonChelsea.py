# Chelsea Horton
# 4/30/2025
# P4HW2
# Enhance the existing program and add key information like gross pay, total overtime pay, and total amount amoungst employees.

# define total values to keep track of multiple employees
employee_count = 0
total_overtime = 0.0
total_regular = 0.0
total_gross = 0.0

# Create loop to process employee data including employee name, pay rate, and hours worked
while True:
    name_employee = input("Enter employee's name or 'Done' to terminate: ")
    if name_employee == 'Done':
        break

    work_hours = float(input("Enter number of hours worked:"))
    pay_rate = float(input("Enter employee's pay rate: "))

 # Determine regular and overtime hours
    if work_hours > 40:
        overtime_hours = work_hours - 40
        regular_hours = 40
    else:
        overtime_hours = 0
        regular_hours = work_hours

 # Calculate pay
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay

 # Update the totals for all employees
    employee_count = employee_count + 1
    total_overtime = total_overtime + overtime_pay
    total_regular = total_regular + regular_pay
    total_gross = total_gross + gross_pay

 # Display the results for current employee
    print("\n--------------------------------------------")
    print(f"Employee name: {name_employee}")
    print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
    print("--------------------------------------------------------------------------------------")
    print(f"{work_hours:<14.1f}{pay_rate:<11.2f}{overtime_hours:<10.1f}{overtime_pay:<15.2f}{regular_pay:<13.2f}{gross_pay:.2f}")
    print()

# Display final totals for all listed employees
print("Total number of employees entered:", employee_count)
print(f"Total amount paid for overtime: ${total_overtime:.2f}")
print(f"Total amount paid for regular hours: ${total_regular:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")
