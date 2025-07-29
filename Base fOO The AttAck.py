Code = input("code: ")
lcode = Code.split()
lcode.reverse()
word = ""
Output = []
vowels = ["a", "e", "i", "o", "u"]
if any(item in vowels for item in Code):
    for i in lcode:
        word = i
        if word[0].upper() == i[0]:
            Output.append(word)
else:
    print("Invalid")

space = " "
print(f"says: {space.join(Output).lower()}")