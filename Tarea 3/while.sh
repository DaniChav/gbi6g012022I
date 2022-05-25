#! /bin/bash

edad=$1
mensaje=$2
while [ $edad -lt 3]
do 
       echo  "la edad es $edad, $mensaje"
       edad=$(( edad+4))
done
