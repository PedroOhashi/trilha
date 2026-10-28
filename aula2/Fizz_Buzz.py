def fizzbuzz(n, lista_print):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            lista_print.append("FizzBuzz")
        elif i % 3 == 0:
            lista_print.append("Fizz")
        elif i % 5 == 0:
            lista_print.append("Buzz")
        else:
            lista_print.append(str(i))

    return lista_print
lista_print = []
n = int(input())
lista_print = fizzbuzz(n, lista_print)

print(lista_print)