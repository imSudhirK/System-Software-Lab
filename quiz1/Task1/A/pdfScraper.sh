#! /bin/bash 

wget -O  name.pdf   $1

pdftotext name.pdf name.txt
rm name.pdf
cat name.txt
rm name.txt
