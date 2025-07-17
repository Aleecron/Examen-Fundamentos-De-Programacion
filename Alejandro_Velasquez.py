productos = {
    '8475HD': ['Hp', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['Hp', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['Lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {
    '8475HD': [387990, 10], '2175HD': [327990, 4], 'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21], '123FHD': [290890, 32], '342FHD': [444990, 7],
    'GF75HD': [749990, 2], 'UWU131HD': [349990, 1], 'FS1230HD': [249990, 0]
}

# funcion1
def stock_marca():
    marca = input("Ingrese marca a consultar:  ")
    encontrados = False
    for modelo, datos in productos.items():
        if datos[0].lower() == marca.lower():
            if modelo in stock:
                cantidad = stock[modelo]
                print(f"El stock es:{cantidad}")
                encontrados = True
    if not encontrados:
        print("No se encuentra esa marca")

# funcion2
def búsqueda_precio():
    try: 
        p_min = int(input("Ingrese precio mínimo: "))
        p_max = int(input("Ingrese precio máximo: "))
        print(f"Productos entre ${p_min} y ${p_max}:")
        encontrados = False
        for modelo, (precio, cantidad) in stock.items():
            if p_min <= precio <= p_max and modelo in productos:
                print(f"Los notebooks entre los precios consultas son:: {modelo}, Precio: ${precio}, Cantidad: {cantidad}")
                encontrados = True
        if not encontrados:
            print("No hay notebooks en ese rango de precio")
    except ValueError:
        print("Debe ingresar valores enteros!!.")

#funcion3
def actualizar_precio():
    modelo = input("Ingrese el modelo que desea actualizar: ")
    if modelo in stock:
        try:
            nuevo_precio = int(input("Ingrese nuevo precio: "))
            stock[modelo][0] = nuevo_precio
            print(f"Precio actualizado para {modelo}: ${nuevo_precio}")
        except ValueError:
            print("Debe ingresar un precio válido (número entero).\n")
    else:
        print("El modelo no existe en el stock.")

#menu
def menu():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Stock marca.")
        print("2. Búsqueda por precio.")
        print("3. Actualizar precio.")
        print("4. Salir.")
        opcion = input("Ingrese opción: ")
        if opcion == "1":
            stock_marca()
        elif opcion == "2":
            búsqueda_precio()
        elif opcion == "3":
            actualizar_precio()
        elif opcion == "4":
            print("Programa Finalizado")
            break
        else:
            print("Debe seleccionar una opción válida!!")

menu()
