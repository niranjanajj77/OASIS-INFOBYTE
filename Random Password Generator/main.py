import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ""
    
    if use_letters:
        characters += string.ascii_letters  # a-z, A-Z
    if use_numbers:
        characters += string.digits         # 0-9
    if use_symbols:
        characters += string.punctuation    # !@#$%^&*()
    
    if not characters:
        print("Error: No character types selected!")
        return ""
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


print("🔐 Random Password Generator")
print("-----------------------------")

try:
    length = int(input("Enter password length: "))
    if length <= 0:
        raise ValueError("Length must be positive!")

    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_letters, use_numbers, use_symbols)

    if password:
        print("\n✅ Your generated password is:")
        print(password)
except ValueError as e:
    print(f"Error: {e}")
