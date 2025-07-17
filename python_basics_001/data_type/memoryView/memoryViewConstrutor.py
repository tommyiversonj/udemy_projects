# Memoryview constructor is used to create a memory view object 
# from an existing object that supports the buffer protocol, such as bytes, 
# bytearray, or other objects that implement the buffer interface.
# Memoryview objects allow you to access the memory of these objects without copying them,
# which can be more efficient for large data sets.
# The memoryview constructor takes a single argument, which is the object you want to create a memory view of.
# Here's an example of how to use the memoryview constructor:

data = bytearray(b"Hello, World!")  # Create a bytearray object
view = memoryview(data)  # Create a memory view of the bytearray
print(view)  # Output: <memory at 0x...> (the exact address will vary)
print(view[0])  # Access the first byte of the memory view (H)
print(view[1:5])  # Access a slice of the memory view (ello)
