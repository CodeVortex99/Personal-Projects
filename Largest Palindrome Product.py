Product = []
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i*j
        if str(product) == str(product)[::-1]:
            Product.append(product)

print(Product[-1])
print(max(Product))