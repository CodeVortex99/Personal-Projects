Dictionary = {}
Line = input("Name and colour: ")
while Line:
    Name, Colour = Line.split()
    Dictionary[Name] = Colour
    Line = input("Name and colour: ")

for Name in Dictionary:
  print(f"{Name} {Dictionary[Name]}")