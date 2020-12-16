#Obtencion de la ip
dir="$(pwd)/ip_nmap_results.txt"

ip_loc="$(hostname -I)"
ip_pub="$(wget http://ipecho.net/plain -O - -q; echo)"
echo ip_local: $ip_loc >> $dir
echo ip_publica: $ip_pub >> $dir

#escaneo con nmap
echo Escaneo del segmento: >> $dir
nmap scanme.nmap.org >> $dir
echo escaneo de la IP publica: >> $dir
nmap $ip_pub >> $dir

cat $dir | base64 > $dir