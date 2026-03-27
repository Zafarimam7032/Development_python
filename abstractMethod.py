from abc import ABC,abstractmethod
class Animal(ABC):
  @abstractmethod
  def getname(self):
    pass

class Vegetrial(Animal):
  def getname(self):
    print("this is getName method")
  def show(self):
    print("show method")  

child=Vegetrial()
child.show()
# child.getname()

parrent=Animal()
parrent.getname()

