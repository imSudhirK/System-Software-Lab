#! /usr/bin/python3

from menuitem import MenuItem
class Menu:    
     def __init__(self,items):
         self.items = items  
     def __len__(self):
         return len(self.items)
     def __str__(self):
	 ar= ""
         for i in range (0 ,len(self.items)):
	    ar=ar+str(self.items[i])+'\n'
	 return ar
 
           

