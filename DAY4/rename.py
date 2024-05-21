#Write a Python program that renames a file named ‘old_name.txt to’ ‘new_name.txt’.
# import os
# old_name = 'file.txt'
# new_name = 'file3.txt'
# os.rename(old_name, new_name)
# print("File ",old_name," renamed to ", new_name," successfully.")







import os
old_name="file3.txt"
new_name="file.txt"
os.rename(old_name,new_name)
print("File ",old_name,"Renamed to ",new_name, " successfully.")