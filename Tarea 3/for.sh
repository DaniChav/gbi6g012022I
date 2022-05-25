#! /bin/bash
echo "primera forma"
for i in 2 4 6 8 
do 
	x=$(( i**3 ))
	echo "valor $i, cubo $x"
done



echo "segunda forma"
for i in {5..100..20}
do
        x=$(( i**3 ))
        echo "valor $i, cubo $x"
done



echo "tercera forma"
for ((i=10; i<101; i+3 ))
do
        x=$(( i**3 ))
        echo "valor $i, cubo $x"
done
