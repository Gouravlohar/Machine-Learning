class Employee:
    def __init__(self,Sal,age):
        self.salary=Sal
        self.age=age
    def display(self):
        print(f"Employee Salary is {self.salary} and Age is {self.age}")
e1=Employee(2000,20)
e2=Employee(3500,40)
#Accessing Class
print(e1.salary)
print(e2.age)
#Accesing Methods
e1.display()
e2.display()