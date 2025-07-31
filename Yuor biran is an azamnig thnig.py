Words = input("Enter words: ")
tempL = Words.split()
Word1 = list(tempL[0])
Word2 = list(tempL[1])
if len(Word1) == len(Word2):
    if all(items in Word1 for items in Word2):
        if Word1[0] == Word2[0] and Word1[-1] == Word2[-1]:
            print("Super Anagram!")
        else:
            print("Huh?")
    else:
        print("Huh?")
else:
    print("Huh?")