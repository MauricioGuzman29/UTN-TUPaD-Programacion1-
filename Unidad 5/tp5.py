
#-----------------Trabajo Practico 5-------------------------

#------------------Ejercicio 1-------------------------------

notas=[1,6,5,9,8,7,9,10,5,6]

suma = 0 

for nota in notas:
    print(nota, end=" ")
    

promedio = sum(notas) / len(notas)
maxima =max(notas)
minima =min(notas)

print(f"\nEl promedio de las notas es: {promedio}")
print(f"La nota maxima es: {maxima} y la nota minima es: {minima}")
print("-----------------------------------------------------------------------------------")

#-----------------------------------------------------------
#------------------Ejercicio 2------------------------------
productos = []

for i in range(5):
    producto= input(f"Ingrese el producto {i+1}: ")
    productos.append(producto)

print()
print(productos)

#Lista ordenada
lista_ordenada = sorted(productos)
print(lista_ordenada)

#Eliminar producto
eliminar = input("\nIndique que producto desea eliminar: ")
if eliminar in productos:
    productos.remove(eliminar)
else:
    print("El producto no se encuentra en la lista.")

print(productos)
print("-----------------------------------------------------------------------------------")

#----------------------------------------------------------
#------------------Ejercicio 3------------------------------
import random

pares=[]
impares=[]
cant_pares = 0
cant_impares = 0

numeros_aleatorios = [random.randint(1,100) for i in range(15)]
print(numeros_aleatorios)

for num in numeros_aleatorios:
    if num % 2 == 0:
        pares.append(num)
        cant_pares += 1
    else:
        impares.append(num)
        cant_impares += 1

print("Numeros pares: ", pares, "Cantidad: ", cant_pares)
print("Numeros impares: ", impares, "Cantidad: ", cant_impares)
print("-----------------------------------------------------------------------------------")

#-----------------------------------------------------------
#------------------Ejercicio 4------------------------------

datos = [1,3,5,3,7,1,9,5,3]
datos_sin_repetir = []

for dato in datos:
    if dato not in datos_sin_repetir:
        datos_sin_repetir.append(dato)
print(f"Los datos sin repetir son: {datos_sin_repetir}\n")
print("-----------------------------------------------------------------------------------")
#-----------------------------------------------------------
#------------------Ejercicio 5------------------------------

estudiantes_presentes = ["Juan", "Jose","Pedro","Mauricio","Patricio","Roberto", "Carlos", "Pablo"]
print("Estudiantes presentes:")
for estudiantes in estudiantes_presentes:
    print(estudiantes, end=" ")
print()

print("\nGestión de estudiantes")
op =input("Ingrese opcion deseada. (A): Agregar estudiante, (E): Eliminar estudiante: ").upper()


if op == "A":
    otro_estudiante = input("\nIngrese nombre del estudiante que desea agregar a la clase: ").title()
    estudiantes_presentes.append(otro_estudiante)
elif op == "E":
    estudiante = input("\nIngrese nombre del estudiante que desea quitar de la clase: ").title()
    if estudiante in estudiantes_presentes:
            estudiantes_presentes.remove(estudiante)
    else: 
        print("Ese estudiante no esta presente")
else:
        print("Opcion incorrecta \n")
        
            
print("Lista actualizada: ")
for estudiantes in estudiantes_presentes:
    print(estudiantes, end=" ")
print()
print("-----------------------------------------------------------------------------------")
#-----------------------------------------------------------
#------------------Ejercicio 6------------------------------

numeros = [1,2,3,4,5,6,7]

ultim_num = numeros[-1] #accede al ultimo numero
resto = numeros[:-1] #accede a todos los elementos de la listas menos el ultio numero

nueva_lista= [ultim_num] + resto 
print(nueva_lista)
print("-----------------------------------------------------------------------------------")
#-----------------------------------------------------------
#------------------Ejercicio 7------------------------------

temperaturas = [
    [2, 15],
    [3, 19],
    [3, 18],
    [5, 22],
    [8, 26],
    [3, 15],
    [4, 17]
]

for fila in temperaturas:
    for temperatura in fila:
        print(temperatura, end=" ")
    print()

minimas = []
for minima in temperaturas:
    minimas.append(minima[0])
