# Given a nested dictionary representing a file system structure, write a function that takes a path as a string (e.g., "/home/user/documents") and returns the corresponding nested dictionary object. Handle cases where the path doesn't exist

def access_nested_dict(file_system, path):
    current = file_system
    for directory in path.strip('/').split('/'):
        if directory in current:
            current = current[directory]
        else:
            return None
    return current

# Example usage:
fs = {
    'home': {
        'user': {
            'documents': {'file1.txt': {}, 'file2.txt': {}},
            'downloads': {}
        }
    }
}
print(access_nested_dict(fs, '/home/user/documents'))
# Output: {'file1.txt': {}, 'file2.txt': {}}
print(access_nested_dict(fs, '/home/user/pictures'))
# Output: None