import random
import string

def generate_random_string(length):
    characters = string.ascii_letters
    return ''.join(random.choice(characters).lower() for i in range(length))

for _ in range(20):
    print(generate_random_string(random.randint(10, 20)))
