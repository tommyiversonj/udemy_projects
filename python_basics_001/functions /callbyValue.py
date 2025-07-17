# call by value − When a variable is passed to a function while calling, the value of actual arguments is copied to the variables representing the formal arguments.

def modify_value(x):
    x = x + 10
    print("Inside function: ", x)
    
a = 5
modify_value(a)
print("Outside function: ", a)  # a remains unchanged
# In this example, the value of `a` is passed to the function, and changes made to `x` inside the function do not affect `a` outside the function. This demonstrates call by value behavior in Python.      