promedio_minimas= sum(minimas)/ len(minimas)
print("El promedio de las temperaturas minimas es: ", round(promedio_minimas, 2))

maximas = []
for maxima in temperaturas:
    maximas.append(maxima[1])
promedio_maximas= sum(maximas)/ len(maximas)
print("El promedio de las temperaturas maximas es: ", round(promedio_maximas, 2))

#Amplitud
amplitudes = []
for temperatura in temperaturas:
    amplitudes.append(temperatura[1]-temperatura[0])

amplitud_mayor = max(amplitudes)

dia = (amplitudes.index(amplitud_mayor) + 1)
dias_semana=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado","Domingo"]
print(f"El dia {dias_semana[dia-1]} se registro la amplitud mas alta de la semana de: {amplitud_mayor}°")
print("-----------------------------------------------------------------------------------")
#-----------------------------------------------------------
#------------------Ejercicio 8------------------------------

notas = [
    [2, 10, 7],
    [8, 8, 6], 
    [6, 9, 7],  
    [5, 10, 5],
    [6, 6, 7]   
]

for fila in notas:
    for nota in fila:
        print(nota, end=" ")
    print()

#Promedio de cada estudiante

print("Promedio por cada estudiante")
for i in range(5): #recorre cada fila:
    suma = 0 
    for j in range(3): 
        suma += notas[i][j]
    promedio = suma / 3
    print(f"Promedio estudiante {i+1}: {promedio:.2f}")

print("\nPromedio por cada materia")
for i in range(3): #columna
    suma = 0 
    for j in range(5):
        suma += notas[j][i]
    promedio = suma / 5
    print(f"Promedio materia {i+1}: {promedio:.2f}")
print("-----------------------------------------------------------------------------------")

#-----------------------------------------------------------
#------------------Ejercicio 9------------------------------


tablero=[]

for i in range(3):
    fila = [] # crea 3 filas
    for j in range(3): #por cada fila coloca 3 "-"
        fila.append("-")
    tablero.append(fila) #agrego la fila al tablero


for fila in tablero:
    for celda in fila:
        print(celda, end= " ")
    print()

jugador = "X"
jugada = 0

while jugada < 9:
    print(f"\nTurno de jugador {jugador}")

    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-2): "))

    if fila <0 or fila >2 or columna < 0 or columna > 2:
        print("Posicion fuera de rango. Intenta de nuevo")
        continue
    
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
        jugada += 1
    else:
        print("Casilla ocupada. Intenta de nuevo")
        continue

    for fila in tablero:
        for celda in fila:
            print(celda, end= " ")
        print()


    if jugador  == "X":
        jugador = "O"
    else:
        jugador = "X"
print("-----------------------------------------------------------------------------------")

#-----------------------------------------------------------
#------------------Ejercicio 10------------------------------

ventas= [
    [10, 5, 4, 6, 8 , 9 , 6],
    [5, 8, 7, 5, 3, 4, 11],
    [7, 6, 9, 10, 12, 3, 5],
    [3, 15, 6, 7, 9, 10, 6]
]

#cantidad de ventas por producto
producto_mas_ventas=[]
for i in range(4):
    suma = 0
    for j in range(7):
        suma += ventas[i][j]
    producto_mas_ventas.append(suma)
    print(f"La cantidad de ventas totales del producto {i+1}: {suma}") 

#producto con mas ventas semanales
mas_ventas= max(producto_mas_ventas)
print(f"\nEl producto con mas ventas es el: {producto_mas_ventas.index(mas_ventas)+1} con {mas_ventas}")

#cantidad de ventas por dia
ventas_totales = []
for i in range(7):
    suma=0
    for j in range(4):
        suma += ventas[j][i]
    ventas_totales.append(suma)

#Dia con mayores ventas [25, 34, 26, 28, 32, 26, 28]
mayores_ventas= max(ventas_totales)
dia = (ventas_totales.index(mayores_ventas) + 1)
dias_semana=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado","Domingo"]
print(f"\nEl dia {dias_semana[dia-1]} se registro la mayor cantidad de ventas de la semana, con un total de: {mayores_ventas}")
print("-----------------------------------------------------------------------------------")