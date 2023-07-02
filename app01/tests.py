from django.test import TestCase

# Create your tests here.
class A():
    def __init__(self,name):
        self.name=name

class B():
    def __init__(self,name,age):
        A.__init__(self,name)
        self.age=age
    def hh(self):
        print(self.name)
kk=B('hh',12)
print(B.__dict__)
kk.hh()