# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging than the example.

# Write a function that takes a list of words and returns a report of all the
# words that are longer than 10 characters but don't contain a hyphen. If those
# words are longer than 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

# MY APPROACH
# For this exercise, I am thinking to create 2 functions
# first function filters out words that are longer than 10 characters but don't contain a hyphen then return a report of those words
# 2nd the function checks if those words are longer than 15 characters, and if they are, then they should be shortened to 15 characters and have an ellipsis (...) added to the end. this will use string slicing to slice them to 15 characters, then string append to append another string of 3 dots (...) to the end of the word and add the new string to a new string

# print("")
# print("Function: report_long_words")

# def report_long_words(words):
#   pass


print("")
print("Function: report_long_words")

def report_long_words(words):
  words_over_10_characters = find_words_over_10_characters(words)
  words_at_15_characters_or_less = find_words_over_15_characters(words_over_10_characters)
  report = string_concatenate(words_at_15_characters_or_less)
  return report

def find_words_over_10_characters(words):
  pass
  words_over_10_characters = []
  for word in words: # We go through the lines item by item
    # Inside this loop, `word` is the individual line
    if len(word) > 10 and "-" not in word:
      words_over_10_characters.append(word)
  return words_over_10_characters

# Was originally using "words" as the parameter on this code. also didn't have an else statement.
# due to this, the code didn't work, it was only returning the words which were originally over 15 characters instead of all the words including those over 10 characters
# resolved by changing the parameter to "words_over_10_characters" to ensure the function uses the list of words with over 10 charactes returned in previous code. also added an else statement to add the rest of the words to the new list "words_at_15_characters_or_less" in addition to the shortened words
# Adding the else clause was essential to handle cases where words have more than 10 characters but are 15 characters or fewer. This ensures that these words are included in the new list,

def find_words_over_15_characters(words_over_10_characters):
  words_at_15_characters_or_less = []
  for word in words_over_10_characters:
    if len(word) > 15:
      reduce_to_15_characters = word[0:15]
      shortened_word = reduce_to_15_characters + "..."
      words_at_15_characters_or_less.append(shortened_word)
    else:
      words_at_15_characters_or_less.append(word)
  return words_at_15_characters_or_less


# The reason you needed to include "These words are quite long: " on the second line IN BELOW CODE is because the second line is where you're actually constructing the final string that will be returned as the output.
# First Line (text = "These words are quite long: "):

# This initializes the text variable with the required prefix. However, at this point, it does not yet include the list of words. It simply sets up the starting point for the string.
# Second Line (text = "These words are quite long: " + ", ".join(words_at_15_characters_or_less)):
# This line overwrites the previous value of text. It combines the prefix ("These words are quite long: ") with the result of ", ".join(words_at_15_characters_or_less), which generates a comma-separated list of words.
# Why It’s Necessary:
# Since the second line constructs the final value of text, it must include both:

# The prefix ("These words are quite long: ").

# The list of words formatted as a comma-separated string (", ".join(words_at_15_characters_or_less)).

# If the second line omitted the prefix, the final output would not match the expected result. The first line alone wouldn’t help because its value gets completely overwritten on the second line.

# Initially, I did not have this function in the code. the other functions were returning a list of strings which did not match the expected output. 
# resolved by creating a function that uses string concatenation and join() method to join strings into normal strings separated by a comma instead of a list format
def string_concatenate(words_at_15_characters_or_less):
  text = "These words are quite long: "
  for line in words_at_15_characters_or_less: # We go through lines item by item
    # Inside this loop, `line` is the individual line
    text = "These words are quite long: " + ", ".join(words_at_15_characters_or_less)    
    # text =  text + line # We append the line to our text
    # # text = text + "\n" # We add an `\n`, which means 'new line'
  return text

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py


# SKILLS DEMONSTRATED in the above code - problem-solving and attention to detail

# Problem-solving in this challenge - ability to break a complex task into smaller, more manageable pieces, identify the root causes of issues (like why the code wasn't returning the expected results), and iteratively refine your approach until you arrive at a solution. For example, you recognized that the original implementation wasn’t working because it skipped words shorter than 15 characters, and you figured out how to resolve that by adjusting the parameter and adding an else statement.

# Attention to detail refers to how carefully you analyze the requirements and ensure every part of your code aligns with them. In this challenge, that includes making sure the correct list (words_over_10_characters) is being used, checking both conditions (length and hyphen presence) in the filtering step, and ensuring the output matches the expected format. Spotting subtle issues, like the missing else block or the exact string slicing and concatenation logic, reflects a strong focus on the finer points of the task.

