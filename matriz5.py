#Dada una matriz cuadrada, converirla a una matriz de identidad
n = int(input("Ingrese el tamaño de la matriz cuadrada: "))
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

print("La matriz de identidad es:")
for fila in matriz:
    print(fila)