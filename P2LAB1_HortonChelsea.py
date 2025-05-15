# Chelsea Horton
# 4/7/25
# P2LAB1
# Write Code that performs mathematical calculations and displays info to users
import math
# Get Radius from User
radius = float(input('What is the radius of the circle? ')) 
# calculations for diameter, circumference, and area

cir = 2 * math.pi * radius
diam = 2 * radius
area = math.pi * (radius**2)

# display results
print(f'The diameter of the circle is {diam:.1f}')
print(f'The circumference of the circile is {cir:.2f}')
print(f'The area of the circle is {area:.3f}')