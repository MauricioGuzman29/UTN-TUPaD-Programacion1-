#------------------ PRACTICO 3 --------------------------

#----------Estructuras Repetitivas---------------------




#Ejercicio 1---------------------------------------------

#Mostrar numero del 0 al 100

for i in range(0,101):
    print(i)

#--------------------------------------------------------

#Ejercicio 2---------------------------------------------

#Cantidad de digitos 

num = int(input("¡Por favor! ingrese un numero entero: "))
digitos = 0
numero = num

while num > 0:
    digitos = digitos + 1 
    num = num // 10 
    

print(f"El numero {numero} contiene {digitos} digitos.")

#--------------------------------------------------------

#Ejercicio 3---------------------------------------------

#Suma en rango 

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
suma = 0

for i in range(num1, num2):
    if i == num1: continue
    suma = suma + i
    
print(f"La suma de los numeros comprendidos entre {num1} y {num2} es igual a: {suma}. ")

#--------------------------------------------------------

#Ejercicio 4---------------------------------------------

#Suma de numeros

num = 1
suma = 0 
while num > 0:
    num = int(input("Ingrese un numero distinto de 0: "))
    suma = suma + num
print(f"La suma de los numeros ingresados es igual a: {suma}")

#--------------------------------------------------------

#Ejercicio 5---------------------------------------------

#Adivina el número

import random

num_aleatorio = random.randint(0,9)
print("¡Adivine el numero secreto!")
num_usuario = int(input("Ingrese un numero del 0 al 9: "))

while num_usuario != num_aleatorio:
    num_usuario = int(input("Ingrese otro numero: "))

print(f"¡Felicitaciones, adivinaste! El numero secreto era {num_aleatorio}")

#--------------------------------------------------------

#Ejercicio 6---------------------------------------------

#Numeros pares entre 0 y 100 decreciente

for i in range(100, -1, -2):
    print(i, end=" ")

#--------------------------------------------------------

#Ejercicio 7---------------------------------------------

#Suma en rango dado por usuario

num_limite = int(input("Ingrese el tope del rango: "))
suma = 0 

for i in range(0, num_limite):
    suma += i
print(f"La suma comprendida entre 0 y {num_limite} es igual a: {suma}.")

#--------------------------------------------------------

#Ejercicio 8---------------------------------------------

#Cantidad de numeros pares, impares, positivos y negativos 

contador = 0
positivos = 0
negativos = 0
pares = 0
impares = 0 

while contador < 100:
    num = int(input("Ingrese un numero: "))
    contador += 1 
    if num > 0:
        positivos += 1 
    elif num < 0:
        negativos += 1 
    if num != 0:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1 

print(f"De los números ingresados hay {positivos} número/s positivos, {negativos} número/s negativos, {pares} números pares y {impares} números impares.")

#--------------------------------------------------------

#Ejercicio 9---------------------------------------------

contador = 0
suma = 0


while contador < 100:
    num = int(input("Ingrese un numero: "))
    contador += 1 
    suma = suma + num 

media = suma / 100

print(f"La media de los numeros ingresados es {media}")


#--------------------------------------------------------

#Ejercicio 10--------------------------------------------

#Invierte numero ingresado por usuario 

num = int(input("Ingrese un numero: "))
invertido = 0
num_inicial = num

while num > 0:
    ultimo_digito = num % 10
    invertido = invertido * 10  + ultimo_digito
    num = num // 10
    
print(f"El número {num_inicial} invertido es {invertido}.")

#--------------------------------------------------------
