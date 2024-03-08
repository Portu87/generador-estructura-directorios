
import os

def generar_arbol_directorios(directorio_raiz, archivo_salida, directorios_excluir=None, extensiones_excluir=None):
    with open(archivo_salida, 'w') as archivo:
        _generar_arbol(directorio_raiz, archivo, directorios_excluir, extensiones_excluir)

def _generar_arbol(directorio_actual, archivo, directorios_excluir, extensiones_excluir, nivel=0):
    if nivel == 0:
        archivo.write(f"{os.path.basename(directorio_actual)}\n")
    else:
        archivo.write(f"{'    ' * (nivel-1)}|-- {os.path.basename(directorio_actual)}\n")

    for item in sorted(os.listdir(directorio_actual)):
        if item.startswith('.'):
            continue
        ruta_item = os.path.join(directorio_actual, item)
        if os.path.isdir(ruta_item):
            if directorios_excluir and any(directorio_excluir in ruta_item for directorio_excluir in directorios_excluir):
                continue
            _generar_arbol(ruta_item, archivo, directorios_excluir, extensiones_excluir, nivel + 1)
        else:
            if extensiones_excluir and any(item.endswith(ext) for ext in extensiones_excluir):
                continue
            archivo.write(f"{'    ' * nivel}|-- {item}\n")

def main():
    directorio_raiz = input("Introduce la ruta del directorio a analizar: ")
    archivo_salida = input("Introduce el nombre del archivo de salida (con extensión .txt): ")

    directorios_excluir_str = input("Opcional: Introduce los nombres de los directorios a excluir, separados por coma (sin espacios): ")
    directorios_excluir = [dir.strip() for dir in directorios_excluir_str.split(',')] if directorios_excluir_str else None

    extensiones_excluir_str = input("Opcional: Introduce las extensiones de archivo a excluir, separadas por coma (sin espacios): ")
    extensiones_excluir = [ext.strip() for ext in extensiones_excluir_str.split(',')] if extensiones_excluir_str else None

    if not os.path.isdir(directorio_raiz):
        print("La ruta especificada no es un directorio válido.")
        return

    generar_arbol_directorios(directorio_raiz, archivo_salida, directorios_excluir, extensiones_excluir)
    print(f"Se ha generado el árbol de directorios en el archivo: {archivo_salida}")

if __name__ == "__main__":
    main()
