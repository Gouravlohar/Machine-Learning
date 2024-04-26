class Boy:
    def __init__(self,name,age):
        self.name=name
        self.age=age
e1=Boy("Tom",8)
e2=Boy("Jerry",9)
print(getattr(e1,"age"))
setattr(e1,"name", "Rick")
print(e1.__dict__)
print(hasattr(e2,"Father"))
delattr(e1,"name")