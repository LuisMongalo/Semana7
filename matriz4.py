#Multiplicacion de matrices cuadradas 2x2
matrizA = []
matrizB = []
matrizC = []
for i in range(2):
    fila = []
    matrizA.append(fila)
    for j in range(2):
        matrizA[i].append(int(input(f"Digite el valor de la posición [{i+1}][{j+1}] de la matriz A: ")))
        
for i in range(2):
    fila = []
    matrizB.append(fila)
    for j in range(2):
        matrizB[i].append(int(input(f"Digite el valor de la posición [{i+1}][{j+1}] de la matriz B: ")))
        
        
#Multiplicacion de matrices
for i in range(2):
    fila = []
    matrizC.append(fila)
    for j in range(2):
        suma = 0
        for k in range(2):
            suma += matrizA[i][k] * matrizB[k][j]
        matrizC[i].append(suma)
        
print("la matriz resultante es:")
for fila in matrizC:
    print(fila)