#! /bin/bash

echo "Escriba un script que imprima los números de las filas y las columnas para cada red" > netsize_all.txt
echo "______________________________________________" >> netsize_all.txt

for file in $(ls *.txt); do wc -l $file >> netsize_all.txt; head -n1 $file|grep -o " "|wc -l >> netsize_all.txt; done
