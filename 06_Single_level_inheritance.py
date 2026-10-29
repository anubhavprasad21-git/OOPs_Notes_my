class BagFactory:
    def __init__(self,material,zips,pockets):
        self.material=material
        self.zips=zips
        self.pockets=pockets
    def detail(self):
        print("The list of items")
        print(self.material)
        print(self.zips)
        print(self.pockets)
class zora(BagFactory):
    def __init__(self, material, zips, pockets,color):
        super().__init__(material, zips, pockets)
        self.color=color
    def details(self):
        print(self.color)
        return super().details()
obj1=BagFactory("leather",3,4)
obj2=zora("polyster",5,3,"pink")
obj2.details()


# if we add one more class then its called multi-level inheritance




   