# Lists mutable is a key feature of Python lists, allowing you to modify their contents without changing their identity.
# Python mutable data types allow you to change their content without changing their identity.
# Python mutable data types include lists, dictionaries, and sets.
# Python mutable data types are useful when you need to change the content of a data structure without creating a new one.

# list is a mutable data type, meaning you can change its content without changing its identity.
my_list = ['1', '2', '3']
print("Original list:", my_list)    
print("Type of my_list:", type(my_list)) # Prints the type of my_list
print("Original list ID:", id(my_list)) # Prints the ID of my_list

my_list.append('4')  # Adds 'orange' to the end of the list
print("Modified list:", my_list)  # Prints the modified list
print("Modified list ID:", id(my_list))  # Prints the ID of my_list after


