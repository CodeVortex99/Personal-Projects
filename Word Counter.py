Line = input("Enter line: ")
List = [], Dict = {}
while Line:
    List.extend(Line.split())
    Line = input("Enter line: ")
List.sort()
List1 = []
for x in List:
    if x not in List1:
        Dict[f"{x}"] = int(List.count(f"{x}"))
for key, value in Dict.items():
    print(f"{key} {value}")