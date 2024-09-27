class Student:
    school = "KVS"
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    
    def deatails(self):
        print("Name=",self.__name)
        print("Age=",self.__age)
        print("School=",Student.school)

    class Marks(Student):
        def marks(self,hindi,math):
            self.hindi = hindi
            self.math = math
        def complete_details(self)