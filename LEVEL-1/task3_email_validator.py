print("=== Email Validator ===")

email = input("Enter your email: ")

if "@" in email and ".com" in email:
    print("Valid Email")
else:
    print("Invalid Email")