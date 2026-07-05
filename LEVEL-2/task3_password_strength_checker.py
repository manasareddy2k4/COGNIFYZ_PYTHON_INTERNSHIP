print("Password Strength Checker")

password = input("Enter your password: ")

length = len(password) >= 8
has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)

if length and has_digit and has_upper:
    print("✅ Strong Password")
else:
    print("❌ Weak Password")