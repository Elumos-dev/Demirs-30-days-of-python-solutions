# Day 3: 30 Days of python programming

# ---------------- Quick Start ----------------
#   5 > 3                 # comparison: > < >= <= == !=
#   'a' in 'cat'          # in / not in
#   True and False        # and / or / not
#   7 % 2                 # remainder
#   7 // 2                # floor division
# ---------------- End Quick Start ----------------

# ---------------- Exercises ----------------

# Day 3 – Exercise Q1:
# Declare your age as integer variable
age = 16

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
side_a = float(input("Enter side A"))
side_b = float(input("Enter side B"))
side_c = float(input("Enter side C"))
perimeter = side_a + side_b + side_c
print(perimeter)

# Day 3 – Exercise Q6:
# Get length and width of a rectangle using prompt. Calculate its area (area = length x width)
# and perimeter (perimeter = 2 x (length + width))
length_rec = float(input("Enter the rectangle length"))
width_rec = float(input("Enter the rectangle width"))
perimeter_rec = 2 * (length_rec + width_rec)
area = length_rec * width_rec
print(perimeter_rec)
print(area)

# Day 3 – Exercise Q7:
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and
# circumference (c = 2 x pi x r) where pi = 3.14.
rad_circle = float(input("Enter radius of a circle"))
circum_rad = 2 * 3.14 * rad_circle
print(circum_rad)

# Day 3 – Exercise Q8:
# Calculate the slope, x-intercept and y-intercept of y = 2x -2
y_intercept = -2
slope = 2
x_intercept = 1

# Day 3 – Exercise Q9:
# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_points = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(slope_points)
print(distance)


# Day 3 – Exercise Q10:
# Compare the slopes in tasks 8 and 9.
print(slope == slope_points)

# Day 3 – Exercise Q11:
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out
# at what x value y is going to be 0.
print((-3)^2 + 6(-3) + 9)

# Day 3 – Exercise Q12:
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
word1 = "python"
print(len(word1) != len(word2))

word2 = "dragon"
print(len(word2))
if (word1 == word2):
    print("The words are the same length")
# Day 3 – Exercise Q13:
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
if ("on" in word1) and ("on" in word2):
    print("on is in both words")
else:
    print("on is not in both words")

# Day 3 – Exercise Q14:
# "I hope this course is not full of jargon". Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon"
if "jargon" in sentence:
    print("jargon is in the sentence")

# Day 3 – Exercise Q15:
# There is no 'on' in both dragon and python
print(("on" not in word1) and ("on" not in word2))

# Day 3 – Exercise Q16:
# Find the length of the text python and convert the value to float and convert it to string
print(str(float(len(word1))))

# Day 3 – Exercise Q17:
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is
# even or not using python?
number = float(input("Enter your number"))
if (number % 2 == 0):
    print("The number is even")
else:
    print("The number is odd")

# Day 3 – Exercise Q18:
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
fact_check = (7 // 3) == int(2.7)
print(fact_check)

# Day 3 – Exercise Q19:
# Check if type of '10' is equal to type of 10
print(type('10') == type(10))

# Day 3 – Exercise Q20:
# Check if int('9.8') is equal to 10
#print(int(('9.8')) == 10)
#can convert '9.8'

# Day 3 – Exercise Q21:
# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
#   Enter hours: 40
#   Enter rate per hour: 28
#   Your weekly earning is 1120
hours = float(input("Enter hours"))
rate = float(input("Enter your rate per hour"))
print("Your weekly earning is ", (hours*rate))

# Day 3 – Exercise Q22:
# Write a script that prompts the user to enter number of years. Calculate the number of seconds
# a person can live. Assume a person can live hundred years
#   Enter number of years you have lived: 100
#   You have lived for 3153600000 seconds.
years_lived=float(input("Enter your number of years you have lived"))
print("You have lived ", (years_lived * 365 * 24 * 60 * 60))

# Day 3 – Exercise Q23:
# Write a Python script that displays the following table
#   1 1 1 1 1
#   2 1 2 4 8
#   3 1 3 9 27
#   4 1 4 16 64
#   5 1 5 25 125

for i in range(1, 6):
    print(f"{i} {i**0} {i**1} {i**2} {i**3}")