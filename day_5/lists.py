# Day 5: 30 Days of python programming

# ---------------- Quick Start ----------------
#   nums = [1, 2, 3]      # make a list
#   nums[0]               # index
#   nums[1:]              # slice
#   nums.append(4)        # list methods: append() insert() remove() pop() sort() reverse() copy() clear()
#   2 in nums             # check membership
#   first, *rest = nums   # unpack
# ---------------- End Quick Start ----------------

# ---------------- Exercises: Level 1 ----------------

# Day 5 – Exercise Level 1, Q1:
# Declare an empty list
nums = []

# Day 5 – Exercise Level 1, Q2:
# Declare a list with more than 5 items
num5 = [1, 2, 3, 4, 5, 6]

# Day 5 – Exercise Level 1, Q3:
# Find the length of your list
print(len(num5))
# Day 5 – Exercise Level 1, Q4:
# Get the first item, the middle item and the last item of the list
print(num5[0], num5[len(num5) // 2], num5[-1])

# Day 5 – Exercise Level 1, Q5:
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ["Demir", 16, 187, "Single", "Capetown"]

# Day 5 – Exercise Level 1, Q6:
# Declare a list variable named it_companies and assign initial values Facebook, Google,
# Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Day 5 – Exercise Level 1, Q7:
# Print the list using print()
print(it_companies)

# Day 5 – Exercise Level 1, Q8:
# Print the number of companies in the list
print(len(it_companies))

# Day 5 – Exercise Level 1, Q9:
# Print the first, middle and last company
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])

# Day 5 – Exercise Level 1, Q10:
# Print the list after modifying one of the companies
it_companies[0] = "Meta"
print(it_companies)

# Day 5 – Exercise Level 1, Q11:
# Add an IT company to it_companies
it_companies.append("Anthropic")

# Day 5 – Exercise Level 1, Q12:
# Insert an IT company in the middle of the companies list
it_companies.insert(3,"OpenAI")
print(it_companies)

# Day 5 – Exercise Level 1, Q13:
# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[6] = it_companies[6].upper()
print(it_companies)

# Day 5 – Exercise Level 1, Q14:
# Join the it_companies with a string '#;  '
sentence = "#; ".join(it_companies)
print(sentence)

# Day 5 – Exercise Level 1, Q15:
# Check if a certain company exists in the it_companies list.
if "IBM" in it_companies:
    print("My item exists!")

# Day 5 – Exercise Level 1, Q16:
# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Day 5 – Exercise Level 1, Q17:
# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Day 5 – Exercise Level 1, Q18:
# Slice out the first 3 companies from the list
new_companies = it_companies[:3]
print(new_companies)


# Day 5 – Exercise Level 1, Q19:
# Slice out the last 3 companies from the list
last_companies = it_companies[-3:]
print(last_companies)
# Day 5 – Exercise Level 1, Q20:
# Slice out the middle IT company or companies from the list
hero = len(it_companies)//2

mid_companies = it_companies[hero]
print(mid_companies)
# Day 5 – Exercise Level 1, Q21:
# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Day 5 – Exercise Level 1, Q22:
# Remove the middle IT company or companies from the list
it_companies.pop(hero)
print(it_companies)

# Day 5 – Exercise Level 1, Q23:
# Remove the last IT company from the list
hi = it_companies.pop(-1)
print(hi)
# Day 5 – Exercise Level 1, Q24:
# Remove all IT companies from the lis
while len(it_companies) > 0:
    popped = it_companies.pop(0)
    print(f"Popped: {popped}")
    print(it_companies)

# Day 5 – Exercise Level 1, Q25:
# Destroy the IT companies list
del it_companies
# Day 5 – Exercise Level 1, Q26:
# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joined = front_end + back_end
print(joined)

# Day 5 – Exercise Level 1, Q27:
# After joining the lists in question 26. Copy the joined list and assign it to a variable
# full_stack, then insert Python and SQL after Redux.
full_stack = joined.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)

# ---------------- Exercises: Level 2 ----------------

# Day 5 – Exercise Level 2, Q1:
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#   - Sort the list and find the min and max age
#   - Add the min age and the max age again to the list
#   - Find the median age (one middle item or two middle items divided by two)
#   - Find the average age (sum of all items divided by their number )
#   - Find the range of the ages (max minus min)
#   - Compare the value of (min - average) and (max - average), use abs() method
import statistics
lowest = min(ages)
highest = max(ages)
median = statistics.median(ages)
average_sum = sum(ages) / len(ages)
age_range = highest-lowest
min_diff= abs(lowest-average_sum)
max_diff = abs(highest-average_sum)

# Day 5 – Exercise Level 2, Q2:
# Find the middle country(ies) in the countries list
# (the list is in the lessons fork: data/countries.py)
import countries
len_countries = len(countries.countries)
divided = len_countries//2
if len_countries % 2 == 0:
    print(countries.countries[divided-1:divided+1])
else:
    print(countries.countries[divided])

# Day 5 – Exercise Level 2, Q3:
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
split_at = (len_countries+1)//2
first_half = countries.countries[:split_at]
second_half = countries.countries[split_at:]
print(first_half)
print(second_half)
print(len(first_half), len(second_half))

# Day 5 – Exercise Level 2, Q4:
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three
# countries and the rest as scandic countries.
China, Russia, America,  *others = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(others)