k=1
h=1
p=1
matriz = []

n = int(input("Ingrese el tamaño de la matriz cuadradad que desea: "))  #Tamaño de la matriz cuadrada

for f in range(n):              #Creación de la matriz vacia
    matriz.append([])
    for d in range(n):
        matriz[f].append(None)

print("Ingrese los valores de la matriz:")      #Asignación de valores a la matriz
for i in range (n):
    for j in range (n):
        matriz[i][j] = int(input())

i=0
j=-1

while n>=0:
    if k==1:
        if h==1:
            for t in range (n):                     #Rutina para correr filas a la derecha
                j = j+1
                print (matriz[i][j], end=' ')
            h = h+1
        else: 
            for t in range (n):                     #Rutina para correr filas a la izquierda
                j = j-1
                print (matriz[i][j], end=' ')
                
            h = h-1
        n=n-1
        k=k+1
    else:
        if p==1:
            for t in range (n):                     #Rutina para correr columnas hacia abajo
                i = i+1
                print (matriz[i][j], end=' ')
                
            p= p+1
        else: 
            for t in range (n):                     #Rutina para correr columnas hacia arriba
                i = i-1
                print (matriz[i][j], end=' ')
                
            p= p-1
        k=k-1
