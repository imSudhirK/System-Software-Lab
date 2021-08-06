#! /usr/bin/python3

class MenuItem:
      def __init__ (self , Name , Cost, Rating):
          self.Name = Name ;
          self.Cost= Cost ;
          self.Rating= Rating;
      def __str__(self):
          return "Item: " + str(self.Name)  +", Cost: " + str(self.Cost) +", Rating: " + str(self.Rating) 
      def __eq__(self , other):
           return self.__dict__ == other.__dict__
  

