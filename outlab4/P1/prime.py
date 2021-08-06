#! /usr/bin/python

import sys 

def no_of_divisor (num):
          count= 0
          for i in range(1, num +1):
                if (num%i)==0:
                       count=count +1 
                else:
                       count=count
          return count 
def isPrime (num):
        if (num <= 1) :
                print ("No")
        elif (int(no_of_divisor (num))>=3):
                print ("No")
        elif (int(no_of_divisor (num))<3):
                print ("Yes")
        
def no__of_prime(lower_bound,upper_bound):
              counter=0
              for no in range(lower_bound,upper_bound + 1):
                      if no > 1:
                         for i in range(2,no):
                               if (no % i) == 0:
                                    break
                         else:
                              counter = counter +1
              return counter

arguments = sys.argv[1:]
if (len(arguments)==0):
     print ("Error : At least one of the following arguments are required: --check_prime, --range")
else:
     if (len(arguments)==2):
           if (sys.argv[1] == "--check_prime"):
                  if (int(sys.argv[2])>=1 and int(sys.argv[2])<=1000 ):
                             num = int (sys.argv[2])
                             isPrime(num)
                  else:
                             print ("Error : Please enter a value between 1 and 1000 only")
     elif (len(arguments)==3):
           if (sys.argv[1] == "--range"):
                   if (int(sys.argv[2])>=1 and int (sys.argv[2])<=1000 and int(sys.argv[3])>=1 and int(sys.argv[3])<=1000 and int(sys.argv[3])>=int(sys.argv[2])):
                             lover_bound = int (sys.argv[2])
                             upper_bound = int (sys.argv[3])
                             print ( no__of_prime(lover_bound , upper_bound))
                   else:
                             print ("Error : Please enter a value between 1 and 1000 only")
     elif (len(arguments)==5):
           if (sys.argv[1] == "--check_prime"):
                   if (int(sys.argv[2])>=1 and int(sys.argv[2])<=1000 ):
                             num = int (sys.argv[2])
                             isPrime(num)
                             if (sys.argv[3] == "--range"):
                                  if (int(sys.argv[4])>=1 and int(sys.argv[4])<=1000 and int(sys.argv[5])>=1 and int(sys.argv[5])<=1000 and int(sys.argv[5])>=int(sys.argv[4])):
                                        lover_bound = int (sys.argv[4])
                                        upper_bound = int (sys.argv[5])
                                        print ( no__of_prime(lover_bound , upper_bound))
                                  else:
                                        print ("Error : Please enter a value between 1 and 1000 only")
                   else:
                             print ("Error : Please enter a value between 1 and 1000 only")
           elif (sys.argv[1] == "--range"):
                   if (int(sys.argv[2])>=1 and int(sys.argv[2])<=1000 and int(sys.argv[3])>=1 and int(sys.argv[3])<=1000 and int(sys.argv[3])>=int(sys.argv[2])):
                             lover_bound = int (sys.argv[2])
                             upper_bound = int (sys.argv[3])
                             print (no__of_prime(lover_bound , upper_bound))
                             if (sys.argv[4] == "--check_prime"):
                                    if (int(sys.argv[5])>=1 and int(sys.argv[5])<=1000 ):
                                           num = int (sys.argv[5])
                                           isPrime(num)
                                    else:
                                           print ("Error : Please enter a value between 1 and 1000 only")
           
                   else:
                             print ("Error : Please enter a value between 1 and 1000 only")
           else:
                 print ("wrong input ")





