#! /bin/bash

i=1;
while [ $i -le 50 ]
do
    echo $1 
    echo $i
    i=$[ $i + 1 ];
done
