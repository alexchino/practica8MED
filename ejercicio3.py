try:

    with open("archivo_inexistente.txt", "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
except FileNotFoundError:
    print("El archivo no fue encontrado. Por favor, asegúrate de que el archivo exista en la ubicación especificada.")
except PermissionError:
    print("No tienes permisos para abrir el archivo.")
except Exception as e:
    print("Ocurrió un error:", e)
