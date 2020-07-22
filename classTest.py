class A:
    def hello(self, x):
        print("My name is", x)
    
class B(A):
    def __init__(self, name):
        self.name = name 

    def hey(self):
        self.hello(self.name)
    
instance = B("Ajay")
instance.hey()