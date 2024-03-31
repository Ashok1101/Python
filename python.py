# ---python course---

"""---print()---"""

print ('Hello World')
print(1+87)
print(2_2_3*2)    # 2_2_3 == 223
''' multiline           
    comment'''
print("arvind",end="-")   # end="" is used so that next print gets same line
print('patel')
print("arvind",'shamji','patel',sep="!")  # bydefault sep value is space
print('arvind','patel') 
print('''arvind
shamji
patel''')
print('arvind\npatel\t1')
print('verat\\patel')

# ---escape sequences:---

"""
    \n 	Inserts a new line in the text at the point
    \\	Inserts a backslash character in the text at the point
    \"	Inserts a double quote character in the text at that point

    \'	Inserts a single quote character in the text at that point
    \t	Inserts a tab in the text at that point

    \f	Inserts a form feed ln the text at that point
    \r	Inserts a carriage return in the text at that point

    \b	Inserts a backspace in the text at that point
"""
name="arvind patel"
print(name)
print(type(name))   # to know datatype

num=89    # int datatype
num=str(num)        # typecasting- to change datatype to desire datatype 
print(type(num))
# print(int('12.89'))    # gives error ->  typecasting must be done in 1 step to desired value
print(10 * 'arvind')  # prints 10 times

# ---input()---

print('enter a number:')
#num=input()
print('you entered:',num)
#num=input('enter a number:')   # input takes no. as string

# ---string---

name1='''Arvind's Pate"l'''
print(name1)
print(name + name1)   # Concatenation 
print(name[5])    # indexing starts with 0 
# name[1]=z  # doesn't work,bcoz strings are immutable

# string slicing
print(name[0:4])
print(name[0:4:2])
print(name[-4:-2:-1])  # ::-1 - reverses the string
print(name[::-2])  # reverses string and skip 1 character and so on
print(name[::])    # bydefault values-[0:n:1]
#print(name[100])   # throws error as out of range 
print(name[:100])   # it will not gives error
# string function
print(len(name))
print(name.endswith('tel'))   # returns True if present
print(name.count('a'))
print(name.capitalize())    # capitalize only 1st character
print(name.title())         # capitalize all 1st character of words
print(name.upper())        # capitalize all character
print(name.lower())
print(name.isalnum())    # returns false if empty space is present
print(name.isalpha())
print(name.find('a',))   # returns index when first encounter and if not present returns -1
print(name.replace('arvind','ashok'))
name="      arvind patel    "
print(name.strip())      # removes leading and trailing spaces

import time      # inbuilt module
time.sleep(2)
print("2 sec passed since program run")
 
from math import *
print(sqrt(16))

#  --assignment operator--

