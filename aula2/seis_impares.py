x = int(input())
encontrado = 0

while encontrado < 6:
    if x % 2 == 1:
        print(x)
        encontrado += 1
    x += 1