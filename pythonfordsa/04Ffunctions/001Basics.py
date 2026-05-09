def fun():
    print("Welcome to GFG")
    
fun()


def evenOdd(x):
    if (x % 2 == 0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(16))
print(evenOdd(7))

####  Positional Arguments
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10)

###arbitrary arguments
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("Keyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun('Hey', 'Welcome', first='Geeks', mid='for', last='Geeks')


def sq_value(num):
    return num**2

print(sq_value(2))
print(sq_value(-4))


'''

Pass by Reference and Pass by Value
Variables refer to objects. Function behavior depends on whether the object is mutable or immutable.

Mutable objects like lists can be modified inside functions.
Immutable objects like integers and strings remain unchanged.

'''

def myFun(x):
    x[0] = 20

b = [10, 11, 12, 13]
myFun(b)
print(b)

def myFun2(x):
    x = 20

x = 10
myFun2(x)
print(x)