a=44
a**=2
a/=22
print(a)
print(12//5) # returns only int value after division i.e 2
print(5**2)  # 5 to the power 2 = 25 
a=int(a)
# comparison operator
b=(a!=2)
print (b)
# Logical operator
b=0
print(a & b)
print(a and b)
print(a|b)
print(a or b)
print(not b) 

# list  -> mutable ,indexed,ordered          

l=[]   # empty list
print(l)
print(type(l))
l=[45,9,0,7,90]     
print(l)
print(l[1])   # access using index
l[1]=55     # change the value of list
l1=[90,55,"arvind",2,"patel",True,3.5]
print(l1[0:4])
l.sort()
print(l)
l.reverse()
print(l)
l.append(99)   # add 99 at end of list
print(l)
l.insert(3,10)  # insert 10 at index 3
print(l)
l.pop(1)  # removes element at index 3
print(l)
l.remove(10)  # removes 10 from list 
print(l) 
print(l1.index(True))   # returns index
# Tuples  -> immutable,indexed,unordered,duplicasy allowed
l=()     # empty Tuple
l=(2,)    # single element tuple{ , is imp}
l=(21,90,45,7,0,99)
print(l)
l=(21,90,45,7,0,99,0.0,'arvind',False,0)
print(l)
print(type(l))
print(l[2])
print(l.count(0))
print(l.index(0))    # returns index of first encountered

# Dictionary ->mutable,unordered,indexed,duplicate keys not allowed, if tried it overwrite

l={"name":"arvind","course":"python","marks":[1,3,5],"anotherdict":{"name":"arvind","marks":90}}
print(l)
print(type(l))
print(l['marks'])
print(l["anotherdict"]['marks'])
print(l.keys())
print(l.values())
print(l.items()) # prints all keys and values as elements of tuple
l1={
    "surname":"patel"
}
l.update(l1)
print(l)
print(l.get("div"))  # if not present it returns none
# print(l["div"])    # if not present returns error that's why get() is preferable

# Sets  --> unordered,no repetition,unindexed,unmutable
l={}
print(type(l))
l=set()
print(type(l))
l={21,90,45,7,0,99,0.0,(5,2,6)}  # can't add list,dict bcoz this are mutable 
print(l)
l.add(3)
print(l)
l.remove(0)  # throws error if not present
print(len(l))
print(l.pop())  # removes arbitary(any) element and returns removed element 
#l.clear()   # empties the set l
print(l.union({4,6}))
print(l.intersection({0,99,1})) # returns set with items in both sets

# ASCII value
print(ord('A'))   # ord is used to get represented int value
print(chr(65))   # returns character representing int value

# if else loop(elif ladder)

# age=int(input("Enter your age:"))
age=3
print('you are eligible') if age>18 else print('you are not eligible') # if else in 1 sentence
if(age==18 or age>18):
    print("you are eligible ")  # indentation(1tab/4spaces)
elif(age<18):
    print("you are not eligible")
else:
    print("not a valid age")
# is/is not  
a=None
if (a is not None):     # works as '==' , difference btw them is 'is' checks address and '=' checks value
    print('not none')
else:
    print(a)
# in/not in   {membership}
b=[6,8,9]
if(6 not in b):
    print("6 is not present")
else:
    pass          # pass instructs to do nothing

# while loop
while age>0:
    print(age)
    age-=1
i=5
while i>=0:
    print(i*"*")
    i-=1
# for loop
for i in b:    # used for iteration
    print(i)
for i in range(3):   # range starts with 0 and ends up in n-1 (n is excluded)
    print(i)
    
# for with else 

for i in range(0,8,2):
    print(i)
    if i==4:
        break
else:                                        # executes only after complete termination
    print("successful execution done!")

for i in range(1,8):
    if i==5:
        continue           # break and continue are called as jump statements
    print(i)
for i in range(5):
    
    if(i==0 or i==4):
        print(5*"*")
    
# f-string
num=2
for i in range(1,6):
    print(str(num)+"X"+str(i)+"="+str(i*num))     # concatenation
    print(f"{num}X{i}={num*i}")  # in this, {} is used for variable
print("my name is :{1} and i am in :{0}".format('Arvind','Mumbai'))   # .format
    
fact=1             # factorial using iteration
for i in range(5):
    fact=fact*(i+1)
print(f"factorial of 5 is: {fact}")

# function
def sum(num1,num2):
    return num1+num2

print(f"sum={sum(5,6)}")  # function call

# default arguement

def greet(name='arvind'):
    print("good morning",name)
greet()
# factorial using recursion
def fact(n):
    if n==1:      # base condition is imp for recursion to stop
        return n  
    return n*fact(n-1)
print(fact(5))
 
n=4
for i in range(n):
    print(" "*(i),end="")
    print('*'*(n-i))

# Files handling
f=open('sample.txt','w')      # automatic creates a file
f.write("arvind shamji patel")   # accept only str
f.writelines(['arvind','shamji','verat or patel'])
f=open('sample.txt','r')
data=f.readlines()      # returns all the lines in a form of list
print(data)
data=f.read(5)   # reads 5 character ; bydefault reads complete files
print(data)
print(f.tell())    # returns index of current position
print(f.seek(3))   # prints from index 3 to end
data=f.read()
if('patel' in data):
    print("patel is present")
else:
    print("not present")
data=f.readline()   # reads 1st line 
print(data)
data=f.readline()   # reads 2nd line
print(data)
f.close()
with open('sample.txt','a') as f:       # with is used bcoz it close file automatically
    a=f.write("arvind shamji patel")
    print(a)      # write() returns no.of character 
# modes of file
# r -> read   -bydefault read, if nothing is written
# w -> write  (new content overwrite old content after file close) 
# a -> append  (adds new content to old content)
# r+ ->for read and write both
# + -> updating
# rb -> open for read in binary mode
# rt -> open for read in text mode{here 't' is optional}
 
# object oriented programming

# Modelling a problem in OOPs:-

# We identify the following in our problem:
# Noun -> Class -> Employee
# Adjective -> Attributes -> name,age,salary
# Verbs -> Methods -> getSalary(), increment()

class add:
    def sum(self):      # self is not keyword ,we can pass can variable but any parameter must be passed
        return self.a + self.b
    
num=add()
num.a=5
num.b=6
print(num.sum())   # add.sum(num) {self=num}
''' 
PascalCase   # classname is written is pascalcase
eg: EmployeeName
camelCase
eg:isNumeric,isFloatOrInt
'''
class emp:
    company="google"      # class attribute
    salary=1000
    _balance=100            # protected attribute
    __password=2345          # private attribute
    
amit=emp()             # obj instantiation
raj=emp()
print(amit.company)
emp.company="youtube"      # changing class attribute
print(raj.company)
amit.salary=10000        # adding obj attribute
raj.salary=5000
print(raj.salary)     # instance(obj) attribute is given preference over class attribute
print(raj._emp__password)      # name mangling to use private attribute
# ---static_method---

class emp:
    company='google'
    def getsalary(self,sign):
        print(f"Salary is {self.salary} in {self.company}\n{sign}")
        
    @staticmethod     # is called decorator used when function doesn't use self parameter
    def greet():
        print("Good Morning,Sir")
        
amit=emp()
amit.salary=10000   
amit.getsalary("Thanks!")     # emp.getsalary(amit)
amit.greet()            # emp.greet()
    
# __init__   -> is used to give arguements to class
class emp:
    company='google'
    def __init__(self,name):
        print("employee is created")
        self.name=name
    def getdetail(self):
        print(self.name)
    def getsalary(self,sign):
        print(f"Salary is {self.salary} in {self.company}\n{sign}")
        
    @staticmethod     # is called decorator used when function doesn't use self parameter
    def greet():
        print("Good Morning,Sir")
amit=emp('amit')
amit.getdetail()

# Inheritance 
# single inheritance
class para():    # Base class
    l=8
    b=5
class area(para):       #Derived class
    def getarea(self):
        self.area=self.l*self.b
        return self.area
rect=area()
a=rect.getarea()
print(a)
# multilevel inheritance
class para():
    l=8
    b=5
class area(para):
    def getvolume(self):
        self.area=self.l*self.b
        return self.area
class volume(area):
    h=2
    area =22
    def getvolume(vol):
        super().getvolume()    # super will take value of base class ignoring the value of derived class  
        vol.volume=vol.area*vol.h
        return vol.volume
        
rect=volume()
a=rect.getvolume()
print(a)

# multiple inheritance
class length():
    l=5
class breadth():
    l=4
    b=8
class area(length,breadth):   # preference is given to class which is written first,here class length is written before breadth
    def getarea(area):
        area.area=area.l*area.b
        return area.area
rect=area()
a=rect.getarea()
print(a)

# class method
class emp:
    salary=1900
    location='mumbai'
    # def changesalary(self,sal):
    #     self.__class__.salary=sal        # Dunder method to change class attribute
    @classmethod                         # method to change class attribute
    def changesalary(cls,sal):
        cls.salary=sal
e=emp()
print(e.salary)
e.changesalary(4500)
print(e.salary)
print(emp.salary)

# property decorator -> it is a function but acts/looks like property
class emp:
    salary=1900
    bonus=500
    # totalsalary=2400    
    @property                # method name with property decorator is called getter method
    def totalsalary(self):
        return self.salary + self.bonus
    @totalsalary.setter      # to change value of class attribute depended on another attributes 
    def totalsalary(self,val):
        self.bonus= val-self.salary
e=emp()
print(e.totalsalary)
e.totalsalary=3000    # changes in totalsalary will automatically invoke setter to change bonus accordingly
print(e.bonus)
print(e.salary)

# Dunder/Magic method

class number:
    def __init__(self,num):     # __init__ is also a dunder
        self.num=num
        
    def __add__(self,num):     
        print("let's Add")
        return self.num + num.num
    def __mul__(self,num):
        print("let's Multiply")
        return self.num * num.num
n1=number(4)
n2=number(6)
sum = n1 + n2     # + operator with objs invokes __add__
print(sum)
mul = n1 * n2     # * operator with objs invokes __mul__
print(mul)

# other Dender 
class number:
    def __init__(self,num):     
        self.num=num
    def __str__(self):
        return f"Decimal Number: {self.num}"
    def __len__(self):
        return 1
n=number(9)
print(n)
print(len(n))

# try-except handling
n1='kl'
n2=7
try:
    print("sum of 2 nos:",n1+n2)
except Exception as e:
    # raise SyntaxError("SyntaxError")
    print(e) 
    print("str+int-not possible")
else:
    print('successfully done')     # this executes when except is not running
finally:
    print('Done')              # runs in any condition in last

# Global & local variable and keyword
l=10       # global variable
def fun():
    m=5       # local variable
    global l
    l=l+5     # to change global variable global keyword is used
    print(l,m)
fun()

# x = 89
def marry():
    x = 20
    def rohan():
        global x
        x = 88      # this won't change value of marry's x
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)

