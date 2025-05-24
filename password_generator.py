import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    # Base characters
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        return "No characters selected to generate password."

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# --- User Input Section ---
try:
    length = int(input("Enter password length (e.g., 12): "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (e.g., !@#) (y/n): ").lower() == 'y'

    result = generate_password(length, use_uppercase, use_digits, use_symbols)
    print(f"\nGenerated Password: {result}")

except ValueError:
    print("Please enter a valid number for the length.")

