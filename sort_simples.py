entrada = str(input())
entrada_separada = entrada.split(" ")
entrada_lida = []

for i in range(len(entrada_separada)):
    numero = int(entrada_separada[i])
    entrada_lida.append(numero)

entrada_organizada = sorted(entrada_lida)

for i in range(len(entrada_lida)):
    print(entrada_organizada[i])
print("")
for i in range(len(entrada_lida)):
    print(entrada_separada[i])