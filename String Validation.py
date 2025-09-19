Text = input("Enter text: ")

def LengthValidation(Text):
    if len(Text) >= 5 and len(Text) <= 7:
        UCValidation(Text)
    else:
        print("The string entered doesn't go within the length range.")

def UCValidation(Text):
    TUpper = Text.upper()
    if TUpper == Text:
        UniqueValidation(Text)
    else:
        print("The string entered is not all upper")

def UniqueValidation(Text):
    UniqueList = list(Text)
    UniqueSet = list(set(Text))

    if all(items in UniqueSet for items in UniqueList):
        CharacterCodeCheck(Text)
    else:
        print("The string doesn't contain unique character")

def CharacterCodeCheck(Text):
    TextList = list(Text)
    count = 0
    for i in TextList:
        count += ord(i)
    
    if count in range(420,600):
        print("The string entered is Valid.")
    else:
        print("The sum of string codes entered doesn't go within the range of 420 - 600")

LengthValidation(Text)