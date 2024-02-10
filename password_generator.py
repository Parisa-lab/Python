import string
import random

def generate_password(length):
    """This function generates a random password
    of a given length using a combination of
    uppercase letters, lowercase letters,
    digits, and special characters"""


    # Define a string containing all possible characters
    pass_chars = string.ascii_letters + string.digits + string.punctuation
    password = ""
    # Generate a password using a random selection of characters
    for i in range(length):
        password = password + random.choice(pass_chars)
    return password

length = int(input("How Long do You Want Your Password to be? "))
password = generate_password(length)
print(password)

