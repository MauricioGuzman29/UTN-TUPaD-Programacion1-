#------------------ PRACTICO 7 ------------------------------

#--------------------Datos Complejos-------------------------


#Ejercicio 1, 2 y 3------------------------------------------

#Ejercicio 1 
precios_frutas = {"Banana" : 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)

#Ejercio 2, se modifican los precios de las frutas

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print(precios_frutas)

#Ejercio 3, se crea lista que almacena solo los nombres de las frutas

frutas=[]

for clave, valor in precios_frutas.items():
    frutas.append(clave)
print(frutas)


#--------------------------------------------------------------

#Ejercicio 4---------------------------------------------------

#Se crean 2 funciones para validacion para cadena de texto en nombre y digito en numero telefonico. 
def es_texto(nombre):
    while not nombre.isalpha():
        print("Error, recuerda ingresar un nombre.")
        nombre = input("Ingresa el nombre del contacto: ").capitalize().strip()
    return nombre

def es_numero(numero):
    while not numero.isdigit():
        print("Error, recuerda ingresar un numero telefonico.")
        numero= input("Ingresa el número telefonico del contacto: ")
    return numero

#Se crea funcion consultar contacto.
def consultar_contacto(dicc):
    consulta = input("Ingrese el nombre del contacto que desea consultar: ").capitalize().strip()
    if consulta in dicc:
        print(f"Número de {consulta}: {dicc[consulta]}")
    else:
        print("Contacto no encontrado.")

#Programa principal

contactos = dict()
print("\n===== Agenda Telefonica ====\n")
for i in range(5):
    nombre_contacto = es_texto(input("Ingresa el nombre del contacto: ").capitalize().strip())
    numero_contacto = es_numero(input("Ingresa el número telefonico del contacto: "))
    contactos[nombre_contacto] = (numero_contacto)
print(f"Contactos: {contactos}")

#Consultar contacto 
consultar_contacto(contactos)

#--------------------------------------------------------------

#Ejercicio 5---------------------------------------------------

#funcion para crear lista con las palabras
def crear_lista_palabras(frase):
    palabras = frase.split()
    return palabras
#crea un set con las palabras sin repetir de la lista
def palabras_sin_repetir(lista):
    sin_repetir = set(lista)
    print("palabras unicas: ",sin_repetir)
#cuenta el total de cada palabra que se encuentra en la lista y lo muestra en un diccionario
def contar_palabras(lista, dicc):
    for elemento in lista:
        dicc[elemento] = dicc.get(elemento, 0) + 1
    print(f"Recuento: {dicc}")

#Programa principal

frase = input("Ingrese una frase: ").lower()

palabras_sin_repetir(crear_lista_palabras(frase))

#creo diccionario recuento
recuento = dict()
contar_palabras(crear_lista_palabras(frase), recuento)

#--------------------------------------------------------------

#Ejercicio 6---------------------------------------------------

#Crea un diccionario vacio
alumnos = {}

#carga el nombre del alumno y sus tres notas en una tupla
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ").capitalize().strip()
    nota1 = float(input("Ingresa una nota: "))
    nota2 = float(input("Ingresa una nota: "))
    nota3 = float(input("Ingresa una nota: "))
    alumnos[nombre] = (nota1, nota2, nota3)
print()
print(f"Notas de alumnos: {alumnos}")

#accede a los nombres y notas de los alumnos y calcula su promedio. Acto seguido imprime por pantalla los resultados
for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"\nPromedio de {nombre}, promedio: {promedio:.2f}")
    
    

#--------------------------------------------------------------

#Ejercicio 7---------------------------------------------------

parcial_1 = {1,2,6,7,8}
parcial_2 = {1,2,3,4,5}
#cada numero equivale al legajo de un alumno


ambos = parcial_1 & parcial_2
solo_uno = parcial_1 ^ parcial_2
al_menos_uno = parcial_1 | parcial_2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)


#--------------------------------------------------------------

#Ejercicio 8---------------------------------------------------

#Diccionario de productos
productos ={
    "Zapatillas": 6,
    "Corbatas": 10,
    "Medias": 25,
    "Pantalones": 9,
    "Remeras": 12
}

#Funciones para consultar y agregar stock
def consultar_producto():
    consulta = input("Ingresa el producto que desea consultar: ").capitalize()
    if consulta in productos:
        print(f"\nStock disponible de {consulta}: {productos[consulta]}")
        
