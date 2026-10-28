# Day 3: 30 Days of python programming

# ---------------- Quick Start ----------------
# From the course repo: quickstart/day_03.py
# (commented out so running this file doesn't run it; run it from the course repo root
#  with: python3 quickstart/day_03.py)
#
#   # Day 3: operators
#
#   height = 1.82                               # Ex 1-3: int, float, complex
#   z = 3 + 4j
#
#   base = float(input('Enter base: '))         # Ex 4-7, 21-22: prompt, cast, calculate, print
#   print('Double the base is', base * 2)
#
#   print(5 > 3, 5 == 5.0, 5 != 4)              # comparison -> True True True
#   print(len('cat') > len('dog'))              # Ex 12: compare lengths -> False
#   print('at' in 'cat' and 'at' in 'hat')      # Ex 13-15: in, and, not in
#   print('x' not in 'cat')
#   print(10 % 2 == 0)                          # Ex 17: even means remainder 0
#   print(7 // 2 == int(3.9))                   # Ex 18: int() chops decimals, no rounding
#   print(type('5') == type(5))                 # Ex 19
#   print(int(float('9.8')))                    # Ex 20: int('9.8') crashes, go through float()
#   print(str(float(len('code'))))              # Ex 16: chain casts
#
#   m = (8 - 2) / (5 - 2)                       # Ex 8-10: slope = (y2 - y1) / (x2 - x1)
#   print(m)
#
#   x = -2                                      # Ex 11: plug x in, try values until y == 0
#   print(x ** 2 + 4 * x + 4)
#
#   print(60 * 60 * 24 * 365)                   # Ex 22: seconds in a year
#   print(f'{2} {2 ** 2} {2 ** 3}')             # Ex 23: one table row per print
# ---------------- End Quick Start ----------------

# ---------------- Exercises ----------------

# Day 3 – Exercise Q1:
# Declare your age as integer variable
height = 16

# Day 3 – Exercise Q2:
# Declare your height as a float variable
height = 187.5

# Day 3 – Exercise Q3:
# Declare a variable that store a complex number
complex_num = 3-1j

# Day 3 – Exercise Q4:
# Write a script that prompts the user to enter base and height of the triangle and calculate
# an area of this triangle (area = 0.5 x b x h).
#   Enter base: 20
#   Enter height: 10
#   The area of the triangle is 100
base_triangle = float(input("What is the base? "))
height_triangle = float(input("What is the height? "))
area_triangle = 0.5*base_triangle*height_triangle
print(area_triangle)
# Day 3 – Exercise Q5:
# Write a script that prompts the user to enter side a, side b, and side c of the triangle.
# Calculate the perimeter of the triangle (perimeter = a + b + c).
#   Enter side a: 5
#   Enter side b: 4
#   Enter side c: 3
#   The perimeter of the triangle is 12


# Day 3 – Exercise Q6:
# Get length and width of a rectangle using prompt. Calculate its area (area = length x width)
# and perimeter (perimeter = 2 x (length + width))


# Day 3 – Exercise Q7:
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and
# circumference (c = 2 x pi x r) where pi = 3.14.


# Day 3 – Exercise Q8:
# Calculate the slope, x-intercept and y-intercept of y = 2x -2


# Day 3 – Exercise Q9:
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)


# Day 3 – Exercise Q10:
# Compare the slopes in tasks 8 and 9.


# Day 3 – Exercise Q11:
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out
# at what x value y is going to be 0.


# Day 3 – Exercise Q12:
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.


# Day 3 – Exercise Q13:
# Use and operator to check if 'on' is found in both 'python' and 'dragon'


# Day 3 – Exercise Q14:
# "I hope this course is not full of jargon". Use in operator to check if jargon is in the sentence.


# Day 3 – Exercise Q15:
# There is no 'on' in both dragon and python


# Day 3 – Exercise Q16:
# Find the length of the text python and convert the value to float and convert it to string


# Day 3 – Exercise Q17:
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is
# even or not using python?


# Day 3 – Exercise Q18:
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.


# Day 3 – Exercise Q19:
# Check if type of '10' is equal to type of 10


# Day 3 – Exercise Q20:
# Check if int('9.8') is equal to 10


# Day 3 – Exercise Q21:
# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
#   Enter hours: 40
#   Enter rate per hour: 28
#   Your weekly earning is 1120


# Day 3 – Exercise Q22:
# Write a script that prompts the user to enter number of years. Calculate the number of seconds
# a person can live. Assume a person can live hundred years
#   Enter number of years you have lived: 100
#   You have lived for 3153600000 seconds.


# Day 3 – Exercise Q23:
# Write a Python script that displays the following table
#   1 1 1 1 1
#   2 1 2 4 8
#   3 1 3 9 27
#   4 1 4 16 64
#   5 1 5 25 125

