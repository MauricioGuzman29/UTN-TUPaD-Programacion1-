#------------------ PRACTICO 1 --------------------------


#Ejercicio 1---------------------------------------------

#Imprime mensaje Hola mundo!

print("Hola mundo!")

#--------------------------------------------------------

#Ejercicio 2---------------------------------------------

#Imprime un saludo con nombre 

nombre = input("Ingrese su nombre: ")
print(f"¡Hola {nombre}!.")

#--------------------------------------------------------

#Ejercicio 3---------------------------------------------

#Imprime un mensaje con datos personales

nombre= input("Ingrese su nomnbre: ")
apellido= input("Ingrese su apellido: ")
edad= int(input("Ingrese su edad: "))
residencia= input("Ingrese su lugara de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#--------------------------------------------------------

#Ejercicio 4---------------------------------------------

#Calcula area y perimetro de un circulo

import math
#importe el valor de PI

radio = float(input("Ingrese el radio: "))

#realice el redondeo a 2 decimales de los resultados de area y perimetro 
area = round(math.pi * (radio ** 2), 2)
perimetro= round(2 * math.pi * radio, 2)

print(f"El area del circulo es: {area}, minetras que su perimetro es: {perimetro}")

#--------------------------------------------------------

#Ejercicio 5---------------------------------------------

#Muestra la equivalencia entre segundos y hora

segundos = int(input("Ingrese la cantidad de segundos: "))
hora= round(segundos / 60)
print(f"{segundos} segundos equivalen a {hora} hora/s.")

#--------------------------------------------------------

#Ejercicio 6---------------------------------------------

#Muestra tabla de multiplicar de un numero 

numero = int(input("Ingrese un numero: "))

print(f"{numero} x 1 = ", numero * 1)
print(f"{numero} x 2 = ", numero * 2)
print(f"{numero} x 3 = ", numero * 3)
print(f"{numero} x 4 = ", numero * 4)
print(f"{numero} x 5 = ", numero * 5)
print(f"{numero} x 6 = ", numero * 6)
print(f"{numero} x 7 = ", numero * 7)
print(f"{numero} x 8 = ", numero * 8)
print(f"{numero} x 9 = ", numero * 9)

#--------------------------------------------------------

#Ejercicio 7---------------------------------------------

#Realiza operaciones matematicas entre 2 numeros

num1 = int(input("Ingrese un numero distinto de 0: "))
num2 = int(input("Ingrese un numero distinto de 0: "))

suma= num1 + num2
resta= num1 - num2
multiplicacion= num1 * num2
division= num1 / num2 

print(f"{num1} + {num2} = ", suma)
print(f"{num1} - {num2} = ", resta)
print(f"{num1} x {num2} = ", multiplicacion)
print(f"{num1} / {num2} = ", division)

#--------------------------------------------------------

#Ejercicio 8---------------------------------------------

#Calcula el IMC

peso= float(input("Ingrese su peso corporal: "))
alt=float(input("Ingrese su altura en metros: "))

altura = alt / 100 
imc = round(peso / (altura ** 2), 2)

print(imc, altura)
print(f"Su indice de masa corporal es: {imc}")

#--------------------------------------------------------

#Ejercicio 9---------------------------------------------

#Convierte grados celciuss en grados fahrenheit

temperatura = float(input("Ingrese una temperatura en grados celcius: "))

conversion = temperatura * (9/5) + 32

print(f"{temperatura} grados Celcius equivalen a {conversion} grados Fahrenheit.")

#--------------------------------------------------------

#Ejercicio 10---------------------------------------------

#Calcula el promedio de 3 notas

nota1 = int(input("Ingrese una nota: "))
nota2 = int(input("Ingrese una nota: "))
nota3 = int(input("Ingrese una nota: "))

promedio = round((nota1 + nota2 + nota3) / 3, 2)

print(f"El promedio general de las notas ingresadas es: {promedio}")

#--------------------------------------------------------