#Write a python program to Delete a file
import os
filename = "file2.txt"

os.remove(filename)
print("File", filename, "successfully deleted.")
