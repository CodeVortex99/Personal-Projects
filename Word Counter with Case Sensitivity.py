# Write a program that counts occurrences of a target word with different case rules:
# - Count how many times "code" appears in lowercase
# - Count how many times "CODE" appears in uppercase
# - Count how many times "code" appears in mixed case
# - Print the counts in format: "Lowercase: X, Uppercase: Y, Mixed: Z"

Line = input("Line: ")
Words = Line.split()

Lowercase_Count = 0
Uppercase_Count = 0
Mixed_Count = 0

for i in Words:
    if i.lower() == "code":
        if i.islower():
            Lowercase_Count += 1
        elif i.isupper():
            Uppercase_Count += 1
        else:
            Mixed_Count += 1
        break
else:
    print("No code mention detected.")

print(f"Lowercase: {Lowercase_Count},\nUppercase: {Uppercase_Count},\nMixed: {Mixed_Count}")
