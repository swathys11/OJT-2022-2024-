#Write a Python program that reads a file and prints its content. 
# Handle ‘FileNotFoundError’ and ‘PermissionError’ exceptions.
filename = "file.txt"
try:
    with open(filename, 'r') as file:
        content = file.read()
        print("Content read from", filename, ":")
        print(content)
except FileNotFoundError:
    print("File not found:", filename)
except PermissionError:
    print("Permission denied to read file:", filename)






filename="file.txt"
try: 
    with open(filename,"r") as file:
        content=file.read()
        print("Content read from",filename,":")
        print(content)
except FileNotFoundError:
    print("File not found",filename)
except PermissionError:
    print("Permission denied to read the file",filename)