import os

def mostrar_productos():
    if not os.path.exists("productos.txt"):
        print(f"No existe productos.txt")
        return 
    
    with open ("productos.txt", "r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            print(f"Producto: {nombre}  Precio: ${precio} Cantidad: {cantidad}")

def agregar_productos():
    nombre = input("Ingrese el nombre del producto: ").capitalize()
    precio = input("Ingrese el precio del producto: ")
    cantidad = input("Ingrese la cantidad del producto: ")

    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre}, {precio}, {cantidad}\n")
    
    print(f"Producto agregado con exito.\n")

def mostrar_lista(productos):
    for producto in productos:
        print(f"Producto: {producto["nombre"]}| Precio: ${producto["precio"]} | Cantidad: {producto["cantidad"]}")

def cargar_productos_en_lista():
    productos = []
    if not os.path.exists("productos.txt"):
        print(f"No existe productos.txt")
        return []

    with open("productos.txt","r") as archivo:
        for linea in archivo:
            nombre, precio, cantidad = linea.strip().split(",")
            producto ={
                "nombre" : nombre,
                "precio" : precio,
                "cantidad": cantidad
            }

            productos.append(producto)
        print("Productos cargados correctamente.")
        mostrar_lista(productos)
        return productos
    
def buscar_productos(productos):
    if len(productos) == 0:
        print("No hay productos en la lista. Debe cargarlos primero.")
        return
    
    nombre_buscado = input("Ingrese el nombre del producto que desea buscar: ")
    encontrado = False

    for producto in productos:
        if producto["nombre"].lower() == nombre_buscado.lower():
            print(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}")
            encontrado = True
            break

    if not encontrado:
        print("Producto no encontrado.")

def reescribir_archivo(productos):
    if len(productos) == 0:
        print("No hay productos en la lista. Debe cargarlos primeros")
        return
    
    with open("productos.txt", "w") as archivo:
        for producto in productos:
            archivo.write(f"Producto: {producto['nombre']} | Precio: ${producto['precio']} | Cantidad: {producto['cantidad']}\n")
