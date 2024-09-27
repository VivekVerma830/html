# class Student:
#     def display(self):
#         global a
#         a=10
#         print("value of a",a)

#     def show(self):
#         print("value of a =",a)

#     def new():
#         print("value of a =",a)
    
# obj=Student()
# obj.display()
# obj.show()
# Student.new()

#method - instance method

# class student:
#     def display(self,name):
#         self.name= name
#         print(Name =self.name)

#     def show(self,age):
#         self.age=age

#         print(Age=self.age)

# obj=student()
# obj.display()
# obj.show()

#---------------------------------

class Book:
    def book_detail(self,name,author):
        self.name=name
        self.author=author
    @classmethod
    def updet_price(cls, price):
        cls.price=price
    def show_detail(self):
        print("Book name =",self.name)
        print("Book Author =",self.author)
        print("Book price =",Book.price)
obj=Book
obj.book_detail("python","vivek")
obj.show_detail()


