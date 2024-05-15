# def add(a, b):
# from code import args
# from pip._vendor.rich.prompt import result
from functools import reduce

#     sum = a + b
    
#     minus = a - b
#     print(sum)
#     print(minus)

    
# add(4, 5)


# def xvb():
#     print("statement 1")
#     print("statement 2")

    
# xvb()
# xvb()
# xvb()


# def fun1():
#     print("Reached fun 1")

#     def fun2():
#         print("Inner avatar")
#     fun2()

#     print("Outer avatar")
    


# fun1()
# print(type(fun1))

    
# def cal_sum(x, y, z):
#     return x + y + z

    
# s1 = cal_sum(2, 4, 3)
# print(s1)

# a, b, c = 20, 30, 10
# s2 = cal_sum(a, b, c)
# print(s2)


# def atm(request):
#         if request == "B":
#             print("Check Balance")
#         elif request == "C":
#             print("Widrawll Cash")
#         elif request == "P":
#             print("Reset Pin")
#         else:
#             print("Enter Valid Option")


# request = input("Enter option: ")
# atm(request)


# def xyz(*args):
#     # print()
#     for i in args:
#         print(i, end=" ")
        
# xyz(29, 89,"khdsh",9.008)


# def sumOf(a, b):
#     addNum = a + b
#     return addNum

# print(sumOf(20,10))
    

# def addNum(a, b):
#     addt = a + b

    
# c = addNum(20, 10)
# print(addt)


# def addNum(a, b):
#     sumOf = a + b
#     print(sumOf)

# addNum(20,10)


# def addnum(a, b):
#     return a + b

# print(addnum(20,10))

    
# def square(num):
#     print(num ** 2)
    
# square(4)


# def square(num):
#     return num ** 2

# print(square(4))


# def sumOf(num1, num2):
#     sum = num1 + num2
#     return sum
    
# print(sumOf(20,380))


# def multiply(p1, p2):
#     result = p1 * p2
#     return result

    
# print(multiply(2, 50))
# print(multiply(5, "shubham "))


# def circle(radius):
#     area = 3.14 * radius**2
#     circumferance = 2 *3.14* radius 
#     return area, circumferance


# a, c = circle(3)
# print("Area: ", a, "Circumferance: ", c)


# def greet(name="User"):
#     return "Hello", name
    
# print(greet())

# cube = lambda x: x ** 3
# print(cube(3))


# def funct():
#     print("Hello World !")

    
# def sum(x, y):
#     print(x + y)

    
# f = funct()

# s = sum(10, 20)


# print("********")


# def sum(x,y):
#     print(x + y)

    
# def funct():
#     print("Hello")
    

# f=funct
# f()
# s = sum(10, 20)

# LAMBDA FUNCTION

# cube=lambda x: x*x*x
# print(cube(3))

# ops = lambda x, y, z:(x + y + z) / 3
# print(ops(10, 20, 30))

# print((lambda n:n * n * n)(3))

# cube=((lambda n:n * n * n)(3))
# print(cube)

# str = lambda s:s.upper()
# print(str("Shubham Shinde"))

# lst1=[1,2,3,4,5]
# lst2=[10,20,30,40,50]

# print((lambda l:sum(l)/len(l))(lst1))
# print((lambda l:sum(l)/len(l))(lst2))

# import math


# def fun(n):
#     return n + n-1

# lst=[5,10,15,20,25]

# m1 = map(math.radians, lst)
# m2 = map(math.factorial, lst)
# m3 = map(fun, lst)

# print(list(m1))    
# print(list(m2))    
# print(list(m3))    

# import functools


# def getsum(x, y):
#     return x + y

    
# def getprod(x, y):
#     return x * y

    
# lst = [1, 2, 3, 4, 5]

# s = functools.reduce(getsum, lst)

# p=functools.reduce(getprod, lst)

# print(s)
# print(p)

# m = map(lambda n: n * n, lst)
# print(list(m))

# f = filter(lambda n:n % 5 == 0, lst)
# print(list(f))

# # from functools import reduce

# r = reduce(lambda x, y : x * y, lst)
# print(r)


# def fun(n):
#     return n > 1000

    
# lst = [10, 20, 30, 40, 50]
# l = filter(fun, map(lambda x:x * x, lst))
# print(list(l))