class Numbers:
    def __init__(self,num):
        self.num=num

    def __add__(self, other):
        return self.num + other.num

obj = Numbers(19)
obj2 = Numbers(34)

print(obj + obj2)