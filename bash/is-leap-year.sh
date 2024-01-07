#! /bin/bash
let v1=$1%1  v2=$1%100  v3=$1%400  v4=$1%4 
if [ $1 -lt 1 ] || [[ "$v1" != 0 ]];
then 
     echo "Invalid argument!"
elif [[ "$v2" = 0 ]];
then 
     if [[ "$v3" != 0 ]];
     then 
         echo "Not a leap year"
     else
         echo "Leap Year!"
     fi
elif [[ "$v4" = 0 ]] ;  then
           echo "Leap Year!"
else  
     echo "Not a leap year" 
fi

#year should be divisible with (4 and not 100) or (100 and 400)
