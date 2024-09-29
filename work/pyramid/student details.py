class Student:
    def ab(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id
    
    def details(self):
        print(f"Name : {self.name} \n age : {self.age} \n id : {self.id}")

name=input("enter the name:")
age=int(input("enter the age:"))
id=int(input("enter the id:")) 
a=Student()
a.ab(name,age,id)
a.details()





