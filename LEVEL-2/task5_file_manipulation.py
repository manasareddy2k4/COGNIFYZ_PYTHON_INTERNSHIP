print("File Manipulation")

text = input("Enter some text: ")

file = open("sample.txt", "w")
file.write(text)
file.close()

file = open("sample.txt", "r")
content = file.read()
file.close()

print("File Content:")
print(content)