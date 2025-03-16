# Video alternative: https://vimeo.com/954334322/c5a36d4407#t=726

from lib.helpers import check_that_these_are_equal

# Here's a great use for dictionaries: counting!

# For example, counting how many times each letter appears in a string.

# We can use a for loop to iterate over some items, and then use a dictionary to
# keep count of the items we've seen.

# In the process, you'll see a few dictionary functions at work, plus the sneaky
# addition of looping over characters in strings.

# The square brackets [] are used because dictionaries in Python are accessed using keys enclosed in square brackets.

# This program counts the frequency of each character in a given string, including spaces, and stores the counts in a dictionary. It iterates over the string one character at a time, checking whether the character is already present in the dictionary. If the character is not present, it adds it as a key and initializes its value to 1. If the character is already present, it increments the value by 1. At the end, the dictionary contains each character as a key and the corresponding number of times it appeared in the string as the value. The final result is printed for the user.

text = "the quick brush jumped over the lazy crab"

# We'll use a dictionary to keep count of the letters we've seen. We'll start
# with an empty dictionary:

letter_counts = {}
# The keys will be the letters, and the values will be the number of that letter
# we've seen.

# We'll use a for loop to iterate over each letter in the string:

for letter in text:
  # We'll check if the letter is already in our dictionary of counts. We can do
  # this using the `not in` operator. 
  if letter not in letter_counts:
    # If it isn't, we'll add it to the dictionary with a starting count of 1.
    letter_counts[letter] = 1
    # Note that the syntax for assigning a value to a key in a dict is similar
    # to assigning a variable.
  else:
    # If it is, we'll increment the count for that letter.
    letter_counts[letter] = letter_counts[letter] + 1
  
# Let's print out the dictionary to see what we've got:
print("letter counts = ", letter_counts)  
# output
# letter counts =
# {
#  't': 2, 'h': 3, 'e': 5, ' ': 8, 'q': 1, 'u': 3, 'i': 1, 'c': 3, 'k': 1, 
#  'b': 2, 'r': 3, 's': 1, 'j': 1, 'm': 1, 'p': 1, 'd': 1, 'o': 1, 'v': 1, 
#  'l': 1, 'a': 3, 'z': 1, 'y': 1
# }



text2 = "the thinnest quick brush jumped over the lazy crab"
letter_counts2 = {}
for letter in text2:
  if letter not in letter_counts2:
     letter_counts2[letter] = 1
  else:
     letter_counts2[letter] = letter_counts2[letter] + 1

print("letter counts2 = ", letter_counts2)
# output
# letter counts2 =  {
#  't': 4, 'h': 3, 'e': 6, ' ': 8, 'i': 1, 'n': 3, 's': 2, 'q': 1, 
#  'u': 3, 'c': 3, 'k': 1, 'b': 2, 'r': 3, 'j': 1, 'm': 1, 'p': 1, 
#  'd': 1, 'o': 1, 'v': 1, 'l': 1, 'a': 3, 'z': 1, 'y': 1
# }

# If you're curious as to why we need to check if the letter is in the
# dictionary, try uncommenting this code and see what happens:

# letter_counts = {}
# for letter in text:
#   letter_counts[letter] = letter_counts[letter] + 1

# In the assignment above, our right hand expression tries to access the value
# for a key that has not been added yet. This causes an error.

# @TASK: Complete this exercise.

print("")
print("Function: count_words_by_length")

# Write this function that counts the number of words by how many letters they
# have. For example:

# words:  ["hat", "cat", "I", "bird"]
# result: {3: 2, 1: 1, 4: 1}
# Since there are two words of length 3, etc.

def count_words_by_length(words):
  pass
  result = {}  # This will store the counts of words grouped by their length
  for word in words:
      length = len(word)  # Find the length of the word
      if length not in result:
          result[length] = 1  # Initialize with 1 if the length is not in the dictionary
      else:
          result[length] += 1  # Increment the count if the length already exists in the dictionary
  return result

check_that_these_are_equal(
  count_words_by_length(["hat", "cat", "I", "bird"]),
  {3: 2, 1: 1, 4: 1}
)

check_that_these_are_equal(
  count_words_by_length(["four", "four", "four", "one"]),
  {4: 3, 3: 1}
)


def count_words_by_length(words):
    result = {}  # The dictionary to store the counts of words grouped by their length.
                 # Key: Length of the words (e.g., 3 for "cat").
                 # Value: Number of words with that length.

    for word in words:  # Loop through each word in the input list.
        length = len(word)  # Calculate the length of the current word (this is the key in the dictionary).

        if length not in result:  # Check if this word length is not already a key in the dictionary.
            result[length] = 1  # Assign the key (word length) with an initial value of 1.
                               # This means we've seen one word with this length so far.
        else:
            result[length] += 1  # Increment the value (count) for this key because another word of the same length is found.

    return result  # Return the dictionary containing the word lengths as keys and their counts as values.

# Test cases
check_that_these_are_equal(
    count_words_by_length(["hat", "cat", "I", "bird"]),
    {3: 2, 1: 1, 4: 1}  # Expected result: Two words of length 3, one of length 1, one of length 4.
)

check_that_these_are_equal(
    count_words_by_length(["four", "four", "four", "one"]),
    {4: 3, 3: 1}  # Expected result: Three words of length 4, one of length 3.
)


# Once you're done, move on to 039_challenge_1_example.py
