# Write a program that validates if a sentence contains specific words in the correct case:
# - Return True if the sentence contains "Python" (exact case)
# - Return False if it only contains "python", "PYTHON", or "PyThOn"
# - Also return False if "Python" appears as part of another word

Line = input("Line: ")
Words = Line.split()
present = False

if "Python" in Words:
    present = True
# else:
#     for i in Words:
#         if i.lower() == "python":
#             if i.islower():
#                 present = False
#                 break
#             elif i.isupper():
#                 present = False
#                 break
#             else:
#                 present = False
#                 break
#         else:
#             present = False
#             break

print(present)