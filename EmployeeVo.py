class EmployeeVo:
  
    def __init__(self, id=None, name=None, address=None):
            if id is None  and name is None and address is None:
                 print("this is constructor")
            else:
             self.id = id
             self.name = name
             self.address = address

    def printData(self):
        print(f"Object data: {self.name} and {self.id}, {self.address}")

# Creating objects without `new`
# obj = EmployeeVo()
obj1 = EmployeeVo(1, "Zafar", "Pune")

# Calling the method correctly
obj1.printData()