#!/bin/bash

for FILE in $(ls -1 *.{jpg,JPG,png,PNG}) ; 
do
    echo "Converting ${FILE}..."
    convert -resize 800 $FILE $FILE
done
