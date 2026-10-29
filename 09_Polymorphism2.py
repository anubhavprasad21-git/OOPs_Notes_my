# Method Overriding
class BigFactory:
    def __init__(self,product):
        self.product=product
    def details(self):
        print(f"The product is {self.product}")

class factory(BigFactory):
    def details(self):
        print(f"The product({self.product}) is packed")

obj=factory("Rice")
obj.details()