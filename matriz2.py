matriz = []

for i in range(2):
    matriz.append([])
    for j in range(2):
        matriz[i].append(int(input(f"Digite el valor de la posición [{i}][{j}]: ")))
for i in matriz:
    print(i)