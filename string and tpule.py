# mov1=input("Enter movie name:")
# mov2=input("Enter movie name:")
# mov3=input("Enter movie name:")
# movies=[]
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

#----------------------------------------------------
# list1=[1,2,3,2,1]

# copy_list1=list1.copy()
# copy_list1.reverse()

# if(copy_list1==list1):
#     print("this is palindrome")

# else:
#     print("this is not palindrome")

#----------------------------------------------------
# lis=["c","d","a","a","b","b","a","c"]
# print(lis.count("a"))   

#------------------------------------

# lis=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
#       'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# lis.sort(reverse=True)
# print(lis)

#------------------------------------
# subject = {"python","java","js","python","java","python","java","c++",
#        "c++"}
# print(len(subject))

# -----------------------------------
# marks ={}

# x = int(input("enter py marks: "))
# marks.update({"py":x})

# y = int(input("enter chem marks: "))
# marks.update({"chem":y})

# z = int(input("enter maths marks: "))
# marks.update({"maths":z})
# print(marks)

# -----------------------------------

# for i in range(1,100):
#     print(i)

# for i in range(100,0,-1):
#     print(i)

# num = int(input('Enter a number :'))
# for i in range (1,11):
#     print(num * i)

n = 4
sum =0
for i in range(1, n+1):
    sum *= i
print(sum)