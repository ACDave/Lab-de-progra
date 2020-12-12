#!/bin/bash
echo "¡Bienvenido! aquí obtendremos el valor hash del path que introduzcas."
echo "Por favor, introduce una ruta"
read path
Dir="$(pwd)/hashfile.txt"

if [[ -f "$path" ]]; then

	sha256sum $path > $Dir
	echo "Hash del archivo escrito en $Dir"

elif [[ -d "$path" ]]; then

	sha256sum $(find $path -type f | tr "\n" " ") > $Dir
	echo "Hash de los archivos escitos en $Dir"
else
	echo "la ruta no existe"
fi