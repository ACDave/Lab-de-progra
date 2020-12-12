echo "introduce un path para obtener los hash: "
read path
dir="$(pwd)/hashfile.txt"

sh_value(){
	if [[ -f "$1" ]]; then

		sha256sum $1 > $2
		echo "Hash enviado a $2"
	elif [[ -d "$1" ]]; then

		sha256sum $(find $1 -type f | tr "\n" " ") > $2
		echo "Hash enviado a $2"
	else
		echo "La ruta no existe"
	fi
}
sh_value "$path" "$dir"