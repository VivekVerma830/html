#multilevel-----------
# class A:
#     name ='vivek'
#     def m1(self):
#         return ("this is m1 method")
    
# class B(A):
#     age=22
#     def m2(self):
#         print("Name=" ,A.name)
#         print("m1=",self.m1())

# class c(B):
#     def m3(self):
#         print("Age=",B.age)
#         self.m2()
# obj =c()
# obj.m3()

#--------------------------------------

# class parent1:
#     def m1(self):
#         print("parent1 method called")

# class parent2:
#     def m1(self):
#         print("parent2 method called")

# class child (parent2,parent1):
#     def m2(self):
#         self.m1()

# obj =child()
# obj.m2()

#---------------------------------------
# class parent1:
#     def m1(self):
#         print ("parent1 method called")

# class parent2:
#     def m2(self):
#         print ("parent2 method called")

# class child (parent1,parent2):
#     def m3(self):
#         self.m1()
#         self.m2()

# obj =child()
# obj.m3()

#-------------------------------------------------
class A:
    def m1(self):
        print("m1 called from A")

class B(A):
    def m1(self):
        print("m1 called from B")
        super().m1()

obj=B()
obj.m1()