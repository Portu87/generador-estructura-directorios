# Generador de Árbol de Directorios

El script `generar_arbol.py` es una herramienta de línea de comandos diseñada para crear una representación visual en forma de árbol de la estructura de directorios de un proyecto. Esta representación se guarda en un archivo de texto, facilitando la visualización y el análisis de la estructura de carpetas y archivos de un proyecto.

### Tecnología y Versión

El script está escrito en Python 3, asegurándose de que sea compatible con la mayoría de las versiones recientes de Python. Se recomienda usar Python 3.6 o superior para garantizar la compatibilidad completa con las características del lenguaje utilizadas en el script.

### Instalación

Para instalar y utilizar el script `generar_arbol.py`, sigue estos pasos:

1. Descarga el archivo zip del generador de estructuras desde [AQUÍ](https://github.com/Portu87/generador-estructura-directorios/archive/refs/heads/main.zip).

2. Descomprime el archivo zip en el directorio de tu elección.

3. Abre una terminal y navega hasta el directorio donde se extrajo el archivo zip.

4. Asegúrate de que el archivo `install.sh` tenga permisos de ejecución. Si no los tiene, puedes concederlos con el siguiente comando:

    ```bash
    chmod +x install.sh
    ```

5. Ejecuta el archivo `install.sh` para instalar el script y configurar la función `generar_arbol`:

    ```bash
    ./install.sh
    ```

Este script copiará `generar_arbol.py` al directorio `/usr/local/bin`,

6. Abre el archivo ~/.bashrc, para agregar un nuevo comando:
   ```bash
   nano ~/.bahsrc
   ```

7. Al final del archivo pega la siguiente función, luego de pegar la funion guarda con `ctrl+o` y luego `ctrl+x`para salir:
    ```bash
    # Funcion para generar arbol de directorios
    function generar_arbol() {
        python3 /usr/local/bin/generar_arbol.py "$@"
    }
    ```

8. Para hacer que los cambios surtan efecto en la sesión actual de la terminal,ejecuta el comando 
    ```bash
    source ~/.bashrc
    ```
Si por alguna razón los cambios no surten efecto, puedes reiniciar la terminal.

### Ejemplo de Ejecución

Para generar un árbol de directorios y archivos del directorio `/home/sebas/Dev/www/gesapp` con las carpetas a excluir normalmente en una app de NextJs (`constants/log,server,node_modules,.next,.git,objects,types`), sigue estos pasos:

1. Ejecuta el script `generar_arbol`:

    ```bash
    generar_arbol
    ```

2. El script solicitará la ruta del directorio que deseas analizar. Ingresa la ruta y presiona Enter:

    ```bash
    Introduce la ruta del directorio a analizar: /tu/ruta/de/directorio
    ```

3. A continuación, se te pedirá que ingreses el nombre del archivo de salida (incluyendo la extensión `.txt`). Ingresa el nombre y presiona Enter:

    ```bash
    Introduce el nombre del archivo de salida (con extensión .txt): ejemplo.txt
    ```

4. Luego, si deseas excluir ciertos directorios del análisis, puedes proporcionar una lista separada por comas de los nombres de los directorios a excluir. De lo contrario, simplemente presiona Enter para continuar sin excluir ningún directorio:

    ```bash
    Opcional: Introduce los nombres de los directorios a excluir, separados por coma (sin espacios): directorio1,directorio2,directorio3
    ```

5. Finalmente, si hay extensiones de archivo que deseas excluir del análisis, puedes proporcionar una lista separada por comas de las extensiones a excluir. De lo contrario, presiona Enter para continuar sin excluir ninguna extensión:

    ```bash
    Opcional: Introduce las extensiones de archivo a excluir, separadas por coma (sin espacios): jpg,png
    ```

6. Una vez que hayas proporcionado todas las opciones necesarias, el script generará el árbol de directorios y guardará la salida en el archivo especificado. Verás un mensaje que indica que se ha generado el árbol de directorios correctamente:

    ```bash
    Se ha generado el árbol de directorios en el archivo: ejemplo.txt
    ```

7. Ahora puedes ver tu archivo creado en la carpeta principal `generador-de-estructuras` que has descomprimido anteriormente.

Este es un ejemplo de cómo sería la ejecución del script `generar_arbol.py` en la consola, paso a paso, con todas las interacciones y solicitudes de información.









