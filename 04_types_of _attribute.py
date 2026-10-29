class student:
    a=20
    def __init__(self,name):
        self.name = name

    def hello(self): # object/Instance method -- capture the location of object
        print(f"The name is {self.name}")

    @classmethod     # class method -- capture the location of class
    def details(cls):
        print(f"The age of student is {cls.a}")

    @staticmethod
    def end():
        print("The End")

obj = student("Anubhav")
obj.hello()
obj.details()
obj.end()


    

    