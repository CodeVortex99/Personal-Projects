Text = input('Enter text: ')
TextList = list(Text)
CharList = []

for i in range(len(Text)):
    if TextList[i] in ['a', 'e', 'i', 'o', 'u']:
        CharList.append(i)
        TextList[i] = '@'

ReversedList = CharList[::-1]
for i in ReversedList:
    for j in range(len(TextList)):
        if TextList[j] == '@':
            TextList[j] = Text[i]
            break

Text1 = ''.join(TextList)
print(Text1)