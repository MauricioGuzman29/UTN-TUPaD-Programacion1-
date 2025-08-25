#------------------ PRACTICO 3 --------------------------

#----------Estructuras condicionales---------------------




#Ejercicio 1---------------------------------------------

#Mayor de edad

edad = int(input("Ingrese su edad: "))

if edad > 0:
    if edad >= 18:
        print("Usted es mayor de edad.")
    else:
        print("Usted es menor de edad.")
else:
    print("Ingrese una edad valida.")

#--------------------------------------------------------

#Ejercicio 2---------------------------------------------

#Aprobado o desaprobado

nota =  int(input("Ingrese su nota: "))

if nota > 0:
    if nota >= 6:
        print("¡Aprobado!")
    else:
        print("¡Desapobado!")
else: 
    print("Ingrese una nota valida.")

#--------------------------------------------------------

#Ejercicio 3---------------------------------------------

#Numeros pares

num = int(input("Ingrese un numero par: "))

if num % 2 == 0 and num != 1: 
    print("Ha ingresado un numero par.")
else:
    print("Por favor, ingrese un numero par.")

#--------------------------------------------------------

#Ejercicio 4---------------------------------------------

#Categoria 

edad = int(input("Ingrese su edad: "))

if edad <= 0:
    print("Ingrese una edad valida.")
elif edad < 12: 
    print("Eres niño/a.")
elif edad >= 12 and edad <= 18:
    print("Eres adolecente.") 
elif edad >= 18 and edad < 30:
    print("Eres adulto joven.")
else:
    print("Eres adulto mayor.")

#--------------------------------------------------------

#Ejercicio 5---------------------------------------------

#Contraseña

contraseña = input("Ingrese su contraseña: ")
longitud = len(contraseña)

if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#--------------------------------------------------------

#Ejercicio 6---------------------------------------------

#Estadistica

from statistics import mode, median, mean
import random


numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("Moda: ", moda)
print("Mediana: ", mediana)
print("Media: ", media)

if (media > mediana) and (mediana > moda):
    print("Hay sesgo positivo.")
elif (media < mediana) and (mediana < moda):
    print("Hay esgo negativo.")
elif media == mediana and mediana == moda:
    print("Sin sesgo.")
else:
    print("La distribucion no presenta un sesgo definido.")

#--------------------------------------------------------

#Ejercicio 7---------------------------------------------

#Cadena con vocal

frase = input("Ingrese una frase o palabra: ")


if frase[-1] in "aeiouAEIOU":
    print(frase + "!")
else: 
    print(frase)

#--------------------------------------------------------

#Ejercicio 8---------------------------------------------

#Manejo de nombre

nombre = input("Ingrese su nombre: ")

print("Seleccione la opcion que desea:")
print("1: su nombre en mayúscula.")
print("2: su nombre en minúscula.")
print("3: primera letra en mayúscula.")

opcion = int(input())

if opcion == 1: 
    print(nombre.upper())
elif opcion == 2: 
    print(nombre.lower())
elif opcion == 3: 
    print(nombre.title())
else:
    print("Ingrese una opción valida: ")


#--------------------------------------------------------

#Ejercicio 9---------------------------------------------

#Magnitud de terremoto

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud > 0 and magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud <= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif magnitud >= 4 and magnitud < 5: 
    print("Moderado (sentido por personsas, pero generalmente no causa daño).")
elif magnitud <= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras debiles).")
elif magnitud >= 6 and magnitud < 7: 
    print("Muy fuerte (puede causar daños significativos).")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala).")
else:
    print("Ingrese una magnitu correcta")

#--------------------------------------------------------

#Ejercicio 10---------------------------------------------

#Estaciones del año en ambos hemisferios

hemisferio = input("¿En que hemisferio te encuentras, ingresa N para Norte y S para Sur (N/S): ")
mes = int(input("Ingresa el mes del año en formato numero (1-12): "))
dia =int(input("Ingresa el dia: "))

if mes < 1 or mes > 12 or dia < 1 or dia > 31:
    print("Fecha no valida.")
else: 

    if hemisferio.lower() == "n":
        if mes >= 1 and mes <= 2 :
            print("Estas en invierno")
        elif mes == 3: 
            if dia >= 1 and dia <= 20:
                print("Estas en invierno")
            else:
                print("Estas en primavera.")
        elif mes >= 4 and mes <= 5:
            print("Estas en primavera")
        elif mes == 6: 
            if dia >= 1 and dia <= 20:
                print("Estas en primavera.")
            else: 
                print("Estas en verano.")
        elif mes >= 7 and mes <= 8:
            print("Estas en verano")
        elif mes == 9: 
            if dia >= 1 and dia <= 20:
                print("Estas en verano.")
            else: 
                print("Estas en otoño.")
        elif mes >= 10 and mes <= 11:
            print("Estas en otoño")
        elif mes == 12: 
            if dia >= 1 and dia <= 20:
                print("Estas en otoño.")
            else: 
                print("Estas en invierno.")
            
    elif hemisferio.lower() == "s":
        if mes >= 1 and mes <= 2 :
            print("Estas en verano")
        elif mes == 3: 
            if dia >= 1 and dia <= 20:
                print("Estas en verano")
            else:
                print("Estas en otoño.")
        elif mes >= 4 and mes <= 5:
            print("Estas en otoño")
        elif mes == 6: 
            if dia >= 1 and dia <= 20:
                print("Estas en otoño.")
            else: 
                print("Estas en invierno.")
        elif mes >= 7 and mes <= 8:
            print("Estas en invierno")
        elif mes == 9: 
            if dia >= 1 and dia <= 20:
                print("Estas en invierno.")
            else: 
                print("Estas en primavera.")
        elif mes >= 10 and mes <= 11:
            print("Estas en primavera")
        elif mes == 12: 
            if dia >= 1 and dia <= 20:
                print("Estas en primavera.")
            else: 
                print("Estas en verano.")
    else:
        print("Opcion de hemisferio no valida. Ingrese nuevamente el hemisferio en el que se encuentra.")


#--------------------------------------------------------