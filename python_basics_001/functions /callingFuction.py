# Calling a python function only gives it name, specifying the function name followed by parentheses.

def printme(str): # The function definition
    # This function prints the passed string to the console.
    # The function does not return any value.
    print(str)
    return;
#Now we call the function
printme("Hello, I am a function in Python!")
printme("This is another call to the same function.")