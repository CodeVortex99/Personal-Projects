Text = input('Enter Text: ')
TextList = list(Text)
CharList = []

for i in range(len(Text)):
    if TextList[i] in ['a', 'e', 'i', 'o', 'u']:
        CharList.append(TextList[i])
        TextList[i] = '@'

NewList = []
for i in range(len(CharList)):
    if CharList[i] == 'a':
        NewList.append('u')
    elif CharList[i] == 'e':
        NewList.append('o')
    elif CharList[i] == 'i':
        NewList.append('i')
    elif CharList[i] == 'u':
        NewList.append('a')
    elif CharList[i] == 'o':
        NewList.append('e')

for i in range(len(NewList)):
    for j in range((len(TextList))):
        if TextList[j] == '@':
            TextList[j] = NewList[i]
            break

print(''.join(TextList))