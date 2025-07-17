# Python lists are used to store multiple items in a single variable.
# Lists are one of the most commonly used data types in Python. 
# Lists are created using square brackets [] and can contain items of different data types. 
# Lists are mutable, meaning you can change their content without changing their identity.  
# Lists can contain duplicate items and are ordered collections of items.
# Lists can be nested, meaning you can have lists within lists. 
# Lists can be sliced, meaning you can access a range of items in the list.
# Lists can be iterated over, meaning you can loop through the items in the list.
# Lists can be concatenated, meaning you can combine two or more lists into one.        
# Lists can be extended, meaning you can add items to the end of the list.
# Lists can be sorted, meaning you can arrange the items in the list in a specific order.
# Lists can be reversed, meaning you can reverse the order of the items in the list.    
# Lists can be copied, meaning you can create a new list that is a copy of an existing list.
# Lists can be used to store multiple items in a single variable.
# List is like an array in other programming languages, but it can contain items of different data types.

list = ['abcd', 786, 2.23, 'john', 70.2]
tinyList = [123, 'john']
print("List variable: ", list, type(list))
print(list[0])  # Prints the first item of the list
print(list[1:3])  # Prints items starting from index 1 to 2
print(list[2:])  # Prints items starting from index 2 to the end
print(tinyList * 2)  # Prints the list two times
print(list + tinyList)  # Concatenates two lists 