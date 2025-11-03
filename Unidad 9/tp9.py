#--------------------- PRACTICO 9 ---------------------------

#----------------------Recursividad--------------------------


#Ejercicio 1-------------------------------------------------


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)

num = int(input("Ingrese un numero: "))
for i in range(num + 1):
    print(f"El factorial de {i} es {factorial(i)}")

#------------------------------------------------------------

#Ejercicio 2-------------------------------------------------

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else: 
        return fibonacci(num -1) + fibonacci(num - 2)
    
num = int(input("Ingrese un numero: "))
for i in range(num + 1):
    print(f"El termino de fibonacci de {i} es {fibonacci(i)}")

#------------------------------------------------------------

#Ejercicio 3-------------------------------------------------

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else: 
        return base * potencia(base, exponente - 1)

base= int(input("Ingresar la base: "))
exponente= int(input("Ingresar el exponente: "))
print(f"{base} elevado a la {exponente} es {potencia(base, exponente)}")

#------------------------------------------------------------

#Ejercicio 4-------------------------------------------------

def conversion(num):
    if num == 0:
        return ""
    else:
        return conversion(num // 2) + str(num % 2)
    
num= int(input("Ingresa un numero: "))
print(f"{num} en binario equivale a {conversion(num)}")

#------------------------------------------------------------

#Ejercicio 5-------------------------------------------------

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])



#------------------------------------------------------------

#Ejercicio 6-------------------------------------------------

def sum_dig(num):
    if num < 10:
        return num
    else:
        return (num % 10) + sum_dig(num // 10)

#------------------------------------------------------------

#Ejercicio 7-------------------------------------------------

def contar_bloques(num):
    if num == 1:
        return 1 
    else:
        return num + contar_bloques(num-1)

#------------------------------------------------------------

#Ejercicio 8-------------------------------------------------

def contar_digito(num, digito):
    if num < 10:
        if num == digito:
            return 1
        else:
            return 0
    
    ultimo_digito = num % 10
    num_sin_ultimo_digito = num // 10

    if ultimo_digito == digito:
        return 1 + contar_digito(num_sin_ultimo_digito, digito)
    else:
        return contar_digito(num_sin_ultimo_digito, digito)

#------------------------------------------------------------