def agregar_stock():
    consulta = input("Ingresa el producto al que desea agregar stock: ").capitalize()
    if consulta in productos:
        cantidad = int(input(f"Ingrese la cantidad de {consulta} que desea agregar: "))
        productos[consulta] += cantidad
        print(f"\nStock disponible de {consulta}: {productos[consulta]}")
    else:
        print("Producto no encontrado. Se agregara al stock")
        productos[consulta] = int(input("Ingrese el stock del nuevo producto: "))
        print("Producto cargado exitosamente.\n")
        print(f"\nStock disponible de {consulta}: {productos[consulta]}")


#Opciones del menu guardados en una lista
menu = [
        "\n--- Menu de opciones ---",
        "........................\n",
        "1. Consultar stock de producto",
        "2. Agregar unidades al stock (si no existe producto se agrega al stock)",
        "3. Mostrar stock completo",
        "4. Salir"
    ]

# Programa principal 

op = "0"
while op != "4":
    for item in menu:
        print(item) 
    op= input("\nIngresar opcion(1-4): ")

    if not op.isdigit():
        print("Opcion invalida. Vuelva a intentarlo")
        continue

    match op:
        case "1":
            consultar_producto()
        case "2":
            agregar_stock()
        case "3":
            print(productos)
        case "4":
            print("Mugas gracias, hasta luego!")
        case _:
            print("Opcion invalida, intentelo de nuevo.")

#--------------------------------------------------------------

#Ejercicio 9---------------------------------------------------

#Agenda semanal
agenda = {
    ("Lunes", "10:00"): "Reunión",
    ("Martes", "15:00"): "Gimnasio",
    ("Miercoles", "18:00"): "Fútbol",
    ("Jueves", "21:00"): "Cena con amigos",
    ("Viernes", "14:00"): "Almuerzo de trabajo",
    ("Sabado", "16:00"): "Futbol",
    ("Domingo", "12:00"): "Almuerzo familiar" 
}
#Funciones para validar hora y para validar dia de la semana
def validar_dia(dia):
    dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    while dia not in dias:
        print("El día ingresado no es válido. Ingrese de nuevo.")
        dia = input("Ingresa el día que querés consultar (Lunes-Domingo): ").capitalize()
    return dia

#Esta funcion valida el formato hh:mm
def validar_hora(hora_str):
    partes = hora_str.split(":")
    if len(partes) != 2:
        return False
    hh_str, mm_str = partes
    if not (hh_str.isdigit() and mm_str.isdigit()):
        return False
    if not (1 <= len(hh_str) <= 2 and len(mm_str) == 2):
        return False
    hh, mm = int(hh_str), int(mm_str)
    return 0 <= hh <= 23 and 0 <= mm <= 59

#consultar el dia y la hora, muestra envento si esta registrado.
def consulta_agenda(dia, hora):
    if (dia, hora) in agenda:
        print(f"\nEl día {dia} a las {hora} tienes: {agenda[(dia, hora)]}.")
    else:
        print(f"\nNo existe evento agendado el {dia} a las {hora}.")

# Programa principal
print("============== AGENDA =====================")
print("...........................................\n")


dia_consulta = validar_dia(input("Ingresa el día que querés consultar (Lunes-Domingo): ").capitalize())

hora_consulta = input("Ingresa la hora que deseás consultar (HH:MM): ")
while not validar_hora(hora_consulta):
    print("La hora ingresada no es válida. Ingrese de nuevo.")
    hora_consulta = input("Ingresa la hora que deseás consultar (HH:MM): ")

consulta_agenda(dia_consulta, hora_consulta)

#--------------------------------------------------------------

#Ejercicio 10---------------------------------------------------

original = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Francia": "París",
    "Japón": "Tokio",
    "Canadá": "Ottawa"
}

#Funcion que toma un diccionario original e invertido vacio. Invierte clave valor y lo almacena en diccionario invertido. Muestra original e invertido
def invertir(dicc_ori, dicc_inv):
    for clave, valor in dicc_ori.items():
        dicc_inv[valor] = clave
    print(f"Original: {dicc_ori}")
    print(f"Invertido: {dicc_inv}")

#Porgrama principal
invertido = {}
invertir(original, invertido)

#--------------------------------------------------------------