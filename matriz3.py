#Suma de matrices
"""Leer 2 matrices 3 x 3 y sumar en una matriz resultado"""
matriz1 = []
for i in range(3):
    matriz1.append([])
    for j in range(3):
        matriz1[i].append(int(input(f"Digite el valor de la posición [{i}][{j}]: ")))

matriz2 = []
for i in range(3):
    matriz2.append([])
    for j in range(3):
        matriz2[i].append(int(input(f"Digite el valor de la posición [{i}][{j}]: ")))

matriz_resultado = []
for i in range(3):
    matriz_resultado.append([])
    for j in range(3):
        matriz_resultado[i].append(matriz1[i][j] + matriz2[i][j])

print("Matriz 1:")
for fila in matriz1:
    print(fila)

print("Matriz 2:")
for fila in matriz2:
    print(fila)

print("Matriz Resultado:")
for fila in matriz_resultado:
    print(fila)