#! /usr/bin/python3

from menuitem import MenuItem
a = []
class Menu:
     def __init__(self,items):
         self.items = items 
     def __len__(self):
         return len(self.items)
     def __str__(self):
	 	#output=[]
        	for i in range(0,len(self)-1):
       	 		yield self[i]
		#return output
     #generator = __str__(self)
     #for item in generator:
	#	print (item)
	
	

if __name__ =="__main__" :
  menuItem1 = MenuItem('Chicken Popcorn', 98, 4.1)
  menuItem2 = MenuItem('Zinger Burger', 258, 4.6)
  menuItem3 = MenuItem('Chicken Pizza', 298, 4.0)
  menuItem4 = MenuItem('Lime Krusher', 75, 4.3)
  menuItem5 = MenuItem('Chicken Popcorn', 60, 4.1)
  menuItem6 = MenuItem('Chicken Popcorn', 60, 4.1)
  print (menuItem1)
  print(menuItem1 == menuItem5)
  menu = Menu([menuItem1, menuItem2, menuItem3, menuItem4, menuItem5, menuItem6])
  print(len(menu))
  print(menu)
