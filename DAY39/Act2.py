import itertools
def generate_permutations():
    letters=['a','e','i','o','u']
    permutations=itertools.permutations(letters)
    for perm in permutations:
        print(''.join(perm))
    generate_permutations()

