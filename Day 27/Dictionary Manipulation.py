# Write a Python function that takes two dictionaries as input and returns a new dictionary containing all key-value pairs from both dictionaries. If a key exists in both dictionaries, the value from the second dictionary should be used.

def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

# Alternative solution:
# def merge_dicts(dict1, dict2):
#     result = dict1.copy()
#     result.update(dict2)
#     return result

# Example usage:
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}
print(merge_dicts(d1, d2))  # Output: {'a': 1, 'b': 3, 'c': 4}


