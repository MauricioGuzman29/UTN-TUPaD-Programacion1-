import utils

op = "0"
productos=[]

menu = [
    "\n=== Gestor de Productos ===",
    "\n1. Mostrar productos.",
    "2. Agregar producto",
    "3. Cargar productos en lista de diccionarios",
    "4. Buscar producto",
    "5. Reescribir lista",
    "6. Salir\n."
]

while op != 6:
    for item in menu:
        print(item) 
    op = input("Ingrese una opcion (1 - 6): ").strip()

    if not op.isdigit():
        print("Opcion invalida. Vuelva a intentarlo")
        continue

    match op:
        case "1":
            utils.mostrar_productos()
        case "2":
            utils.agregar_productos()
        case "3":
            productos = utils.cargar_productos_en_lista()
        case "4":
            utils.buscar_productos(productos)
        case "5":
            utils.reescribir_archivo(productos)
        case "6":
            print("Hasta luego!")
        case _:
            print("Opcion fuera de rango, intente nuevamente")
        
        