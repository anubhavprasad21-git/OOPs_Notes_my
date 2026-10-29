class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        print(f"Hello Hello {self.name}")
class Humans:
    def speak(self):
        print(f"Hello Hello" )

obj=Animal("Tiger")
obj2=Humans()
obj.speak()
obj2.speak()