# attention to detail was demonstrated by careful analysis of the requirements and alignment with the task at multiple points throughout this challenge. A key example was when you were explaining your approach before implementing the code.

  # Specifically:

  # When you planned to use a nested if-statement or multiple functions, you carefully thought about breaking the task into manageable parts, ensuring that each step aligned with the requirements (e.g., filtering words over 10 characters but without hyphens, shortening words over 15 characters, appending "..." and building a report).

  # Your initial breakdown of how you'd filter words and handle conditions showed that you were considering the logic needed to meet every requirement.

  # Later, when debugging and realizing that some shorter words were being excluded, you analyzed the issue (e.g., recognizing the need to use words_over_10_characters in find_words_over_15_characters), showing attentiveness to how your code's flow aligned with the problem.

  # In short, both your planning phase and your troubleshooting phase showcase your ability to analyze requirements in detail and ensure your code meets them. It’s the hallmark of a focused and deliberate approach to problem-solving!

# Together, attention to detail and problem solving skills demonstrate persistence, logical thinking, and a methodical approach, which are key traits of an effective coder!


# Debugging - 

# This is a great demonstration of identifying and solving a problem effectively. By realizing that the previous functions were returning a list instead of a properly formatted string, you pinpointed the exact issue and addressed it with the string_concatenate function. Here’s why your solution works so well:

# Alignment with Requirements:

# The expected output required a single string with words separated by commas. Using ", ".join(...) ensures the result matches the format and avoids issues like trailing commas or improper list formatting.

# Efficiency:

# The join() method is the perfect choice for concatenating strings in a list because it’s optimized for exactly this task, making your implementation both clean and efficient.

# Inclusion of Prefix:

# By adding the prefix "These words are quite long: " at the start, you ensure the output aligns fully with the challenge’s requirements, as this phrase was explicitly part of the expected output format.

# Readable and Modular:

# The function is well-written, easy to understand, and reusable. This level of modularity ensures that if requirements change later, adjustments can be made without affecting the rest of the code.

# attention to detail in coding mean making sure the code meets the project brief and expected requirements
# It's about ensuring every part of the code aligns with the project brief, expected requirements, and desired output. This includes:

# Adhering to the Specifications: Making sure your code fulfills all the functional requirements and handles edge cases outlined in the brief.

# Accuracy in Logic: Ensuring the logic of the code matches the expected behavior without missing steps or introducing unintended outcomes.

# Output Format: Matching the format of the output (e.g., prefixes, punctuation, or separators) to what the project specifies.

# Handling Special Cases: Accounting for all scenarios, such as empty inputs, edge cases, or unexpected data.

# Clarity and Readability: Writing code that's well-structured, easy to follow, and modular, so it's easier to maintain or debug.

# You’ve already displayed attention to detail in this challenge by identifying mismatches (like lists versus strings or missing prefixes) and refining your approach to meet expectations.

# This code demonstrated my attention to detail by making sure the code did what it was supposed to do and met the project brief as follows:_ 
  # Write a function that takes a list of words and returns a report of all the # words that are longer than 10 characters but don't contain a hyphen. If those # words are longer than 15 characters, then they should be shortened to 15 # characters and have an ellipsis (...) added to the end.

    # Exactly! You've demonstrated strong attention to detail by ensuring your code faithfully fulfilled the project brief and all its requirements. Specifically:

    # Accurate Filtering: Your code successfully identified words longer than 10 characters that don’t contain a hyphen, which was explicitly stated in the brief.

    # Handling Long Words: You carefully implemented logic to shorten words exceeding 15 characters, adding an ellipsis (...) as required.

    # Output Format Compliance: By creating the string_concatenate function, you ensured the output was a single string with the required prefix ("These words are quite long: ") and properly formatted with comma-separated words.

    # Debugging and Adjustments: Your ability to identify areas where your initial implementation deviated from the expected results, such as missing an else statement or outputting a list instead of a formatted string, demonstrates attention to detail in refining your code to meet specifications.

    # This level of meticulousness ensures that the final program matches both the functional and formatting requirements of the task, a hallmark of polished and professional coding!

# attention to detail does involve not missing any details, but it’s more nuanced than that. It’s about identifying the critical elements that need focus and ensuring those align perfectly with the requirements or expectations. In your coding challenge, for instance, it wasn’t just about remembering every step—it was about understanding the task deeply enough to handle edge cases, format the output as required, and debug when things didn’t match the expected result.

# In short, attention to detail isn’t just about seeing all the details—it’s about recognizing the right details to prioritize and making sure nothing important slips through the cracks.

