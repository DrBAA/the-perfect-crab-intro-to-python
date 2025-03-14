# Video alternative: https://vimeo.com/954334322/c5a36d4407#t=510

# Here are the data structures we've met so far:

# * Strings: A sequence of characters
# * Lists: A sequence of any item

# We're going to add another one:

# * Dictionaries: A collection of keys mapped to values

# You know how in a dictionary you look up a word and it provides a definition?
# In that sense, the 'word' is the key, and the 'definition' is the value.

# We'll use that example for a programming dictionary too:

my_dictionary = {
  "String": "A sequence of characters",
  "List": "A sequence of any item",
  "Dictionary": "A collection of key-value pairs, allowing for quick lookups",
}

# Note that:
#
# * We use braces `{` and `}` to tell Python that this is a dictionary
# * We use commas `,` to separate pairs
# * We use colons `:` to separate keys and values

# Now let's look something up. It's just like a list:

print("A String is:")
print("  " + my_dictionary["String"])

print("A List is:")
print("  " + my_dictionary["List"])

# @TASK: Add a definition for a "Dictionary" to our dictionary above by editing
# the code around line 20. Then print out the value below.

print("A Dictionary is:")
print("  " + my_dictionary["Dictionary"])

print("\nContents of the whole Dictionary in JSON format:")
print(my_dictionary)

print("\nContents of the whole dictionary in a readable format:")
for key, value in my_dictionary.items():
    print(f"{key}: {value}")


# Once you're done, move on to 038_dict_operations.py
