Car = input("Cars: ")
Cars = Car.split()
R = 0
B = 0
for car in Cars:
  if "red" == car:
    R += 1
  if "blue" == car:
    B += 1
print(f"red: {R}")
print(f"blue: {B}")