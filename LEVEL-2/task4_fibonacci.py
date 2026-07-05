print("Fibonacci Series")

terms = int(input("How many terms do you want? "))

a = 0
b = 1
count = 0

while count < terms:
    print(a, end=" ")

    next_number = a + b
    a = b
    b = next_number

    count = count + 1