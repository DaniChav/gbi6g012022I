#! /bin/bash

echo "Escriba un script que tome uno de estos archivos y determine el número de filas (polinizadores) y columnas (plantas). Tenga en cuenta que las columnas están separadas por espacios y que hay un espacio al final de cada línea. Tu script debería regresar." > netsize.txt
echo "_________________________________________________________" >> netsize.txt
echo "Daniela Chávez, Análisis de datos simple" >> netsize.txt; echo "Archivo: n1.txt" >> netsize.txt; echo "N° de filas:" >> netsize.txt; wc -l n1.txt >> netsize.txt; echo "N° de columnas:" >> netsize.txt; head -n1 n1.txt|grep -o " "|wc -l >> netsize.txt

