"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""
#reading notes
# modes
# r - read (default)
# w - write
# a - append (data written at the end)
# r+ - read and 
# add b - opens in binary mode for files that have more than just text
# a+ - creates file if it doesn't exsist and opens it in append mode


# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('foo.txt') as foo:
    print(foo.read())

# foo.read() checking to see if file closed, should return ValueError

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE

with open('bar.txt', 'w+') as bar:
    bar.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.")

with open('bar.txt') as bar:
    print(bar.read())