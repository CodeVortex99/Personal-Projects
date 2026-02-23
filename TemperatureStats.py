def Main():
    count = 1
    tempList = []
    temp = float(input(f'Enter temperature for day {count}: '))
    tempList.append(temp)  # Add the first temperature to the list
    while count < 7:
        count += 1
        temp = float(input(f'Enter temperature for day {count}: '))
        tempList.append(temp)

    AvgTemp(tempList)
    MaxTemp(tempList)
    MinTemp(tempList)
    SearchTemp(tempList)
    SortTemp(tempList)

def AvgTemp(tempList):
    Avg = 0
    for i in tempList:
        Avg += i
    Avg = Avg // len(tempList)
    print(f'Average temperature: {Avg}°C')

def MaxTemp(tempList):
    Max = 0
    for i in tempList:
        if i > Max:
            Max = i
    print(f'Highest temperature: {Max}°C')

def MinTemp(tempList):
    Min = tempList[0]  # Start with the first temperature
    for i in tempList:
        if i < Min:
            Min = i
    print(f'Lowest temperature: {Min}°C')

def SearchTemp(tempList):
    TempInput = float(input('Enter a temperature to search for: '))
    count = 0
    for i in range(len(tempList)):
        if tempList[i] == TempInput:
            count += 1
    print(f'Temperature {TempInput}°C occured on {count} days.')

def SortTemp(tempList):
    # Create a copy to avoid modifying the original list
    sortedList = tempList.copy()
    for i in range(0, len(sortedList)-1):
        for j in range(0, len(sortedList)-1):
            if sortedList[j] > sortedList[j+1]:
                temporary = sortedList[j]
                sortedList[j] = sortedList[j+1]
                sortedList[j+1] = temporary
    print(f'Sorted temperatures: {sortedList}')

Main()