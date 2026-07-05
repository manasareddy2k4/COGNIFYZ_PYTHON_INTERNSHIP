print("=== Temperature Converter ===")

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    temperature = float(input("Enter temperature in Celsius: "))
    fahrenheit = (temperature * 9 / 5) + 32
    print("Temperature in Fahrenheit:", fahrenheit, "°F")

elif choice == 2:
    temperature = float(input("Enter temperature in Fahrenheit: "))
    celsius = (temperature - 32) * 5 / 9
    print("Temperature in Celsius:", celsius, "°C")

else:
    print("Invalid choice")
    