class Human:
    __a= 23
    @classmethod
    def access(cls):
        print(f"the private attribute is {cls.__a}")

obj=Human()
obj.access()