# Function arguments are the values or variables passed into a function when it is called. The behavior of a function often depends on the arguments passed to it.
# In Python, functions can accept arguments in various ways, including by value and by reference.
# Call by value − When a variable is passed to a function while calling, the value of actual arguments is copied to the variables representing the formal arguments.
# Call by reference - in this way of passing variable, a reference to the object in memory is passed.
# The following code snippets demonstrate how to define functions, call them, and how arguments can be passed by value or by reference.
# The following code demonstrates how to define and call a function in Python.
# The function definition starts with the keyword `def`, followed by the function name and parentheses containing any parameters.
# The function body contains the code that will be executed when the function is called.
# The function can return a value using the `return` statement, but it is optional.

def greetings(name):
    print(f"Hello, {name}! Welcome to Python programming!")
    return
greetings("Alice")
greetings("Bob")
# The above code defines a function `greetings` that takes a parameter `name` and prints a greeting message.