# -*- coding: UTF-8 -*-

"""
1. List: list is a built in data type
"""
cats = ['Kido', 'Maoqiu']

#1.2. We can use keyword len to get the size of a list
print 'Size of list is cats {len}'.format(len=len(cats))


#1.3. Start index of a list is 0
print cats[0]

#1.4. Use append method of a list to ppend a new element to it
cats.append('xiaoxiao')

#1.5 Use pop method of a list to delete an element of it,
# list.pop(index)
cats.pop(2)

#1.6 Use insert method of a list to insert an element to the indexed postion of it.
cats.pop(1)
cats.insert(1, 'Maoqiu')

#1.7 An element of list can be another list
pets = ['dog koakoa', cats]

"""
tuiple: tuiple is an unmutable list. There is no insert, pop, append mehtods on it.
"""
unmutable_tuiple = ('White', 'Walker')
