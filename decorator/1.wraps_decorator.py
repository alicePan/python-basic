# -*- coding: UTF-8 -*-

from functools import wraps


def log(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print 'before call function {0}'.format(func.__name__)
        return func(*args, **kwargs)
    return wrap

@log
def sum(*number):
  sum = 0
  for item in number:
    sum += item
  return sum

sum(12,33)