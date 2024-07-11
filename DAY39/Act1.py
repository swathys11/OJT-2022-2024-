def all_unique_numbers(sequence):
 
    unique_numbers = set(sequence)
    
    return len(unique_numbers) == len(sequence)

print(all_unique_numbers([1, 2, 3, 4, 5]))  
print(all_unique_numbers([1, 2, 3, 3, 5]))  
