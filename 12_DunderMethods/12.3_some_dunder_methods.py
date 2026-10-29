class Equals:
    def __init__(self,num):
        self.num = num

    def __eq__(self, value):
        return self.num == value.num

num1 = Equals(10)
num2 = Equals(10)

print(num1 == num2)