import string
# Video alternative: https://vimeo.com/954334424/6e40d11ef1#t=300

# There's another kind of loop — the `for` loop.

# It looks like this:

for letter in ["a", "b", "c"]:
  print(f"This letter is {letter}")

# @TASK: Run this file and see what it does.

# In programming jargon: the Python for loop iterates over a list.

# In everyday language: the Python for loop takes each item one by one and runs
# its block of code with that item.

# It's pretty nice. And there's another Python helper that makes it even more
# useful:

print("print numbers in range")
def print_numbers_in_range():
  for number in range(0, 10):
    print(f"This number is {number}")
print_numbers_in_range()

# def print_numbers_in_range():
#   for number in range(0, 10):
# print(print_numbers_in_range())  


# The range function only works with integers, not characters. Attempting to use range("a", "z") will raise a TypeError. To iterate through characters, you can use Python’s string module or the ASCII values with chr() and ord() functions. For example:

print("\nusing Python’s string module to print a to z")
def print_chars_in_range():
    for char in string.ascii_lowercase:  # Iterate over 'a' to 'z'
        print(f"This character is {char}")
print_chars_in_range()


print("\nAlternatively, using ASCII values")
def print_chars_in_range():
    for char in range(ord('a'), ord('z') + 1):  # ASCII values of 'a' to 'z'
        print(f"This character is {chr(char)}")
print_chars_in_range()


# `range` more or less creates a list of the numbers from its first parameter to
# one below its last parameter. So: the numbers 0-9.

# Compare this to the `while` version which does the same thing:

print("\nprint_numbers_in_range_with_a_while loop")
def print_numbers_in_range_with_a_while():
  number = 0
  while number <= 10:
    print(f"This number is {number}")
    number = number + 1
print_numbers_in_range_with_a_while()

# The `for` and `range` version is a bit more concise.

# You're probably expecting an exercise now. But not just yet. Lists and loops
# are very powerful tools and we're going to go through three different ways of
# using them:

# * Summarising: Using a loop to distil a list into one value.

# * Mapping: Using a loop to convert each item to another item.

# * Filtering: Using a loop to pick out only some items from a list.

# To start summarising, go to 034_summarising.py
