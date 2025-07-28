steps = int(input("How many steps? "))
print("__")
i = ""
count = 0
while count != steps-1 :
  i += "  "
  print(i+"|_")
  count += 1
j = ""
num = 0
StepC = steps * 2
while num != StepC:
  j += "_"
  num += 1
print(j+"|")