Line = input("Line: ")
Words = Line.split()

for i in Words:
    if i.lower() == "password":
        if i.islower():
            print("Weak security mention detected.")
        elif i.isupper():
            print("Strong security mention detected.")
        else:
            print("Medium security mention detected.")
        break
else:
    print("No password mention detected.")
