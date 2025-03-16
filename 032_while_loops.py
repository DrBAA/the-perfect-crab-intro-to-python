# Video alternative: https://vimeo.com/954334424/6e40d11ef1#t=0

from lib.helpers import check_that_these_are_equal

# Remember `if`s? Here's a reminder:

my_name = "Beth"
if my_name == "Kay":
  print("Hello, Kay!")
else:
  print("Hello, you!")

# The `if` is part of a category of programming tools known as 'control flow'.
# These are tools that control the flow of execution in a program. The `if`
# controls which lines get executed.

# There's another kind of control flow: the loop. It comes in two varieties:
# `for` and `while` loops.

# A while loop is perhaps the most simple:

i = 0 # We call this the counter variable
while i <= 10:
  print(f"The number is now {i}")
  # i = i + 2
  i += 1

# @TASK: run this program and see what it does.

# The `while` loop is like an `if`, in that it takes an expression that
# evaluates to True or False, and then executes its block of code if the
# condition is True.

# However, the `while` loop is different in that it keeps repeatedly executing
# the block for as long as the condition is True.

# @TASK: Here's an exercise where you can put it into practice:

print("")
print("Function: add_cats_repeatedly")



# Write a function that adds the item "cats" to the given word_list, repeatedly,
# a number of times defined by the given count parameter.
# Example:
#    add_cats_repeatedly([], 3)
# => ['cats', 'cats', 'cats']

# ORIGINAL CODE 
def add_cats_repeatedly(word_list, count):
  # ...
  return word_list

# CODE NOT WORKING FOR THE SECOND TEST
# in this example, The count parameter represents the number of times we want to add "cats" to the word_list. We do not need to reset the count to 0.
# By resetting it to 0, we lose the user's original input (e.g., 3). Instead, we use the count value as a target and compare it to the length of word_list to determine how many "cats" need to be added.
# the number of iterations is determined indirectly by the growing length of word_list, so a separate counter variable isn't necessary. If the user calls add_cats_repeatedly([], 3), the word_list starts empty (len(word_list) = 0). the while loop checks whether the length of word_list has reached the target value of count. By appending "cats" in each iteration, the length of word_list increases automatically, so we don't need to increment count.

print ("CODE NOT WORKING FOR THE SECOND TEST \n")
# def add_cats_repeatedly(word_list, count):
#     while len(word_list) < count:
#         word_list.append("cats")
#     return word_list

# check_that_these_are_equal(
#   add_cats_repeatedly([], 3), ['cats', 'cats', 'cats'])
# check_that_these_are_equal(
#   add_cats_repeatedly(['dogs'], 2), ['dogs', 'cats', 'cats'])

# NEW CODE - WORKING WITH COPILOT HELP
# Copilot introduced a counter variable (cats_added) to track how many times "cats" has been appended to word_list.
# The while loop runs until the total number of "cats" added (cats_added) equals the specified count.
# This approach doesn't rely on the initial length of word_list, so it works correctly for test cases where the list already has other items.

print("NEW CODE - WORKING WITH COPILOT HELP \n")
def add_cats_repeatedly(word_list, count):
    cats_added = 0  # Tracks how many "cats" have been added
    while cats_added < count:
        word_list.append("cats")
        cats_added += 1  # Increment the counter
    return word_list


check_that_these_are_equal(
  add_cats_repeatedly([], 3), ['cats', 'cats', 'cats'])
check_that_these_are_equal(
  add_cats_repeatedly(['dogs'], 2), ['dogs', 'cats', 'cats'])



print("ADD bananas to a list of fruits")
def add_bananas_repeatedly(fruits_list, count):
    bananas_added = 0  # Tracks how many "bananas" have been added
    while bananas_added < count:
        fruits_list.append("banana")
        bananas_added += 1  # Increment the counter
    return fruits_list

print("added bananas: ", add_bananas_repeatedly(["apple", "melons"], 5))

# When you're done, move on to 033_for_loops.py
