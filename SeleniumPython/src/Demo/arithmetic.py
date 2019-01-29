'''
Created on 29-Jan-2019

@author: Ivavsys
'''

class arithemtic_operations:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b    
    def sub(self):
        return abs(self.a-self.b)
    def mul(self):
        return self.a*self.b
    def div(self):
        if self.b!=0 or self.b!=0:
            if self.a>self.b:
                return self.a/self.b
            else:
                return self.b/self.a
        else:
            print("Not Possible divide by 0")

