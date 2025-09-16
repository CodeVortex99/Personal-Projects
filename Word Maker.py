Word1 = list(input("Word 1: "))
Word2 = list(input("Word 2: "))

count = 0
for i in Word2:
    for j in Word1:
        if i == j:
            Word1.remove(i)
            break
        else:
            count += 0

if count == len(Word1):
    print("Word 1 can be made from Word 2")
else:
    print("Word 1 cannot be made from Word 2")