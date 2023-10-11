try:
    with open("archivo.txt", "r") as archivo
        for linea in archivo:
            print(linea, end="")
except FileNotFoundError:
    print("El archivo no fue encontrado.")
except PermissionError:
    print("No tienes permisos para abrir el archivo.")
except Exception as e:
    print("Ocurrió un error:", e)
