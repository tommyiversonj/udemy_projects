# Bytearray by encoding a string using UTF-8 encoding
# Bytearray String is a mutable sequence of bytes, which can be modified after creation.
# Bytearray String is useful when you need to manipulate binary data, such as reading and writing files,
# or when you need to perform operations on binary data that require mutability.
# Bytearray String can be created using the bytearray() constructor or by converting an existing bytes object.
# Bytearray String can be iterated over using a for loop, which allows you to access each byte in the bytearray.
# Bytearray String can also be sliced, concatenated, and modified in place.
value = bytearray("Hello, World!", "utf-8")
print(value)  # Output: bytearray(b'Hello, World!')