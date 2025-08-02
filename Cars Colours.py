Car = input("Car: ")
Cars = []
Carss = {}
while Car:
  Cars.append(Car)
  Car = input("Car: ")
for i in Cars:
  Carss[f"{i}"] = int(Cars.count(f"{i}"))
for key, value in Carss.items():
  print(f"Cars that are {key}: {value}")
