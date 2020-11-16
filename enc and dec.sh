#!/usr/bin/env bash

val=1

while [ $val -gt 0 ]
do
	echo "enter an archive or press 2 for leave"
	read arch 
	if [ $arch == 2 ]
		then
		echo "Understandable have a great day" 
		exit 0
	fi  

	archive=$(md5sum $arch | cut -f 1 -d " ") 
	if [ $archive == "4260808329804b5f553cf3e3d5a446c6" ] #fcfm_logo
		then
		cat $arch | base64  | base64 > fcfm_base_64.txt
		echo "Master, the encode is complete"      

	elif [ $archive == "5db9862819edb16f9ac0f3b1c406e79d" ] #mystery_img1.txt
		then
		cat $arch | base64 --decode > mystery_img1_decoded.jpeg
		echo "Master, the decode is complete"

	elif [ $archive == "b091a841da98ca516635f4dfea1dbaf5" ] #mystery_img2.txt
		then
		cat $arch | base64 --decode > mystery_img2_decoded.jpeg
		echo "Master, the decode is complete"

	elif [ $archive == "40744679dff4bf36705c00f9cb815579" ] #msg.txt
		then
		cat $arch | base64 | base64 >  msg_base_64.txt 
		echo "Master, the encode is complete"
	else:
		echo "It doesn't exist"
	fi
done
