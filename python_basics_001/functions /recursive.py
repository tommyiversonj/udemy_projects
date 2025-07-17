# Recursive functions are functions that call themselves in order to solve a problem.
# They are useful for tasks that can be defined in terms of smaller sub-tasks, such as calculating factorials or traversing data structures like trees.
# The following code demonstrates how to define and use a recursive function in Python.         
def factorial(n):
    """This function calculates the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 
    print(factorial(5))  # Output: 120
    print(factorial(0))  # Output: 1
    print(factorial(1))  # Output: 1
    print(factorial(3))  # Output: 6            
    print(factorial(4))  # Output: 24
    print(factorial(6))  # Output: 720
    print(factorial(7))  # Output: 5040
    print(factorial(8))  # Output: 40320
    print(factorial(9))  # Output: 362880
    print(factorial(10))  # Output: 3628800         