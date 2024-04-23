class Employee:
    def __init__(self,salary,age):
        self.salary=salary
        self.age=age
e1=Employee(24000,20)
e2=Employee(35000,25)

print(e1.__dict__)
print(e2.__dict__)