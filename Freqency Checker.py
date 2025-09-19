Num = int(input("Enter the number of digits: "))
Digits = input("Enter the digits seperated by comma: ").split(',')

while len(Digits) != int(Num):
    Digits = input("Enter the digits seperated by comma: ").split(',')

Digits = [int(d.strip()) for d in Digits]

Frequency = []
for i in range(0,10):
    Frequency.append(Digits.count(i))

Count = 0
for i in Frequency:
    if i > Count:
        Count = i

print(Count)