import re

password = input("Enter your password: ")

# Conditions
min_length = len(password) >= 8
has_number = re.search(r"\d", password)
has_uppercase = re.search(r"[A-Z]", password)
has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

# Checking strength
if min_length and has_number and has_uppercase and has_special:
    print("✅ Strong Password")
else:
    print("❌ Weak Password")
    print("\nPassword must contain:")
    if not min_length:
        print("- At least 8 characters")
    if not has_number:
        print("- At least one number")
    if not has_uppercase:
        print("- At least one uppercase letter")
    if not has_special:
        print("- At least one special character")