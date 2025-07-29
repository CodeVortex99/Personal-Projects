Code = input("code: ")
lcode = Code.split()
lcode.reverse()
word = ""
Output = []
for i in lcode:
    word = i
    if word[0].upper() == i[0]:
        Output.append(word)

space = " "
print(f"says:"{space.join(Output).lower()})