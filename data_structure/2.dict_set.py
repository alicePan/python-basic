# -*- coding: UTF-8 -*-

"""
1.1 dict is a map with key-value feature;
key must be a string in python
Search  speed in map is  higher than list
"""

grades = {
  'Adam': 98,
  'Amy': 87
}



"""
1.2 Geting the value of not existing key will cause error
Solutions:
  Using keyword in to check if used key exist or not
  Using get method to get value of a key
disadvantage:
  Memory hightly cost 
"""
try:
  grades['Kido']
except:
  print 'Get a not existing key cause error'
  #Using get method to get value of a key
  print grades.get('Kido')
  # Using in keyword to do a check
  if 'Kido' in grades:
    print grades['Kido']
  else:
    print 'grades does not have a key called "Kido"'



"""
2. Set: Set forms up with unique keys
"""
a_set = ([1,2,3,4])

a_set.add(7)
a_set.add(7)

a_set.remove(3)

print(a_set)