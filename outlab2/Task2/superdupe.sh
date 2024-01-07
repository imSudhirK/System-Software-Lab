#!/bin/bash


if [ -f $2 ];
then 
  echo "Not copied $1 "
else 
   mkdir  -p $2 
   cp $1 $2
   echo "Copied $1 "
fi
