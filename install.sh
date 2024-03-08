#!/bin/bash

# Ruta al directorio donde se encuentra el script y el README
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"


# Copiar el script a un directorio adecuado
TARGET_DIR="/usr/local/bin"
cp "$SCRIPT_DIR/generar_arbol.py" "$TARGET_DIR"
chmod +x "$TARGET_DIR/generar_arbol.py"


# Imprimir mensaje de instalación exitosa
echo "El script 'generar_arbol.py' ha sido instalado correctamente."
echo "Para usarlo, simplemente ejecuta 'generar_arbol' en tu terminal."
