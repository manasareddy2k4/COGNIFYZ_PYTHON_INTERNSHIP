print("=== Palindrome Checker ===")

word = input("Enter a word: ")

reverse = word[::-1]

if word == reverse:
    print("The given word is a palindrome")
else:
    print("The given word is not a palindrome")