# Anonymous functions, also known as lambda functions, are a way to create small, unnamed functions in Python. They are often used for short operations that are not reused elsewhere in the code.
# Lambda functions can take any number of arguments but can only have one expression. They are defined using the `lambda` keyword followed by the arguments, a colon, and the expression.
# The following code demonstrates how to create and use a lambda function in Python.        
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8
print((lambda x, y: x * y)(5, 3))  # Output: 15
print((lambda x: x ** 2)(4))  # Output: 16
print((lambda x: x + 10)(5))  # Output: 15
print((lambda x, y: x - y)(10, 4))  # Output: 6
print((lambda x: x / 2)(10))  # Output: 5.0
print((lambda x: x % 3)(10))  # Output: 1
print((lambda x: x // 3)(10))  # Output: 3
print((lambda x: x ** 3)(2))  # Output: 8
print((lambda x, y: x ** y)(2, 3))  # Output: 8
print((lambda x, y: x // y)(10, 3))  # Output: 3        