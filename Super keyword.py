class Parent:
    def __init__(self,txt):
        self.message = txt
    def printmessage(self):
        print(self.message)
class Child(Parent):
    def __init__(self,txt):
        super().__init__(txt)
a=input("Enter the message:")
x=Child(a)
x.printmessage()