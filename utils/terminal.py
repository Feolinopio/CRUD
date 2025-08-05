import os

def limpiar():
    if os.name == 'nt':  # Felipe tiene Windows
        os.system('cls')
    else:  # Camilo tiene MacOS
        os.system('clear')