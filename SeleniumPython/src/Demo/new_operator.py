'''
Created on 29-Jan-2019

@author: Ivavsys
'''
class test:
    inst=0
    MAX_OBJ=4
    def __init__(self,a=0):
        print('From Init')
        print('Default value = ',a)
    #Optional
    ''' Optional '''
    def __new__(cls, *args, **kwargs):
        ''' Python calls this method  before `init '''
        if cls.inst>=cls.MAX_OBJ:
            print("No More Objects can be created")
        else:
            cls.inst=cls.inst+1
            return object.__new__(cls, *args, **kwargs)
    
class static_demo:
    x=10
    @staticmethod
    def static_method():
        print("This is this static method")
    def non_static_method(self):
        print("This is the non static method")
    def test_lambda(self):
        g=lambda x:x**2
        return g(self.x)
    
obj=static_demo()
print(obj.test_lambda())
print(obj.non_static_method())
obj=test()
obj1=test()
obj2=test()
obj3=test()
obj4=test()