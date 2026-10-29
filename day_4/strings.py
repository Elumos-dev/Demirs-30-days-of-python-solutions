# Day 4: 30 Days of python programming

# ---------------- Quick Start ----------------
#   'a' + 'b'             # join strings
#   s = 'hello'
#   s.upper()             # string methods: upper() lower() title() replace() split() strip() ...
#   s[0]                  # index
#   s[1:3]                # slice
#   s.find('l')           # position of a match
#   f'Hi {s}'             # f-string
#   'a\nb'                # \n new line, \t tab
# ---------------- End Quick Start ----------------

# ---------------- Exercises ----------------

# Day 4 – Exercise Q1:
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print('Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python')

# Day 4 – Exercise Q2:
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('Coding' + ' ' + 'For' + ' ' + 'All')

# Day 4 – Exercise Q3:
# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# Day 4 – Exercise Q4:
# Print the variable company using print().
print(company)

# Day 4 – Exercise Q5:
# Print the length of the company string using len() method and print().
print(len(company))

# Day 4 – Exercise Q6:
# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Day 4 – Exercise Q7:
# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Day 4 – Exercise Q8:
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Day 4 – Exercise Q9:
# Cut(slice) out the first word of Coding For All string.
print(company[0:6])

# Day 4 – Exercise Q10:
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("Coding" in company)

# Day 4 – Exercise Q11:
# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))

# Day 4 – Exercise Q12:
# Change "Python for Everyone" to "Python for All" using the replace method or other methods.
print("Python for Everyone".replace("Everyone", "All"))

# Day 4 – Exercise Q13:
# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "))

# Day 4 – Exercise Q14:
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
sentence2 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(sentence2.split(", "))
# Day 4 – Exercise Q15:
# What is the character at index 0 in the string Coding For All.
print(company[0])

# Day 4 – Exercise Q16:
# What is the last index of the string Coding For All.
print(len(company) - 1)

# Day 4 – Exercise Q17:
# What character is at index 10 in "Coding For All" string.
print(company[10])

# Day 4 – Exercise Q18:
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
words = "Python For Everyone".split()
print(words[0][0] + words[1][0] + words[2][0])

# Day 4 – Exercise Q19:
# Create an acronym or an abbreviation for the name 'Coding For All'.
words = company.split()
print(words[0][0] + words[1][0] + words[2][0])

# Day 4 – Exercise Q20:
# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index("C"))

# Day 4 – Exercise Q21:
# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index("F"))

# Day 4 – Exercise Q22:
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("Coding For All People".rfind("l"))

# Day 4 – Exercise Q23:
# Use index or find to find the position of the first occurrence of the word 'because' in the
# following sentence: 'You cannot end a sentence with because because because is a conjunction'
print("You cannot end a sentence with because because because is a conjunction".find("because"))

# Day 4 – Exercise Q24:
# Use rindex to find the position of the last occurrence of the word because in the following
# sentence: 'You cannot end a sentence with because because because is a conjunction'
print("You cannot end a sentence with because because because is a conjunction".rindex("because"))

# Day 4 – Exercise Q25:
# Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence[31:54])

# Day 4 – Exercise Q26:
# Find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find("because"))

# Day 4 – Exercise Q27:
# Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
start_index = sentence.find("because because because")
end_index = start_index + len("because because because")

print(sentence[start_index:end_index])

# Day 4 – Exercise Q28:
# Does 'Coding For All' start with a substring Coding?
print(company.startswith("Coding"))

# Day 4 – Exercise Q29:
# Does 'Coding For All' end with a substring coding?
print(company.endswith("coding"))

# Day 4 – Exercise Q30:
# '   Coding For All      ', remove the left and right trailing spaces in the given string.
sen ="    Coding For All      "
start_index1 = sen.find("C")
end_index1 = start_index1 + len(company)
print(sen[start_index1:end_index1])

# Day 4 – Exercise Q31:
# Which one of the following variables return True when we use the method isidentifier():
#   - 30DaysOfPython
#   - thirty_days_of_python
#option 2 because it can not start with an integer
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# Day 4 – Exercise Q32:
# The following list contains the names of some of python libraries:
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
sen2 = 'Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'
print("# ".join(sen2))

# Day 4 – Exercise Q33:
# Use the new line escape sequence to separate the following sentences.
#   I am enjoying this challenge.
#   I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

# Day 4 – Exercise Q34:
# Use a tab escape sequence to write the following lines.
#   Name      Age     Country   City
#   Asabeneh  250     Finland   Helsinki
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# Day 4 – Exercise Q35:
# Use the string formatting method to display the following:
#   radius = 10
#   area = 3.14 * radius ** 2
#   The area of a circle with radius 10 is 314 meters square.
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area:.0f} meters square.")

# Day 4 – Exercise Q36:
# Make the following using string formatting methods:
#   8 + 6 = 14
#   8 - 6 = 2
#   8 * 6 = 48
#   8 / 6 = 1.33
#   8 % 6 = 2
#   8 // 6 = 1
#   8 ** 6 = 262144
a = 8
b = 6
print(f"{a} + {b} = {a+b}\n{a} - {b} = {a -b}\n{a} * {b} = {a *b}\n{a} / {b} = {a/b:.2f}\n{a} % {b} = {a % b}\n{a} // {b} = {a//b}\n{a} ** {b} = {a**b}")
