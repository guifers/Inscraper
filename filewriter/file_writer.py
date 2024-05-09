import os


def write_to_file(filename, data):
    with open(filename, "a") as f:
        f.write(data)


def verify_folder(ruta_carpeta,userToScrape):
    rutaCarpeta = 'D:\\Proyectos\\Instalker\\' + userToScrape
    print("ruts",rutaCarpeta)
    """
    Verifica si una carpeta existe en la ruta especificada.
    Si no existe, crea la carpeta.
    """
    if not os.path.exists(rutaCarpeta):
        os.makedirs(rutaCarpeta)
        return -1 #No existe
    else:
        return 0 #Existe

