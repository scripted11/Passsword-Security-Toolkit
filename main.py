import secrets
import string 
import hashlibs

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation

    while True:
        try:
            length = int(input("Enter password length: "))

            if length < 4:
                print("Password must be at least 4 characters long.")
                continue

            break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    password = ''.join(secrets.choice(characters) for _ in range(length))

    print(f"Generated Password: {password}")

def check_password_strength(password):
    length = len(password)

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if length < 8:
        return "Weak"

    elif length >= 12 and has_upper and has_lower and has_digit and has_special:
        return "Strong"

    elif length >= 8 and (has_upper or has_lower) and (has_digit or has_special):
        return "Moderate"

    else:
        return "Weak"
    
def generate_sha256(text):
    return hashlib.sha256(text.encode()).hexdigest()

def security_report(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    strength = check_password_strength(password)
    hash_result = generate_sha256(password)

    print("\n" + "=" * 40)
    print("  Security Report")
    print("=" * 40)

    print(f"password Length :  {length}")
    print(f"Uppercase Letters: {'Yes'if has_upper else 'No'}")
    print(f"Lowercase Letters: {'Yes'if has_lower else 'No'}")
    print(f"Numbers: {'Yes ' if has_digit else 'No'} ")
    print(f"Special Characters  : {'Yes' if has_special else 'No'}")

    print(f"\nPassword Strength: {strength}")
    print(f"SHA-256 Hash: {hash_result}")

    print("=" * 40)



def menu():
    print("=" * 40)
    print("Password Security Toolkit")
    print("=" * 40)
    print("1. Generate Strong Password")
    print("2. Check Password Strength")
    print("3. Generate SHA-256 Hash")
    print("4. Security Report")
    print("5. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        generate_password()
 
    elif choice == "2":
        password = input("Enter password: ")
        result = check_password_strength(password)
        print(f"Password Strength: {result}")

    elif choice == "3":
        text = input("Enter text:")
        hash_result = generate_sha256(text)

        print("\nSHA-256 Hash:" )
        print(hash_result)

    elif choice == "4":
        password = input("Enter password for security report: ")
        security_report(password)

    elif choice == "5":
     print("Goodbye!")
     exit()

    else:
     print("Invalid option")

while True:
    menu()
