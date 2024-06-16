import random
import string


def validate_min_length():
    while True:
        try:
            # Prompt user to enter minimum length and convert to int
            min_length = int(input("Enter the minimum length: "))

            # Ensure the minimum length is positive
            if min_length < 1:
                raise ValueError

            return min_length
        except ValueError:
            # Handle invalid input
            print("Please enter a valid positive integer.")


def validate_yes_no(prompt):
    while True:
        # Prompt user for a yes/no response
        response = input(prompt).strip().lower()

        # Check if response is either 'y' or 'n'
        if response in {"y", "n"}:
            return response == "y"

        # Handle invalid input
        print("Please enter 'y' or 'n'.")


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
        # Add digits to character pool if numbers option is True
        characters += digits
    if special_characters:
        # Add special characters to character pool if special_characters option is True
        characters += special

    pwd = []
    has_number = False
    has_special = False

    while (
        len(pwd) < min_length
        or not has_number
        and numbers
        or not has_special
        and special_characters
    ):
        # Randomly select a character from the pool
        new_char = random.choice(characters)
        pwd.append(new_char)

        # Check if the new character is a number
        if new_char in digits:
            has_number = True
        # Check if the new character is a special character
        elif new_char in special:
            has_special = True

    return "".join(pwd)


def main():
    min_length = validate_min_length()
    has_number = validate_yes_no("Do you want to have numbers (y/n)? ")
    has_special = validate_yes_no("Do you want to have special character (y/n)? ")

    # Generate a password using the specified constraints
    pwd = generate_password(min_length, has_number, has_special)

    # Display the generated password
    print(f"\nThe generated password is: {pwd}\n")


if __name__ == "__main__":
    main()
