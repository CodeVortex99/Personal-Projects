Digits = int(input("Number of Digits: "))
Number = (input("Enter the number with those many Digits: "))

Array = [0] * 10

for i in (Number):
    Array[int(i)] += 1

Max = max(Array)
Frequent = [I for I, frequency in enumerate(Array) if frequency == Max]

if len(Frequent) == 1:
    print(f"Most frequently occured number is: {Array.index(max(Array))}")
else:
    print(f"Numbers with the highest freq {Max} are: {','.join(map(str, Frequent))}")