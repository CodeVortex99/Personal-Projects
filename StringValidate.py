Counter = False
def Main():
    Text = input('Enter a String: ')
    if len(Text) >= 5 and len(Text) <= 7:
        if Text.upper() == Text:
            if all(items in list(set(Text)) for items in list(Text)):
                if sum(ord(i) for i in Text) in range(420, 600):
                    print('The string is valid.')
                    return True
                else:
                    print('The sum of string codes entered doesn\'t go within the range of 420 - 600')
                    return False
            else:
                print('The string doesn\'t contain unique character')
                return False
        else:
            print('The string entered is not all upper')
            return False
    else:
        print('The string entered doesn\'t go within the length range.')

while not Counter:
    Counter = Main()