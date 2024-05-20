#Write a Python program to generate a random number between 1 and 100 using the random module.
import random
def generate_random_number():
    return random.randint(1, 100)
random_number = generate_random_number()
print("The random number between 1 and 100 is:" ,random_number)
