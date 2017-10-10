# -*- coding: UTF-8 -*-
import json

# json.loads converts json to original data
# json.dumps encode data into json

person = {
  'name': 'Betty',
  'age': 28
}
# dict --> object
person_str = json.dumps(person)
print person_str

# list --> array
# tuiple --> array
fruits = ['Apple', 'Orange', 'Bnana']
cats = ('kido', 'maoqiu', 'small')
print json.dumps(fruits), json.dumps(cats)

# True --> true; False --> false; None -> null
print json.dumps(True), json.dumps(False), json.dumps(None)



jsonData = '{"a":1,"b":2,"c":3,"d":4,"e":5}'
print json.loads(jsonData)