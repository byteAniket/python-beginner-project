# -------------------> This is a simple passoword generator program that creates a random password based on user-defined criteria. <-------------------
#  Password Generator Project
#  Made by Aniket
# Python beginner project
import random
print("Welcome to the Password Generator!")
length = int(input("Enter the desired length of your password: "))
include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
include_special = input("Include special characters? (yes/no): ").lower() == 'yes'
characters = ""
if include_uppercase:
    characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if include_lowercase:
    characters += "abcdefghijklmnopqrstuvwxyz"
if include_digits:
    characters += "0123456789"
if include_special:
    characters += "!@#$%^&*()-_=+[]{}|;:,.<>?/"
if not characters:
    print("Error: At least one character type must be included.")
else:
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated Password: {password}")
