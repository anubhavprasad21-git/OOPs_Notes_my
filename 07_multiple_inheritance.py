class parent_1:
    def __init__(self,name):
        self.name=name

class parent_2:
    def __init__(self,id):
        self.id=id

class child(parent_1,parent_2):
    def __init__(self, name,id):
        parent_1.__init__(self,name)
        parent_2.__init__(self,id)

obj_child = child("anubhav",23) 
print(obj_child.name)
print(obj_child.id)

