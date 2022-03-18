#!/bin/bash
for nombre in $(cat lista_nombres)
do
	if [ $nombre = "Mika" ]; then
		echo "Encontre a $nombre"
	else
		let a=$a+1
	fi
	curl -s https://api.genderize.io/?name=$nombre |
	jq '.gender' |
	{ read -r gen; echo "Gender of $nombre is: $gen"; } 
	curl -s https://api.nationalize.io/?name=$nombre |
	jq '.country[0].country_id' |
	{ read -r cn; echo "Country of $nombre is: $cn"; }
done
