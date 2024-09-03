import os

lista_carpetas = []
numeros = {
    "1": "Primero de",
    "2": "Segundo de",
    "3": "Tercero de",
    "4": "Cuarto de",
    "5": "Quinto de",
    "6": "Sexto de",
    "7": "Septimo de",
    "8": "Octavo de",
    "9": "Noveno de",
    "10": "Decimo de",
    "11": "Undecimo de",
    "12": "Duodecimo de",
    "13": "Decimo Tercero de",
    "14": "Decimo Cuarto de",
    "15": "Decimo Quinto de",
}


def agregar_carpetas(nombre, cantidad):
    lista_carpetas.append({"nombre": nombre, "cantidad": int(cantidad)})


def crear_carpetas():
    for carpeta in lista_carpetas:
        for x in range(1, int(carpeta["cantidad"]) + 1):
            if not os.path.isdir(
                f"C:/Compartida Tribunal {numeros[str(x)]} {carpeta["nombre"]}"
            ):
                os.mkdir(
                    f"C:/Compartida Tribunal {numeros[str(x)]} {carpeta["nombre"]}"
                )
            else:
                continue
    print(f"Carpetas para los Tribunales de {carpeta["nombre"]} creadas con éxito")


def crear_carpeta(nombre, numero_tribunal):
    nombre_carpeta = f"Compartida Tribunal {numeros[str(numero_tribunal)]} {nombre}"
    os.mkdir(f"C:/{nombre_carpeta}")
    return nombre_carpeta


def grupo_carpetas():
    nombre_carpetas = input(
        "Ingrese el nombre de la dependencia de las cuales necesita crear las carpetas (Por ejemplo: Control Ordinario): "
    )

    cantidad_carpetas = input(
        f"Ingrese la cantidad de carpetas de {nombre_carpetas} que necesita crear: "
    )

    agregar_carpetas(nombre_carpetas, cantidad_carpetas)
    crear_carpetas()


def carpeta_individual():
    nombre_carpeta = input(
        "Ingrese el nombre de la dependencia que desea crear una carpeta de manera individual (Por ejemplo: Control Violencia contra la Mujer): "
    )
    numero_dependencia = input(
        f"Ingrese el numero de la dependencia {nombre_carpeta} que desea crear (Por ejemplo: '3' para Tercero de {nombre_carpeta}): "
    )
    if not os.path.isdir(
        f"C:/Compartida Tribunal {numeros[str(numero_dependencia)]} {nombre_carpeta}"
    ):
        nombre_carpeta = crear_carpeta(nombre_carpeta, numero_dependencia)
        print(f"La carpeta {nombre_carpeta} se creo correctamente")
    else:
        print("La carpeta existe")


def menu():
    while True:
        print("Seleccione una opción:")
        print("1. Agregar carpeta individual")
        print("2. Agregar grupo de carpetas")
        print("0. Salir")

        opcion = input("Ingrese el número de la opción: ")

        match opcion:
            case "1":
                carpeta_individual()
            case "2":
                grupo_carpetas()
            case "0":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida, por favor intente de nuevo.")


menu()
