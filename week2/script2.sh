#!/bin/bash
req=`curl https://raw.githubusercontent.com/olea/lemarios/master/nombres-propios-es.txt | shuf`
countA=0
countL=0
countX=0

for nombre in $req
do
    if [[ $nombre == A* ]] && [ $countA -le 4 ] ;then
        echo "$countA - $nombre"
        let "countA++"
        curl -s https://api.genderize.io/?name=$nombre |
        jq '.gender' |
        { read -r gen; echo "Gender of $nombre is: $gen"; } 
        curl -s https://api.nationalize.io/?name=$nombre |
        jq '.country[0].country_id' |
        { read -r cn; echo "Country of $nombre is: $cn"; }
    fi
    if [[ $nombre == L* ]] && [ $countL -le 4 ] ;
    then
        echo "$countL - $nombre"
        let "countL++"
        curl -s https://api.genderize.io/?name=$nombre |
        jq '.gender' |
        { read -r gen; echo "Gender of $nombre is: $gen"; } 
        curl -s https://api.nationalize.io/?name=$nombre |
        jq '.country[0].country_id' |
        { read -r cn; echo "Country of $nombre is: $cn"; }
    fi
    if [[ $nombre != L* && $nombre != A* ]] && [ $countX -le 4 ] ;
    then
        echo "$countX - $nombre"
        let "countX++"
        curl -s https://api.genderize.io/?name=$nombre |
        jq '.gender' |
        { read -r gen; echo "Gender of $nombre is: $gen"; } 
        curl -s https://api.nationalize.io/?name=$nombre |
        jq '.country[0].country_id' |
        { read -r cn; echo "Country of $nombre is: $cn"; }
    fi    
done