marry()
print(x)

# lambda function or anonymous function
minus=lambda x,y : x-y
print(minus(9,4))

# args and kwargs ( to run function even if arguements are less than max arguements)

def funargs(normal, *argsrohan, **kwargsbala):    # args /kwargs are not keyword,it is mainly identified by *,** respectively
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")
        
har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam":"Cook"}
funargs(normal)   # no need to pass all arguements, only that which we want
funargs(normal, *har, **kw)
  
# Enumerate function        # it reduces code 
list_1=["code","with","harry"]
for index,val in enumerate(list_1,5):
    print(index,val)
# if__name__==__main__
print(__name__)     # returns file name ,if called/run from same file returns__main__
if(__name__=="__main__"):    # executes only if call from same file in which it is present
    password=12345
    print(password)
# Join function
l=["apple","mango","grapes","lychee"]
print(" or ".join(l),",etc")
# map,filter & reduce
#--------------------------MAP------------------------------
numbers = ["3", "34", "64"]
numbers = list(map(int, numbers))   # map is used to operation on each item 
print(numbers)

def sq(a):
    return a*a

num = [2,3,5,6,76,3,3,2]
square = list(map(sq, num))
print(square)
num = [2,3,5,6,76,3,3,2]       # maping using lambda
square = list(map(lambda x: x*x, num))
print(square)


