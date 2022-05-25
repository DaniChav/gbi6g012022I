#!/bin/bash
echo "Chávez, Daniela"

echo "Número de filas"
for f in ../Saavedra2013/*.txt;
do
	cat $f 	|wc -l;
done

echo "Número de columnas"
for f in ../Saavedra2013/*.txt;
do
	head -n 1 $f | tr -d " " | tr -d "\n" | wc  -c;
done
