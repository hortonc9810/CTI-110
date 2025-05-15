#Chelsea Horton
#4/9/25
#P2HW2
#design a program that displays the grades from each module and find the min,max, avg, and sum

grade1 = float(input('Enter grade for Module 1: '))
grade2 = float(input('Enter grade for Module 2: '))
grade3 = float(input('Enter grade for Module 3: '))
grade4 = float(input('Enter grade for Module 4: '))
grade5 = float(input('Enter grade for Module 5: '))
grade6 = float(input('Enter grade for Module 6: '))

module_grades = [grade1, grade2, grade3, grade4, grade5, grade6]
               
low_grade = min(module_grades)
high_grade = max(module_grades)
sum_grade = sum(module_grades)
avg_grade = sum_grade / len(module_grades)

print('\n------------Results------------')
print(f'{'Lowest Grade:':20}{low_grade:.1f}')
print(f'{'Highest Grade:':20}{high_grade:.1f}')
print(f'{'Sum of Grade:':20}{sum_grade:.1f}')
print(f'{'Average:':20}{avg_grade:.2f}')
print('----------------------------------------')
