#Write a Python program to Read/Write to a File
with open("file.txt", 'w') as file:
    file.write("Hello, this is some content written to the file.")

with open("file.txt", 'r') as file:
    content = file.read()
    print("Content read from the file:")
    print(content)
