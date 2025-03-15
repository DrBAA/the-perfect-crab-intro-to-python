# Video alternative: https://vimeo.com/954334103/0aed500d39#t=0

# Congratulations! You've covered all of the key syntax, concepts, and ideas
# necessary to succeed in your assessment. You can take it now if you like,
# though you might be a little stronger if you do these extra challenges.

# Each challenge focuses on a new technique or approach. It starts with an
# example, and then leads into an exercise.

# We'll start with combining filtering, mapping, and summarising into one
# super-brilliant pipeline.

# I'll demonstrate for you a function that:
#
# * Gets rid of junk data
# * Converts negative integers to positive numbers
# * Creates a graph of how frequently each number shows up
#
# If you've not used the videos so far, you might want to do so for this one. It
# will show you how I build up the program piece by piece.

example_numbers = [1, 2, 3, -2, -2, 2, None, -3, 4, 4, None, 3, 3, 2, 2, 1]

# Desired output:
# 1: xx
# 2: xxxxxx
# 3: xxxx
# 4: xx

# First I'll show you the function that will combine all the other functions
# together to create the graph. This will give you an idea of the flow of the
# program.

def generate_frequency_graph(numbers): # example_numbers is passed to the function as numbers 

# When the generate_frequency_graph(numbers) function is called, the above List example_numbers 
# is passed as an argument as numbers. Inside the function, example_numbers is assigned to the 
# parameter 'numbers'. From this point onward, the variable 'numbers' is used as the parameter for 
# each supporting function called within generate_frequency_graph(numbers).


# The supporting functions within the generate_frequency_graph(numbers) use numbers as their parameter because it serves as the input that allows the functions to perform their specific tasks. Each supporting function is designed to process a specific aspect of the numbers data. By using numbers as a parameter, the functions remain flexible and can work with any list of numbers passed to them.
# In the generate_frequency_graph function, the original example_numbers list is passed down as numbers. As it moves through each supporting function, the numbers variable is transformed at each stage
# Each supporting function transforms the numbers list in some way and returns the modified version, which is passed along to the next step in the sequence.
# Each function uses the modified output of the previous one, ensuring the data flows seamlessly through the program.



  # Calls get_only_integers:
  integers = get_only_integers(numbers) # This function filters out None values from numbers (example_numbers). Returns a list containing only integers.

  # Calls convert_negatives_to_positives:
  positive_integers = convert_negatives_to_positives(integers) # This function processes the list of integers from step 2.
    # Negative numbers are converted to their positive equivalents.
    # Returns a new list with only positive integers.

  # Calls calc_frequency_of_numbers:
  number_frequency = calc_frequency_of_numbers(positive_integers) # This function calculates the frequency of each number in the list from step 3. Returns a dictionary where keys are the unique numbers and values are their frequencies.

  # Calls format_graph:
  graph = format_graph(number_frequency) # This function formats the frequency data into a graph-like output using string multiplication. Returns the formatted graph as a string.

  return graph 
# The return graph statement in the generate_frequency_graph function is written by the programmer and is essential for the function to provide its final output.

# In the generate_frequency_graph function, the line graph = format_graph(number_frequency) calls the format_graph function. This function returns a string representing the formatted frequency graph.

# The generate_frequency_graph function stores that string in the variable graph.

# To ensure that the result of the function is accessible outside of it (when called), the function explicitly uses the return graph statement. This sends the value of the graph variable back to the caller.


# Here we'll filter the List of example_numbers to get rid of the None values and create a new list of integers
def get_only_integers(numbers):
  integers = []
  for number in numbers:
    if number != None:
      integers.append(number)
  return integers

# Here we'll use mapping to convert negative numbers from returned List of integers above to positive numbers
def convert_negatives_to_positives(numbers):
  positive_integers = []
  for number in numbers:
    if number < 0:
      # Note that a negative number multiplied by -1
      # will be its positive equivalent
      positive_integers.append(number * -1)
    else:
      positive_integers.append(number)
  return positive_integers

# Here we'll use dictionary summarising the List positive_integers created above to create a graph of how frequently each
# number shows up
def calc_frequency_of_numbers(numbers):
  number_frequency = {}
  for number in numbers:
    if number not in number_frequency:
      number_frequency[number] = 1
    else:
      number_frequency[number] += 1
  return number_frequency

# Here we'll use summarising and mapping in the same loop to format the graph.
# he reason we use "number_frequency" as the parameter in the below code (format_graph) instead of "numbers" as in previous functions is because the format_graph functions works with different type of data as input unline in the other functions
# This function takes the dictionary output (number_frequency) from the previous function as its input. The dictionary contains the frequency of each number, and this is the data needed to construct the graph.
# The key-value pairs in the dictionary are used to generate the graph string.
# If we used numbers in format_graph, it wouldn't work, because by this point, numbers is no longer a list—it's a dictionary of frequencies.

# The function format_graph takes a dictionary (number_frequency) as its input. The keys in the dictionary represent numbers, and the values represent how frequently each number appears. The function's goal is to create a textual "graph" showing each number and its frequency, represented by a line of "x" characters.
def format_graph(number_frequency):
  graph = ""
  for number in number_frequency:
    # Note the cool use of 'string multiplication' here!
    # 'x' * 3 will give you 'xxx'
    graph += f"{number}: {'x' * number_frequency[number]}\n"
  return graph

# Output:
# The generate_frequency_graph function calls all the other functions that are defined to support it, returns the final graph string, which is then printed to the console.
# Now let's use it!
print("RESULTS FOR generate_frequency_graph function")
print(generate_frequency_graph(example_numbers))

# @TASK Run this file to see the result.

# Once you're done, move on to 040_challenge_1_exercise.py
