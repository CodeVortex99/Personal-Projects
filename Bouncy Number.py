Num = input('Enter an integer: ')

while int(Num) <= 0:
    Num = input('Enter an integer: ')

NumList = list(Num)
# print(NumList)
Increasing = 0
Decreasing = 0

for i in range(len(NumList)):
    if i != len(Num)-1:
        if int(NumList[i+1]) > int(NumList[i]):
            Increasing += 1
        elif int(NumList[i+1]) < int(NumList[i]):
            Decreasing += 1
    else:
        pass

if Increasing == Decreasing:
    print('Its a perfectly bouncy number.')
elif Increasing > 0 and Increasing == len(Num)-1 and Decreasing == 0:
    print('It is an Increasing Number.')
elif Decreasing > 0 and Decreasing == len(Num)-1 and Increasing == 0:
    print('It is a Decreasing Number.')
else:
    print('It is a bouncy number.')