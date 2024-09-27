import functools

# def max(x,y):
#     if x>y:

#         return x
#     else:
#         return y
    
# max_digit=functools.reduce(max,[1,2,5,7,8,9,10])
# print(max_digit)
#######################################
# def min(x,y):
#     if x<y:
#         return x
#     else:
#         return y
    
# min_digit=functools.reduce(max,[1,2,5,7,8,9,10])
# print(min_digit)

def sum(x,y):
    return x+y
       
sum_digit=functools.reduce(sum,[9,10])
print(sum_digit)