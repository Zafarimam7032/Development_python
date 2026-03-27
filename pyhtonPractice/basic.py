
class Student:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Address:",self.address) 
    def __str__(self):
        return f"name:{self.name},age:{self.age},address:{self.address}"
    
    def __repr__(self):
        return self.__str__()

obj1 = Student("Zafar", 25, "123 Main St")
obj2 = Student("Ali", 22, "Mumbai")

students = [obj1, obj2]
students.sort(reverse=False, key=lambda x: x.name)
print(students)