# Day 2: 30 Days of python programming

# ---------------- Quick Start ----------------
# From the course repo: quickstart/day_02.py
# (commented out so running this file doesn't run it; run it from the course repo root
#  with: python3 quickstart/day_02.py)
#
#   # Day 2: variables, built-in functions, casting, input   (Ex L1.2: comments start with #)
#
#   city = 'Cape Town'                             # Ex L1.3-12: name = value
#   age = 17
#   is_student = True
#   first, last, country = 'Ada', 'Lovelace', 'UK'  # Ex L1.13: many variables on one line
#
#   print(type(age), len(city))                    # Ex L2.1-3: type() and len()
#   print(len(first) > len(last))
#
#   a, b = 9, 4                                    # Ex L2.4-11: store results in variables
#   total = a + b
#   print(total, a - b, a * b, a / b, a % b, a ** b, a // b)
#
#   pi = 3.14
#   print(pi * 3 ** 2, 2 * pi * 3)                 # Ex L2.12: area pi*r**2, circumference 2*pi*r
#
#   radius = float(input('Radius: '))              # Ex L2.12.3, L2.13: input() always returns a str
#   print('Area:', pi * radius ** 2)               # so cast with int() or float() before doing math
#
#   # Ex L2.14: run  help('keywords')  to list words you can't use as variable names
# ---------------- End Quick Start ----------------

# ---------------- Exercises: Level 1 ----------------

# Day 2 – Exercise Level 1, Q1:
# Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
# (done – this file)

# Day 2 – Exercise Level 1, Q2:
# Write a python comment saying 'Day 2: 30 Days of python programming'
# (done – see the top of this file)

# Day 2 – Exercise Level 1, Q3:
# Declare a first name variable and assign a value to it
first_name = "Demir"

# Day 2 – Exercise Level 1, Q4:
# Declare a last name variable and assign a value to it
last_name = "Gursesler"

# Day 2 – Exercise Level 1, Q5:
# Declare a full name variable and assign a value to it
full_name = "Demir Gursesler"

# Day 2 – Exercise Level 1, Q6:
# Declare a country variable and assign a value to it
country = "Turkey"

# Day 2 – Exercise Level 1, Q7:
# Declare a city variable and assign a value to it
city = "Istanbul"

# Day 2 – Exercise Level 1, Q8:
# Declare an age variable and assign a value to it
age = 25

# Day 2 – Exercise Level 1, Q9:
# Declare a year variable and assign a value to it
year = 2026

# Day 2 – Exercise Level 1, Q10:
# Declare a variable is_married and assign a value to it
is_married = False

# Day 2 – Exercise Level 1, Q11:
# Declare a variable is_true and assign a value to it
is_true = True

# Day 2 – Exercise Level 1, Q12:
# Declare a variable is_light_on and assign a value to it
is_light_on = False

# Day 2 – Exercise Level 1, Q13:
# Declare multiple variable on one line
is_false,date,makeup = False,2026,False

# ---------------- Exercises: Level 2 ----------------

# Day 2 – Exercise Level 2, Q1:
# Check the data type of all your variables using type() built-in function
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
#...

# Day 2 – Exercise Level 2, Q2:
# Using the len() built-in function, find the length of your first name
print(len(first_name))

# Day 2 – Exercise Level 2, Q3:
# Compare the length of your first name and your last name
if len(first_name) == len(last_name):
    print("The length of your first and last name is the same")

else:
    print("The length of your first and last name is not the same")

# Day 2 – Exercise Level 2, Q4:
# Declare 5 as num_one and 4 as num_two
num_one,num_two = 5,4

# Day 2 – Exercise Level 2, Q5:
# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# Day 2 – Exercise Level 2, Q6:
# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

# Day 2 – Exercise Level 2, Q7:
# Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one

# Day 2 – Exercise Level 2, Q8:
# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# Day 2 – Exercise Level 2, Q9:
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

# Day 2 – Exercise Level 2, Q10:
# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one**num_two

# Day 2 – Exercise Level 2, Q11:
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# Day 2 – Exercise Level 2, Q12:
# The radius of a circle is 30 meters.
#   1. Calculate the area of a circle and assign the value to a variable name of area_of_circle
#   2. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
#   3. Take radius as user input and calculate the area.
area_of_circle = 3.141*(30**2)
circum_of_circle = 60*3.141
radius2 = int(input("What is the radius: "))
circum_of_circle_2 = 3.141*(radius2**2)
# Day 2 – Exercise Level 2, Q13:
# Use the built-in input function to get first name, last name, country and age from a user
# and store the value to their corresponding variable names
first_name2=input("What is your first name? ")
last_name2=input("What is your last name? ")
country2 = input("Where are you from? ")
age2 = input("What is your age? ")

# Day 2 – Exercise Level 2, Q14:
# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')