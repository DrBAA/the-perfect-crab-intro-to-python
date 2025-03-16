# Video alternative: https://vimeo.com/954334279/dd2abfbdd7#t=760

from lib.helpers import check_that_these_are_equal

# We're going to show you some more things you can do with strings.

# == Length ==

# Strings contain characters. We can find the number of characters a string has.
# This is called the length.

# You can get the length using a function pre-loaded into Python called `len`

# Here's an example:

length = len("Hello!")
print(f"The string is {length} characters long")

# @TASK: Try it out yourself by changing the string "Hello!" above, and then
# running this code with:
#
#   python 024_string_operations.py
#
# You'll see some other test output at the bottom. You can ignore this until
# later in the exercise.

# == Replace ==

# Let's say you wanted to turn this:

"Hello, YOUR_NAME!"
"Hello, BETH!"

# Into this:

"Hello, Kay!"

# For this, you could use the `replace` function:

old_string = "Hello, YOUR_NAME!"
new_string = old_string.replace("YOUR_NAME", "Kay")
newer_string = old_string.replace("Hello, YOUR_NAME", "Hi Beth")

# Uncomment this next line to see the result:
print("old string ", old_string)
print("new string is ", new_string)
print("newer string is: ", newer_string)

# # You'll notice here that the function is coming in a different place. Let's
# # compare `len` and `replace`:

my_string = "hello"

len(my_string)              # <-- Independent Function
my_new_string = my_string.replace("h", "w") # <-- Method Function
print(my_new_string)

# STRING SLICING TO REMOVE A LETTER(S) FROM A STRING
print("STRING SLICING TO REMOVE A LETTER(S) FROM A STRING")
sling_to_slice = "Birmingham City"
sliced_string = sling_to_slice[11:]
print("sliced_string", sliced_string)

def slice_out_city(keep_birmingham):
  # keep the word Birmingham 
  # Find the starting index of "birmingham"
  start_index = keep_birmingham.lower().find("birmingham")

  # Find the ending index of "birmingham"
  end_index = start_index + len("birmingham")

  # Slice to extract "birmingham"
  result = keep_birmingham[start_index:end_index]
  return result

print("results after slicing out the word city are: ", slice_out_city("Birmingham City"))


def slice_out_city(keep_birmingham):
    # Validate input
    if not isinstance(keep_birmingham, str) or not keep_birmingham.strip():
        return "Invalid input: Please provide a non-empty string."

    # Convert string to lowercase and find "birmingham"
    start_index = keep_birmingham.lower().find("birmingham")

    # Handle case when "birmingham" is not found
    if start_index == -1:
        return "The word 'birmingham' is not found in the input."

    # Find the ending index of "birmingham"
    end_index = start_index + len("birmingham")

    # Slice to extract "birmingham"
    result = keep_birmingham[start_index:end_index]

    # Return the cleaned result
    return result.strip()

print("results after slicing out the word city are: ", slice_out_city("London City"))



def slice_out_city(keep_birmingham):
    # Validate input
    if not isinstance(keep_birmingham, str) or not keep_birmingham.strip():
        return "Invalid input: Please provide a non-empty string."

    # Convert string to lowercase and find "birmingham"
    start_index = keep_birmingham.lower().find("birmingham")

    # Handle case when "birmingham" is not found
    if start_index == -1:
        return "The word 'birmingham' is not found in the input."

    # Find the ending index of "birmingham"
    end_index = start_index + len("birmingham")

    # Slice to extract "birmingham"
    result = keep_birmingham[start_index:end_index]

    # Return the cleaned result
    return result.strip()

print("results after slicing out the word city are: ", slice_out_city(" "))




def slice_out_city(keep_birmingham):
    # Validate input
    if not isinstance(keep_birmingham, str) or not keep_birmingham:
        return "Invalid input: Please provide a non-empty string."
    
    # Convert string to lowercase and find "birmingham"
    start_index = keep_birmingham.lower().find("birmingham")

    # Handle case when "birmingham" is not found
    if start_index == -1:
        return "The word 'birmingham' is not found in the input."

    # Find the ending index of "birmingham"
    end_index = start_index + len("birmingham")

    # Slice to extract "birmingham"
    result = keep_birmingham[start_index:end_index]

    # Return the cleaned result
    return result

print("results after slicing out the word city and stripping traling spaces are:", slice_out_city("I am going to Birmingham City"))


# # Why the difference? It's a little complicated.
# #
# # What you need to know for now is that some functions come in one style like
# # `len`, and some come in the other style like `replace`. The latter are called
# # 'methods'.

# # == Upper and Lowercase ==

# # When you're doing the Makers assessment, you're quite likely to be asked to do
# # something you've not done before. This is very normal.

# # In an engineering job, and increasingly in any job, you have to get
# # comfortable with looking up how to do things.

# # We'll practice this here.

# # @TASK Complete these exercises:

# # == Exercise One ==

# print("")
# print("Function: uppercase")

# # Search for 'python make string uppercase'

def make_uppercase(string):
  # Return the string in uppercase
  pass
  return string.upper()

check_that_these_are_equal(
  make_uppercase("hello"), "HELLO")

check_that_these_are_equal(
  make_uppercase("World"), "WORLD")

# # == Exercise Two ==

print("")
print("Function: lowercase")

# Search for 'python make string lowercase'

def make_lowercase(string):
  # Return the string in lowercase
  pass
  return string.lower()

check_that_these_are_equal(
  make_lowercase("HELLO"), "hello")

check_that_these_are_equal(
  make_lowercase("World"), "world")

# # == Exercise Three ==

print("")
print("Function: strip_whitespace")

# Search for 'python remove whitespace from string'

def strip_whitespace(string):
  # Return the string with any whitespace removed from the start and end
  # Use python built-in strip() method - looks at your string and checks for any leading (at the start) or trailing (at the end) whitespace, including spaces, tabs (\t), or newline characters (\n).
  # It’s especially useful in scenarios where the input might have inconsistent spacing—like user inputs, data from files, etc.'
  pass
  return string.strip()

check_that_these_are_equal(
  strip_whitespace("hello "), "hello")

check_that_these_are_equal(
  strip_whitespace(" hello world "), "hello world")

# When you're done, move on to 025_string_concatenation.py
