class Employee:
    def __init__(self):
        self.salary=25000
        self.age=20
e1=Employee()
e2=Employee()

print(e1.__dict__)
print(e2.__dict__)