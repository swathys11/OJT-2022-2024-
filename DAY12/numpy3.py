import numpy as np         

#create an orginal array
orginal_array = np.array([1,2,3,4,5,6])
print("Orginal_array: ",orginal_array)

#create a view for the array
view_array = orginal_array.view()
print("View of the original array : ",view_array)

view_array[2]=30
print("The modyfied view of the array: ",view_array)
print("Orginal arrayafter modifying the  view : ",orginal_array)

#create a copy of orginal array
copy_array = orginal_array.copy()
print("Copy of the orginal array: ", copy_array)

#modify element in copy array
copy_array[0]=10
print("Modified copy array: ", copy_array)
print("Orginal arrayafter modifying the copy : ",orginal_array)
