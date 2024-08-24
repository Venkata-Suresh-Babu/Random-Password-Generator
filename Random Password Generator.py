import random
import string

def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Take user input for password length
try:
    password_length = int(input("Enter the desired password length: "))
    if password_length <= 0:
        print("Please enter a positive integer for password length.")
    else:
        generated_password = generate_password(password_length)
        print(f"Generated password: {generated_password}")
        print("")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")