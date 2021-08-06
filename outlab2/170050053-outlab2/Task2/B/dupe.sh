#! /bin/bash 

if [ -f $2 ];
then 
  echo "Not copied $1 "
else 
   cp $1 $2
   echo "Copied $1 "
fi
