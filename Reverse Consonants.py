Text = input('Enter Text: ')
TextList = list(Text)
CharList = []

for i in range(len(TextList)):
    if TextList[i] not in ['a', 'e', 'i', 'o', 'u']:
        CharList.append(i)
        TextList[i] = '@'

ReverseL = CharList[::-1]
for i in ReverseL:
    for j in  range(len(TextList)):
        if TextList[j] == '@':
            TextList[j] = Text[i]
            break

print(''.join(TextList))