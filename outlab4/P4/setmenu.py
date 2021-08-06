#! /usr/bin/python3

from menuitem import MenuItem
class SetMenu:    
     def __init__(self,items):
         self.items = items  
     def __len__(self):
         return len(self.items)
     def __str__(self):
	 ars = ""
         for i in range (0 ,len(self.items)):
	    ars=ars+str(self.items[i])+'\n'
	 return ars
