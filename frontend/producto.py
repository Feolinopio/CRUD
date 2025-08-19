from utils.terminal import limpiar
import backend.producto as Producto
from tabulate import tabulate

headers = ["ID", "Nombre", "Precio", "Cantidad"]


def solicitarProducto():
    nombre = input("Ingrese un nombre: ")
    ID = input(f"Ingrese el ID de {nombre}: ")
    precio = input(f"Ingrese el precio de {nombre}: ")
    cantidad = input(f"Ingrese la cantidad disponible de {nombre}: ")

    return (ID, nombre, precio, cantidad)


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


def agregarProducto():
    nuevo_prodcuto = solicitarProducto()
    producto_creado = Producto.crearProducto(*nuevo_prodcuto)

    if producto_creado:
        print("El prodcuto se agregó con éxito")
    else:
        print("Se produjo un error al agregar el producto")


def actualizarProducto():
    nuevo_producto = solicitarProducto()
    producto_actualizado = Producto.actualizarProducto(*nuevo_producto)

    if producto_actualizado:
        print("El producto se actualizó con éxito")
    else:
        print("Error: verifique que el producto con ese nombre sí exista")


def eliminarProducto():
    nombre = input("Ingrese el nombre del producto: ")

    producto_eliminado = Producto.eliminarProducto(nombre)

    if producto_eliminado:
        print("El producto se eliminó con éxito")
    else:
        print("Error: verifique por favor que el producto con ese nombre sí exista")


def mostrarMenuDeProductos():
    separador = "------------------------"
    bienvenida = "Bienvenido a RR Tech 🤓"
    opciones = {
        "1": listarProductos,
        "2": consultarProducto,
        "3": agregarProducto,
        "4": eliminarProducto,
        "5": actualizarProducto,


    }
    solicitud = "Ingrese una opción: "
    salida = False

    while True:
        menu = f"{bienvenida if salida == False else separador}\n1. Listar productos\n2. Buscar productos\n3. Agregar producto\n4. Eliminar producto\n5. Actualizar producto\n6. Salir"
        print(menu)
        opcion = input(solicitud)
        salida = False

        if opcion == "6":

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
