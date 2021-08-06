#! /usr/bin/env python
f = open('employees.txt', 'rU')
lines = f.readlines()
for line in lines:
      words = line.split()
      for word in words:
            string = word.split(',')
            for strings in string:
                  if strings.isalpha():
                      print(strings[3:] + strings[:3])       

f.close
