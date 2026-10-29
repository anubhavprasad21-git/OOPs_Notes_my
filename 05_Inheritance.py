class parent:
    a=2
    def __init__(self,name):
        self.name = name
    def details(self):
        print(f"Hello Hello {self.name}")
class child(parent):
    pass

obj1 = parent("Anubhav")

obj2 = child("Harsh")
obj2.details()
print(obj2.a)

# Your child class object(obj2) has all the powers to access the attribute and methods of parent class(obj1)



