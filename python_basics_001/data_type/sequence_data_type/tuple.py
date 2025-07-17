# Python tuple is another sequence data type that is used to store multiple items in a single variable.
# Tuples are one of the most commonly used data types in Python.
# Tuples are created using parentheses () and can contain items of different data types.
# Tuples are immutable, meaning you cannot change their content after they are created.
# Tuples can contain duplicate items and are ordered collections of items.
# Tuples can be nested, meaning you can have tuples within tuples.
# Tuples can be sliced, meaning you can access a range of items in the tuple.
# Tuples can be iterated over, meaning you can loop through the items in the tuple.
# Tuples can be concatenated, meaning you can combine two or more tuples into one.          
# Tuples can be extended, meaning you can add items to the end of the tuple.
# Tuples can be sorted, meaning you can arrange the items in the tuple in a specific order.
# Tuples can be reversed, meaning you can reverse the order of the items in the tuple.    
# Tuples can be copied, meaning you can create a new tuple that is a copy of an existing tuple.
# Tuples can be used to store multiple items in a single variable.
# Tuples are like lists in other programming languages, but they are immutable and can contain items of different data types.

tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinyTuple = (123, 'john')

print("Tuple variable: ", tuple, type(tuple)) # Prints the tuple and its type
print(tuple[0])  # Prints the first item of the tuple
print(tuple[1:3])  # Prints items starting from index 1 to 2
print(tuple[2:])  # Prints items starting from index 2 to the end
print(tinyTuple * 2)  # Prints the tuple two times
print(tuple + tinyTuple)  # Concatenates two tuples