def square(a):
    return a*a

def cube(a):
    return a*a*a

func = [square, cube]
num = [2,3,5,6,76,3,3,2]
for i in range(5):
    val = list(map(lambda x:x(i), func))
    print(val)

# --------------------------FILTER------------------------------
list_1 = [1,2,3,4,5,6,7,8,9]
def is_greater_5(num):
    return num>5

gr_than_5 = list(filter(is_greater_5, list_1))
print(gr_than_5)
# --------------------------REDUCE------------------------------
from functools import reduce  # returns single value after doing operation

list1 = [1,2,3,4,2]
num = reduce(lambda x,y:x*y, list1)
print(num)

# ---Abstract Method---

# from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod       
    def printarea(self):   # An error will occur if the abstract method has not been implemented in the derived class.
        return 0           # i.e all derived class must have abstract method in it.

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())

# Generators
"""
Iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration -

"""

def gen(n):
    for i in range(n):
        yield i

g = gen(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())
# print(g.__next__())


# for i in g:
#     print(i)

h = "arvind"
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
for c in h:
    print(c)
# Comprehension
listA = [i for i in range(10) if i%2==0]   # list Comprehension
print(listA)
dict1={i:f"item {i}" for i in range(25) if i%5==0}   # dict Comprehension
print(dict1)
set1 = {a for a in ["a", "a", "b", "c", "d", "d"]}
print(set1)

print('Insertion Sort:-')
l=[9,7,3,8,5,0]
for i in range(5+1):
    k=l[i]
    j=i-1
    while j>=0 and k<l[j]:
        l[j+1]=l[j]
        j=j-1
    else:
        l[j+1]=k
        print("Sorted List:",l)
        
print('Bubble Sort:-')
l=[9,7,3,8,5,0]
j=5
while j>0:
    for i in range(j):
        if(l[i]>l[i+1]):
            k=l[i]
            l[i]=l[i+1]
            l[i+1]=k
        print("Sorted list:",l)
    j=j-1
# Numpy   
import numpy as np
L=[1,2,3,4]
a=np.array(L)    #makes ‘a’ array from List ‘L’.
print( type(a) )   # numpy.ndarray
print(a.shape )    #(1,)
print(a.itemsize )   #4
print(a.dtype)

