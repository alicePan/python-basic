# -*- coding: UTF-8 -*-

# 1. function defination
def sayHi():
  """
  Rirst line is the description of this function 
  """
  print 'Hi'

  """ 
    if there is return keyword, defination of this function ends.
    if there is no return key word in this function, default returned value is None
  """

  return 'Hi'

# 2. call function
word = sayHi()

print 'sayHi function returns {0}.'.format(word)


# 3. pass paramters to  a function
"""
  param types:
    1. unmutable params: strings, numbers, tuples
    2. mutable params: list, dict and so on
  paramter pass in python:
    To unmutable params, function changes the copy one of it
    To mutable params, function changes the params itself

 3.1 pass unmutable params example
"""
# dict varible points to the memory address of this object
cat = {'name': 'kido', 'age': 12}
num = 12
def set_none(value):
  return value
print set_none(num), num
print set_none(cat), cat

# 3.2 pass mutable params example
def change_name(cat):
  try:
    cat['name'] = 'maoqiu'
  except:
    None

change_name(cat)
print cat['name']

""""
  4. param  callable types:
    required parm: param callback order must match param order in declaration
    keyword param: callback order does not matte
    default param

"""

def chat(p1, sth, cat):
  print '{p1} says {sth} to {p2}'.format(p1=p1, sth=sth, p2=cat)

# 4.1 required param
try:
  # param pass is not correct
  chat()
except:
  print 'Miss required params with'

# param order is no correct
chat('Cat kido', 'miao', 'Betty')
print 'params is not correct'


# 4.2 keyword param
chat(cat='Kido', sth='miao', p1='Betty')

#4.3 default param
def log_info(name, age=18):
  print '{name} is age years old'.format(name=name, age=18)
# age is not passed to log_info function
log_info('Alice')

# 不定长参数
def sum(*num):
  sum = 0
  # num 是一个tuiple
  for num_item in num:
    sum += num_item
  return sum

print 'sum is:' + str(sum(12,23,44))

# 5.0 匿名函数
sayHi = lambda world='world': 'Hello, {world}'.format(world=world)
print sayHi('kido')

# global nonlocal 参数