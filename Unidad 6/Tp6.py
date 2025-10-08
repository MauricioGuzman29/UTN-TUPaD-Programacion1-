#------------------ PRACTICO 6 ------------------------

#--------------------Funciones-------------------------


#Ejercicio 1-------------------------------------------
#Imprime Hola mundo! por pantalla.

#Funcion -----------------
def imprimir_hola_mundo():
    print("\nHola mundo")
#-------------------------

#Programa principal-------

imprimir_hola_mundo()

#------------------------------------------------------

#Ejercicio 2-------------------------------------------
#Saludo personalizado

#Funcion -----------------
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
#-------------------------

#Programa principal-------
print("\nSaludo personalizado")
print("------------------------------------------")
nombre = input("Ingrese un nombre: ").capitalize()

saludar_usuario(nombre)

#-----------------------------------------------------

#Ejercicio 3------------------------------------------
#Brinda un mensaje con informacion personal

#Funcion -----------------
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"\nSoy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
#-------------------------

#Programa principal-------
print("\nInformacion personal")
print("------------------------------------------")
nombre = input("Ingrese su nombre: ").capitalize()
apellido = input("Ingrese su apellido: ").capitalize()
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de Residencia: ").capitalize()

informacion_personal(nombre, apellido, edad, residencia)


#--------------------------------------------------------

#Ejercicio 4 --------------------------------------------
# calcula el area y oerimetro de un circulo mediante el radio.

import math

#Funciones -----------------
def calcular_area_circulo(radio):
    area = math.pi * (radio**2)
    print(f"El area del circulo segun el radio {radio} es: {area:.2f}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print(f"El perimetro del circulo segun el radio {radio} es: {perimetro:.2f}")
#-------------------------

#Programa principal-------
print("\nArea y perimetro de un circulo")
print("------------------------------------------")
radio = float(input("Ingresa el radio del circulo: "))

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)


#---------------------------------------------------------

#Ejercicios 5---------------------------------------------
#Convierte segundos a horas

#Funcion -----------------
def segundos_a_hora(segundos):
    horas= segundos / 3600
    return horas
#-------------------------

#Programa principal-------
print("\nConvertir segundos a horas")
print("------------------------------------------")
segundos= int(input("Ingrese una cantidad de segundos: "))

if segundos < 0:
    print("Ingrese un numaro mayor que 0")
else:
    horas = segundos_a_hora(segundos)
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

#-------------------------------------------------------

#Ejercicio 6--------------------------------------------
#Imprime la tabla de multiplicar de un numero ingresado

#Funcion -----------------
def tabla_multiplicar(num):
    for i in range(0,11):
        producto = num * i
        print(f"{num} x {i} = {producto}")
#-------------------------

#Programa principal-------
print("\nTabla de multiplicar")
print("------------------------------------------")
num = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))

tabla_multiplicar(num)

#---------------------------------------------------------

#Ejercicio 7----------------------------------------------
#con 2 numeros ingresados por el usuario calcula el resultado de sumarlos, restarlos, multiplicarlos y dividirlos.

#Funcion -----------------
def operaciones_basicas(a,b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = None
    return (suma, resta, multiplicacion, division)
#-------------------------

#Programa principal-------
print("\nOperaciones basicas")
print("------------------------------------------")
a= int(input("Ingrese un número: "))
b= int(input("Ingrese otro número: "))

suma, resta, multiplicacion, division = operaciones_basicas(a,b)

print(f"Suma: {a} + {b} = {suma}.")
print(f"Resta: {a} - {b} = {resta}.")
print(f"Multiplicacion: {a} * {b} = {multiplicacion}.")
if division is not None:
    print(f"Division: {a} / {b} = {division}.")
else:
    print("No se puede dividir por 0.")
#---------------------------------------------------------

#Ejercicio 8----------------------------------------------
#Calcula el indice de masa muscular 

#Funciones -----------------
def calcular_imc(peso, altura):
    imc = peso / (altura**2)
    return imc
#-------------------------

#Programa principal-------
print("\nCalcular IMC")
print("------------------------------------------")
peso = float(input("Ingresa tu peso en kg: "))
altura =float(input("Ingresa tu altura en metros: "))

imc = calcular_imc(peso,altura)
print(f"El indice de masa muscular es(IMC) es: {imc:.2f}")

#---------------------------------------------------------

#Ejercicio 9----------------------------------------------
#Convertir grados celcius a fahrenheit 

#Funcion -----------------
def celcius_a_fahrenheit(celcius):
    return  celcius * (9/5) + 32
#-------------------------

#Programa principal-------
print("\nConvertir grados celcius a fahrenheit")
print("------------------------------------------")
celcius = int(input("Ingresa grados celcius: "))

fahrenheit = celcius_a_fahrenheit(celcius)

print(f"\n{celcius} °C equivalen a {fahrenheit} °F.")

#---------------------------------------------------------

#Ejercicio 10---------------------------------------------
#Calcular el promedio de 3 notas ingresadas

#Funcion -----------------
def calcular_promedio(a,b,c):
    suma = a + b + c
    promedio = suma / 3
    return  promedio


#-------------------------

#Programa principal-------
print("\nPromedio de 3 notas")
print("------------------------------------------")
a = int(input("Ingresa una nota: "))
b = int(input("Ingresa una nota: "))
c = int(input("Ingresa una nota: "))

promedio = calcular_promedio(a,b,c)


print(f"El promedio de {a}, {b}, {c} es: {promedio:.2f}")

#---------------------------------------------------------


