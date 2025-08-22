import random
import string

def generate_password(length):
    # characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("---- Password Generator ----")
length = int(input("Enter password length: "))

if length < 4:
    print("Password length should be at least 4.")
else:
    print("Your generated password is:", generate_password(length))
