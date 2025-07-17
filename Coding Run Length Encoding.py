#Coding Run Length Encoding

Org_Text = input("Enter the text: ")
Chars = list(dict.fromkeys(Org_Text))

Counts = []
Char = Org_Text[0]
count = 1
for i in Org_Text[1:]:
    if i == Char:
        count += 1
    else:
        Counts.append(count)
        Char = i
        count = 1
Counts.append(count)

RLE = dict(zip(Chars, Counts))
print(RLE)