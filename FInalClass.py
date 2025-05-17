from typing import final

@final
class Employee:
    def display(self):
        print("This is a final class")

class Child(Employee):  # ❌ ERROR: Cannot inherit from a final class
    def display(self):
        return super().display()
    
    

