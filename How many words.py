u_w = []
words = input("Word: ")
num = 0
while words:
  if words not in u_w:
    u_w.append(words)
    words = input("Word: ")
    num += 1
  if words in u_w:
    u_w.append(words)
    words = input("Word: ")

print(f"You know {num} unique word(s)!")