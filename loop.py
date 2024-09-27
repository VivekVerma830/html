# marks=int(input("enter student marks :"))

# if(marks >=90):
#     grade="A"
# elif(marks >=80 and marks < 90):
#     grade="B"
# elif(marks >=70 and marks < 80):
#     grade="c"
# else:
#     grade="D"

# print("Student marks=", grade)

#-----------------------------------
# num = int(input("enter number "))

# if(num%2==0):
#     print("Even")
# else:
#     print("Odd")
    
#---------------------------------------

# a= int(input("Enter number:"))
# b= int(input("Enter number:"))
# c= int(input("Enter number:"))

# if(a >= b and a >= c):
#     print("first number is largest",a)
# elif(b >= c):
#     print("second number is largest",b)
# else:
#     print("3rd is largest number" , c)

#---------------------------------------
# num=int(input("Enter number:"))
# if (num%7==0):
#     print(num,"is divisible by 7")
# else:
#     print(num, "is not divisible by 7")

#---------------------------------------

# i =1
# while  i<=5 :
#     print("hello :",i)
#     i+=1

#---------------------------------------
# i = 5
# while  i>=1 :
#     print(i)
#     i-=1

#---------------------------------------
# i = 1
# while i<=100:
#     print(i)
#     i += 1

#---------------------------------------
# i =100
# while i>=1:
#     print(i)
#     i-=1


#---------------------------------------
# n = int(input("enter number:"))
# i = 1
# while i <= 10:
#     print(n*i)
#     i +=1

#---------------------------------------
# num = [1,4,9,16,25,36,46,64,81,100]

# idx = 0
# while idx < len(num):
#     print(num[idx])
#     idx += 1

# ---------------------------------------
# num = (1,4,9,16,25,36,46,64,4,81,100,4)
# x = 4
# i = 0
# while i < len(num):
#     if (num[i] == x):
#         print("found : ", i)
#         break
#     else:
#         print("finding....")

#     i += 1

# ---------------------------------------

# i = 0
# while i <= 5:
#     if(i == 3):
#         i +=1
#         continue
#     print(i)
#     i  += 1

# ---------------------------------------
# i = 0
# while i <= 10:
#     if(i%2 == 1):
#         i +=1
#         continue
#     print(i)
#     i  += 1

# ---------------------------------------
# nums = []
# g = 0
# sum = 0
# avg = 0
# str="this is 909 speaking"
# for val in str:
#     sum += g
#     avg =(str/g)
#     g += 1
#     print(sum,avg )

# ---------------------------------------
# num = [1,4,9,16,25,36,46,64,81,100]
# for val in num:
#     print(val)

# -----------------------------------

# nums = [1,4,9,16,25,36,49,64,81,49,49,100]
# x = 49
# inx = 0
# print(nums.count(x))
# for el in nums:
#     if(el == x):
#         inx += 1   
# print("number is found :", inx)

# -----------------------------------
# num = [15, 6, 7, 10, 12, 20, 10, 28, 10]
# x = 10 
# count = 1
# for el in num:
#     if(el == x):
#        print(count)
#        count += 1
   
# 

# num = [15, 6, 7, 10, 12, 20, 10, 28, 10]
# x =10
# ind = 0
# while(num < len(num)-1):
#     if(num == x):
#        print("number is founded",num)
#        ind+=1
        
#-----------------------
# def testeven(n):
#     if n % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# # List to be processed
# lis = [33, 33, 56, 90, 89]

# # Applying testeven() to each element of the list using map()
# result = list(map(testeven, lis))

# # Displaying the result
# print("Status of each element in the list:")
# print(result)

#-----------------------
# marks = [22, 33, 4, 55, 6, 77, 8, 99, 21, 12, 2]

# # Find the maximum mark
# max_mark = max(marks)

# # Find the minimum mark
# min_mark = min(marks)

# # Calculate the average mark (using sum() and len() for efficiency)
# average_mark = sum(marks) / len(marks)

# # Find the number of students who scored above the average
# above_average = sum(mark > average_mark for mark in marks)

# # Find the number of students who scored below the average
# below_average = sum(mark < average_mark for mark in marks)

# # Print the results
# print("Maximum mark:", max_mark)
# print("Minimum mark:", min_mark)
# print("Average mark:", average_mark)
# print("Number of students above average:", above_average)
# print("Number of students below average:", below_average)
        
        
#-----------------------

# marks = [22, 33, 4, 55, 6, 77, 8, 99, 21, 12, 2]

# # Find the maximum mark
# max_mark = max(marks)
# min_mark = min(marks)
# print(max_mark)
# print(min_mark)
#-------------------------
# rows = 5

# for i in range(rows, 0, -1):
#     for j in range(0, i):
#         print("*", end=' ')
#     print()

# def half_inverted_triangle(height):
#     for i in range(height, 0, -1):
#         print("*" * i)

# # Example usage:
# height = 5
# half_inverted_triangle(height)
#------------------------------------
# def testeven(n):
#     if n % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# # List to be processed
# lis = [33, 33, 56, 90, 89]

# # Applying testeven() to each element of the list using map()
# result = list(map(testeven, lis))

# # Displaying the result
# print("Status of each element in the list:")
# print(result)

#-----------------------------

# def is_palindrome(s):
#   return s == s[::-1]
# s = "my mom and dad, both are arrived at noon"



# output_string = " ".join([word for word in s.split() if is_palindrome(word)])
# print(s.split)
# print(output_string)
#--------------------------

# s="my name is sumit"
# m= s.split()
# k=m[::-1]
# print(k)



# def frequency_setter(numbers):
#     frequency_dict = {}
#     for num in numbers:
#         if num in frequency_dict:
#             frequency_dict[num] += 1
#         else:
#             frequency_dict[num] = 1
#     return frequency_dict

# # Example usage:
# numbers = [1, 2, 3, 4, 5, 2, 3, 1, 1, 4, 4, 4]
# result = frequency_setter(numbers)
# print(result)
#-------------------------------

class RecordSystem:
    def _init_(self):
        self.records = {}

    def meet_record(self, enrollment_number, names_and_addresses):
        self.records[enrollment_number] = names_and_addresses

    def search(self, enrollment_number):
        if enrollment_number in self.records:
            print("Enrollment Number:", enrollment_number)
            for index, (name, address) in enumerate(self.records[enrollment_number].items()):
                print(f"Name {index+1}: {name}")
                print(f"Address {index+1}: {address}")
        else:
            print("Record not found for the given Enrollment Number.")

record_system = RecordSystem()
record_system.meet_record(1223, {"ajay": "bhopal"})
record_system.meet_record(1224, {"sckhur": "bhopal"})
record_system.meet_record(1225, {"aditya": "ujjain"})

print("Output of meet_record(3):")
print(record_system.records)

print("\nOutput of search(1225):")
record_system.search(1225)
