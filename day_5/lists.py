# Day 5: 30 Days of python programming

# ---------------- Quick Start ----------------
# From the course repo: quickstart/day_05.py
# (commented out so running this file doesn't run it; run it from the course repo root
#  with: python3 quickstart/day_05.py)
#
#   # Day 5: lists
#
#   empty = []                                          # Ex L1.1
#   fruits = ['apple', 'kiwi', 'mango', 'pear', 'plum']
#   print(len(fruits), fruits[0], fruits[len(fruits) // 2], fruits[-1])   # Ex L1.3-4, 8-9
#
#   fruits[1] = 'KIWI'                                  # Ex L1.10, 13: change an item
#   fruits.append('fig')                                # Ex L1.11: add to the end
#   fruits.insert(2, 'lime')                            # Ex L1.12: insert at an index
#   print('fig' in fruits)                              # Ex L1.15
#   print(' + '.join(fruits))                           # Ex L1.14: list -> string
#
#   fruits.sort()                                       # Ex L1.16
#   print(fruits)
#   fruits.reverse()                                    # Ex L1.17 (or sort(reverse=True))
#   print(fruits)
#   print(fruits[:3], fruits[-3:], fruits[3:5])         # Ex L1.18-20: slicing
#
#   fruits.pop(0)                                       # Ex L1.21: remove by index
#   fruits.remove('mango')                              # Ex L1.22: remove by value
#   fruits.pop()                                        # Ex L1.23: remove the last item
#   fruits.clear()                                      # Ex L1.24: empty the list
#   del fruits                                          # Ex L1.25: delete the variable
#
#   a, b = [1, 2], [3, 4]
#   joined = a + b                                      # Ex L1.26
#   copy = joined.copy()                                # Ex L1.27: copy first, then edit safely
#   copy.insert(2, 99)
#   print(joined, copy)
#
#   nums = [7, 3, 9, 3]
#   print(min(nums), max(nums), sum(nums) / len(nums), abs(3 - 9))   # Ex L2.1
#   print(sorted(nums))                                 # sorted() returns a new list
#
#   import sys                                          # Ex L2.2-3: run from the repo root
#   sys.path.append('data')                             # let import look inside data/
#   from countries import countries                     # data/countries.py -> its countries list
#   half = (len(countries) + 1) // 2                    # +1 gives the first half the extra item
#   print(len(countries), countries[:half][-1])
#
#   first, *rest = ['A', 'B', 'C', 'D']                 # Ex L2.4: * collects the rest
#   print(first, rest)
# ---------------- End Quick Start ----------------

# ---------------- Exercises: Level 1 ----------------

# Day 5 – Exercise Level 1, Q1:
# Declare an empty list


# Day 5 – Exercise Level 1, Q2:
# Declare a list with more than 5 items


# Day 5 – Exercise Level 1, Q3:
# Find the length of your list


# Day 5 – Exercise Level 1, Q4:
# Get the first item, the middle item and the last item of the list


# Day 5 – Exercise Level 1, Q5:
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)


# Day 5 – Exercise Level 1, Q6:
# Declare a list variable named it_companies and assign initial values Facebook, Google,
# Microsoft, Apple, IBM, Oracle and Amazon.


# Day 5 – Exercise Level 1, Q7:
# Print the list using print()


# Day 5 – Exercise Level 1, Q8:
# Print the number of companies in the list


# Day 5 – Exercise Level 1, Q9:
# Print the first, middle and last company


# Day 5 – Exercise Level 1, Q10:
# Print the list after modifying one of the companies


# Day 5 – Exercise Level 1, Q11:
# Add an IT company to it_companies


# Day 5 – Exercise Level 1, Q12:
# Insert an IT company in the middle of the companies list


# Day 5 – Exercise Level 1, Q13:
# Change one of the it_companies names to uppercase (IBM excluded!)


# Day 5 – Exercise Level 1, Q14:
# Join the it_companies with a string '#;  '


# Day 5 – Exercise Level 1, Q15:
# Check if a certain company exists in the it_companies list.


# Day 5 – Exercise Level 1, Q16:
# Sort the list using sort() method


# Day 5 – Exercise Level 1, Q17:
# Reverse the list in descending order using reverse() method


# Day 5 – Exercise Level 1, Q18:
# Slice out the first 3 companies from the list


# Day 5 – Exercise Level 1, Q19:
# Slice out the last 3 companies from the list


# Day 5 – Exercise Level 1, Q20:
# Slice out the middle IT company or companies from the list


# Day 5 – Exercise Level 1, Q21:
# Remove the first IT company from the list


# Day 5 – Exercise Level 1, Q22:
# Remove the middle IT company or companies from the list


# Day 5 – Exercise Level 1, Q23:
# Remove the last IT company from the list


# Day 5 – Exercise Level 1, Q24:
# Remove all IT companies from the list


# Day 5 – Exercise Level 1, Q25:
# Destroy the IT companies list


# Day 5 – Exercise Level 1, Q26:
# Join the following lists:
#   front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
#   back_end = ['Node','Express', 'MongoDB']


# Day 5 – Exercise Level 1, Q27:
# After joining the lists in question 26. Copy the joined list and assign it to a variable
# full_stack, then insert Python and SQL after Redux.


# ---------------- Exercises: Level 2 ----------------

# Day 5 – Exercise Level 2, Q1:
# The following is a list of 10 students ages:
#   ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#   - Sort the list and find the min and max age
#   - Add the min age and the max age again to the list
#   - Find the median age (one middle item or two middle items divided by two)
#   - Find the average age (sum of all items divided by their number )
#   - Find the range of the ages (max minus min)
#   - Compare the value of (min - average) and (max - average), use abs() method


# Day 5 – Exercise Level 2, Q2:
# Find the middle country(ies) in the countries list
# (the list is in the lessons fork: data/countries.py)


# Day 5 – Exercise Level 2, Q3:
# Divide the countries list into two equal lists if it is even if not one more country for the first half.


# Day 5 – Exercise Level 2, Q4:
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three
# countries and the rest as scandic countries.

