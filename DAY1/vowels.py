vowel=input("Enter a string:")
count = 0
for i in vowel:
    if i in 'aeiouAEIOU':
        count += 1
        print(count)