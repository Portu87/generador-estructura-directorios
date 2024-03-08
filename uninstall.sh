#!/bin/bash

# Pregunta al usuario si está seguro de desinstalar
read -p "¿Estás seguro de que deseas desinstalar y eliminar todos los árboles creados por el script? (s/n): " confirmacion
if [ "$confirmacion" != "s" ]; then
    echo "Desinstalación cancelada."
    exit 0
fi

# Elimina la función del archivo .bashrc
sed -i '/# Función para generar el árbol de directorios/,/^}/d' "$HOME/.bashrc"

# Recargar el archivo .bashrc para aplicar los cambios
source "$HOME/.bashrc"

# Otorga permisos de escritura para el archivo en /usr/local/bin
sudo chmod +w /usr/local/bin/generar_arbol.py

# Elimina el archivo desde /usr/local/bin
sudo rm /usr/local/bin/generar_arbol.py

# Elimina todos los árboles creados en la carpeta arboles
rm -r arboles

echo "La desinstalación se ha completado correctamente."
