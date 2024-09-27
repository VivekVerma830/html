def decorator(fun):
    def wrapper():
        print("start work")
        fun()
        print("stop work")
    return wrapper
def original_fun():
    print("this is vivek ")
var=decorator(original_fun)
var()