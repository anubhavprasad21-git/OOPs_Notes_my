class student:
    def __init__(self,name,age,work):
        self.name=name
        self.age=age
        self.work=work
st_1=student("Anubhav",19,"AI Engineer")
st_2=student("Vaibhav",21,"Cost Manage Accountant")
print(st_1.work)
print(st_2.work)
print(f"{st_1.name} is {st_1.age} year old boy who work as an {st_1.work} in our company")