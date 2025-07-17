# Call by reference - in this way of passing variable, a reference to the object in memory is passed.

def modify_list(lst): 
    lst.append(4)
    print("Inside: ", lst)
    
my_list = [1, 2, 3]
modify_list(my_list)
print("outside: ", my_list)