import csv

def process_class(fichero):
    """ Función que tendrá como ruta el fichero csv al abrir 
    los datos de una clase.
    Parámetros: con dicho fichero se obtendrá los datos de c/alumno
    que se van a almacenar en una lista de diccionarios.
    Salida: se indicará en la primera fila la clave de c/ valor y en las
    filas inferiores la información de c/alumno y las notas.
    """
    lista = []
    with open(fichero) as archivo:
        datos = csv.reader(archivo)

        for j in datos:
            lista.append(j)
        
        cabecera = lista.pop(0)
        print(cabecera)
        print()
        print(lista)

process_class("class.csv")