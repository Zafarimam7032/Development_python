

class Parent:
  def show(self):
    print("this is show method parent Method")


class Child(Parent):
  def show(self):
    print("this is child method")

obj=Parent()
obj.show()
obj1=Child()
obj1.show()
