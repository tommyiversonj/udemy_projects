# Python range data type is a built-in data type that represents an immutable sequence of numbers.
# It is commonly used for looping a specific number of times in for loops.  
# The range function generates a sequence of numbers, which can be used to iterate over a block of code a specific number of times.
# The range function can take one, two, or three arguments: start, stop, and step.
# The start argument is the first number in the sequence, the stop argument is the number at which the sequence ends, and the step argument is the difference between each number in the sequence.
# The range function returns a range object, which is an immutable sequence of numbers.
# The range object can be converted to a list or tuple using the list() or tuple() functions, respectively.
# The range data type is useful when you need to generate a sequence of numbers for iteration or when you need to create a list or tuple of numbers.
# The range data type is often used in for loops to iterate over a sequence of numbers.
# The range data type is also useful when you need to create a sequence of numbers for mathematical operations or when you need to generate a sequence of numbers for data analysis.
# The range data type is a built-in data type in Python, meaning it is part of the core language and does not require any additional libraries or modules to use.
# The range data type is an immutable sequence of numbers, meaning you cannot change the content of a range object after it is created.
# The range data type is often used in conjunction with other data types, such as lists and tuples, to create more complex data structures.
# The range data type is a powerful tool for generating sequences of numbers and is widely used in Python programming.
# Example of using the range data type in Python
# The range function can be used to generate a sequence of numbers for iteration in a for loop

'''
for i in range(5): # Generates numbers from 0 to 4
    print(i)  # Prints numbers from 0 to 4
    '''
for i in range(2, 5, 2):  # Generates numbers from 1 to 9 with a step of 2
    print(i)  # Prints numbers 1, 3, 5, 7, 9