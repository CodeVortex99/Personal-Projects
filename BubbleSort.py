List = [5, 3, 8, 4, 2, 1, 6, 7, 9, 10, 0, 100, -100, -100000]
for i in range(len(List)-1):
    Swapped = False
    for j in range(len(List)-i-1):
        if List[j] > List[j+1]:
            List[j], List[j+1] = List[j+1], List[j]
            Swapped = True
    if not Swapped:
        break
print(List)