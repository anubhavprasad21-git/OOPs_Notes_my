# All __something__ are called dunder methods in python because they automatically called when we create a object

class Humans:
    def __init__(self,name):
        self.name= name

    def __str__(self):
        return f"The name is {self.name}"

obj=Humans("Dhruve")
print(obj)