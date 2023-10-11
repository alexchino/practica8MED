nombres = input("Ingrese una serie de nombres separados por coma: ")

nombres_lista = nombres.split(',')

try:
    with open("nombres.txt", "w") as archivo:

        for nombre in nombres_lista:
            archivo.write(nombre.strip() + "\n")
    print("Los nombres se han guardado en el archivo nombres.txt.")
except Exception as e:
    print("Ocurrió un error:", e)
