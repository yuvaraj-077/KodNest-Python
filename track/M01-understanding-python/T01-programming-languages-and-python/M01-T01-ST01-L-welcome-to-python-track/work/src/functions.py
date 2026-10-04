# add 2 numbers
#No argyments + No return value
def add1():
    a, b = 10, 10
    c = a + b
    print(c)
add1()

def sub1():
    a, b = 30, 15
    c =  a - b
    print(c)
sub1()

def multiply1():
    a, b = 25, 25
    c = a*b
    print(c)
multiply1()

def div1():
    a, b = 40, 20
    c = a/b
    print(c)
div1()

# No arguments + Return value
def add2():
    a, b = 10, 20
    c = a + b
    return c
print(add2())

def sub2():
    a, b = 40, 10
    c = a-b
    return c
print(sub2())

def multiply2():
    a,b=10,20
    c=a*b
    return c
print(multiply2())

def div2():
    a,b=50,25
    c=a/b
    return c
print(div2())
# Arguments + No return value
def add3(a,b):
    c = a + b
    print(c)
add3(10,50)

def sub3(a,b):
    c = a - b
    print(c)
sub3(40,10)

def multiply3(a,b):
    c = a * b
    print(c)
multiply3(10,20)

def div3(a,b):
    c = a / b
    print(c)
div3(50,25)
# Arguments + Return value
def add4(a,b):
    c = a + b
    return c
res = add4(100, 200)
print(res)

def sub4(a,b):
    c = a - b
    return c
res = sub4(400, 100)
print(res)

def multiply4(a,b):
    c = a * b
    return c
res = multiply4(400, 50)
print(res)

def div4(a,b):
    c = a / b
    return c
res = div4(100, 100)
print(res)
