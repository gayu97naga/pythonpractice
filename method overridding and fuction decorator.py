#decorated  functions with parameters:
def make_pretty(func):
    def inner():
        print("i got decorated")
        func()
    return inner
def ordinary():
    print("i am ordinary")
decorated_func=make_pretty(ordinary)
decorated_func()
        

def smart_divide(func):
    def inner(a,b):
        print("i am going to divide",a,"and",b)
        if b==0:
            print("oops cannot divide")
            return
        return func(a,b)
    return inner
@smart_divide
def divide(a,b):
    print(a/b)
divide(2,5)
divide(2,0)


def outer(x):
    def inner(y):
        return x+y
    return inner
add_five=outer(5)
result=add_five(6)
print(result)


#function pass aruguments:

def add(x,y):
        return x+y
def calculate(func,x,y):
    return func(x,y)
result=calculate(add,4,6)
print(result)
















