import random
import string


def generate_password(min_length, numbers=True, special_characters=True):
    """
    Generate a random password with given constraints.

    Args:
        min_length (int): Minimum length of the password.
        numbers (bool): Include numbers in the password.
        special_characters (bool): Include special characters in the password.

    Returns:
        str: Generated password.
    """
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not (meets_criteria and len(pwd) >= min_length):
        new_char = random.choice(characters)
        pwd += new_char

        has_number = has_number or new_char in digits
        has_special = has_special or new_char in special

        meets_criteria = (has_number or not numbers) and (
            has_special or not special_characters
        )

    return pwd


while True:
    try:
        min_length = int(input("Enter the minimum length: "))
        if min_length < 1:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid positive integer.")

has_number = input("Do you want to have numbers (y/n)?").strip().lower() == "y"
has_special = (
    input("Do you want to have special character (y/n)? ").strip().lower() == "y"
)
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)
