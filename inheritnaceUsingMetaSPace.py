class FinalMeta(type):
    def __init__(cls,name,bases,dict):
        for base in bases:
            if isinstance(base,FinalMeta):
                raise TypeError(f" {base.__name__}class cant not be overRide")

class Student(metaclass=FinalMeta):
    def display():
        print("this is student class")


class College(Student):
    pass