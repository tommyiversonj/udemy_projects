# Using prefix 'b' to create a bytes object in Python
# The 'b' prefix indicates that the following string is a bytes literal.
# Bytes literals are immutable sequences of bytes, which can be used to represent binary data.
# Bytes literals are often used to represent binary data, such as images, audio files, and  # other types of binary files.
# Bytes literals are also used to represent text data in a specific encoding, such as UTF-8 or ASCII.
# Bytes literals are immutable, meaning that once they are created, they cannot be modified.
# Bytes literals are useful when you need to ensure that the content of a data structure cannot be changed.
# Bytes literals are also useful when you need to create a new object with the same
# content but a different identity, such as when you need to create a new bytes object with
# the same content as an existing bytes object.                                 
# Using the 'b' prefix to create a bytes object
# The 'b' prefix indicates that the following string is a bytes literal.
# Bytes literals are immutable sequences of bytes, which can be used to represent binary data.
# Bytes literals are often used to represent binary data, such as images, audio files,
# and other types of binary files.
# Bytes literals are also used to represent text data in a specific encoding, such as UTF-8 or ASCII.
# Bytes literals are immutable, meaning that once they are created, they cannot be modified.
# Bytes literals are useful when you need to ensure that the content of a data structure cannot
# be changed.       


b1 = b'ABCDEFGHIJKLMNOP'
print(b1)  # Output: b'ABCDEFGHIJKLMNOP'
print(type(b1))  # Output: <class 'bytes'>
print(len(b1))  # Output: 16
print(bytes)  # Output: <class 'bytes'>