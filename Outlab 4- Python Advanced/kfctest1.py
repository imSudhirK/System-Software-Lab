from menu import Menu
from menuitem import MenuItem

menuItem1 = MenuItem('Chicken Popcorn', 98, 4.1)
menuItem2 = MenuItem('Zinger Burger', 258, 4.6)
menuItem3 = MenuItem('Chicken Pizza', 298, 4.0)
menuItem4 = MenuItem('Lime Krusher', 75, 4.3)
menuItem5 = MenuItem('Chicken Popcorn', 60, 4.1)
menuItem6 = MenuItem('Chicken Popcorn', 60, 4.1)

print(menuItem1)
print(menuItem1 == menuItem5)
print(menuItem5 == menuItem6)

menu = Menu([menuItem1, menuItem2, menuItem3, menuItem4, menuItem5, menuItem6])

print(len(menu))

print(menu)
list.sort(menu.menuitems, reverse=True)
print(menu)
