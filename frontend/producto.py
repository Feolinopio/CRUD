from utils.terminal import limpiar
import backend.producto as Producto
from tabulate import tabulate

headers = ["ID", "Nombre", "Precio", "Cantidad"]


def listarProductos():

    productos = Producto.listarProductos()
    print(tabulate(productos, headers=headers, tablefmt="rounded_grid"))


def consultarProducto():
    nombre = input(
        "Ingrese el nombre del producto (tenga en cuenta las mayúsculas): ")

    producto = Producto.consultarProducto(nombre)

    if producto == None:
        print(f"Producto con nombre {nombre} no existe, intenta nuevamente")
        return

    print(tabulate([producto[1:]], headers=headers, tablefmt="rounded_grid"))


def mostrarMenuDeProductos():
    separador = "------------------------"
    bienvenida = "Bienvenido a RR Tech 🤓"
    opciones = {
        "1": listarProductos,
        "2": consultarProducto,
    }
    solicitud = "Ingrese una opción: "
    salida = False

    while True:
        menu = f"{bienvenida if salida == False else separador}\n1. Listar productos\n2. Buscar productos\n3. Salir"
        print(menu)
        opcion = input(solicitud)
        salida = False

        if opcion == "3":

            limpiar()
            break

        if opcion in opciones:
            salida = True
            solicitud = "Ingrese una opción: "
            limpiar()
            opciones.get(opcion)()
        else:
            solicitud = "Opción invalida, ingrese una nueva opción: "
            limpiar()
