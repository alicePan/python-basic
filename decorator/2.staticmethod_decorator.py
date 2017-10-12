# -*- coding: UTF-8 -*-

# reference: https://taizilongxu.gitbooks.io/stackoverflow-about-python/content/14/README.html
class A(object):
  def foo(self,x):
    """
    foo function is expected called by instance of class A
    """
    print "executing foo(%s,%s)"%(self,x)

  @classmethod
  def class_foo(cls,x):
    """
    clss is the hidded first params been passed to class_foo function
    and class_foo function is expeced called by A class itself but not instance of A class.
    """
    print "executing class_foo(%s,%s)"%(cls,x)

  @staticmethod
  def static_foo(x):
    """
    static methods are used as a logical conjunction betwwen classes.
    """
    print "executing static_foo(%s)"%x

a = A()

A.class_foo('1')

print '-----------'

print a.foo('1')

print '-----------'
print a.static_foo('1')


print '--------'
print A.static_foo('1')
