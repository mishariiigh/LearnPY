#import math

#radius = float(input ('Enter the radius of a circle: '))

#circumference = 2 * math.pi * radius

#print(f"The Circumference is: {round(circumference, 2)}") # round function is to round up number without it, it would just show float numbers. with a 2 is showing only 2 float numbers.

###################################

#import math

#radius = float(input("Enter the radius of a circle: "))
#area = math.pi * pow(radius, 2)

#print(f"The area of the circle is: {round(area, 2)}cm^2")
#################################

import math
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a,2) + pow(b, 2))

print(f"Side C = {c}")



