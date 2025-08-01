# line = input("Line: ")
# words = line.split()

# robot_found = False
# robot_word = None

# for i, word in enumerate(words):
#     if word.lower() == 'robot':
#         robot_found = True
#         robot_word = word  
#         break

# if robot_found:
#     if robot_word.islower():
#         print("There is a small robot in the line.")
#     elif robot_word.isupper():
#         print("There is a big robot in the line.")
#     else:
#         print("There is a medium sized robot in the line.")
# else:
#     print("No robots here.")

line = input("Line: ")
words = line.split()

for i in words:
    if i.lower() == 'robot':
        if i.islower():
            print("There is a small robot in the line.")
        elif i.isupper():
            print("There is a big robot in the line.")
        else:
            print("There is a medium sized robot in the line.")
        break
else:
    print("No robots here.")