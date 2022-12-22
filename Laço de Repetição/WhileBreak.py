x = 0
while x < 10:
    print(x)
    x += 1
    if x == 6:
        print(f"x é igual a {x}")
        break
else:
    print("fim while")