
# print("Enter two numbers")
# a = int(input ())
# b = int(input ())
# c=a+b
# print("sum is", c)

#1 write a program to print MysirG five times on the screen.

# i=1
# while i<=5:
#    print("MySirG")
#    i+=1


#2 write a program to print first N natural numbers

# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     print(i)
#     # print(i,end=" ")
#     i+=1

#3 write a program to calculate sum of first N natural numbers.

# n=int(input("Enter a number: "))
# i=1
# s=0
# while i<=n:
#     s=s+i
#     i+=1
# print("Sum is",s)

#4 write a program to check whether a given number is the prime munbern or not.

# n=int(input("enter a n number: "))
# i=2
# while i<=n-1:
#     if n%i==0:
#         break
#     i+=1
# if i==n:
#     print("Prime")
# else:
#     print("Not Prime")

#5 write a program  to print unicode of each character of the string "MYSIRG".

# s1="NitinYadav"
# for a in s1:
#     # print(a)
#     print(a,ord(a))

#6 write a program to print first n natural numbers.

# print("Enter a number")
# n=int(input())
# for e in range(1,n+1):
#      print(e,end=' ')
# print()

#7 write a program to print squares of first n natural numbers.

# print("Enter a number")
# n=int(input())
# for e in range(1,n+1):
#      print(e**2,end=' ')
# print()

#8 write a python script to print first 10 odd natural numbers.

# i=1
# while i<=19:
#     print(i,end=' ')
#     i+=2

# i=1
# while i<=10:
#     print(2*i-1,end=' ')
#     i+=1

# for i in range(1,11):
#     print(2*i-1,end=' ')
# print()

#9 write a python script to print squares of first N natural numbers.

# i=1
# while i<=10:
#     print(i**2,end=' ')
#     i+=1
# print()

#10 LCM program.

# print("Enter two numbers")
# a=int(input())
# b=int(input())
# L= a if a>b else b
# while L<=a*b:
#     if L%a==0 and L%b==0:
#         print("LCM is",L)
#         break
#     L+=1
# print()


#11
# def f1():
#     print("Enter a number")
#     n=int(input())
#     for e in range(1,n+1):
#         print(e**2,end=' ')
#         print()

# f1() #function call
# f1() #function call

#12

# def f1(a,b,d):
#     c=a+b+d
#     print("Sum is",c)

# f1(3,5,7) #function call
# f1(10,20,0) #function call

#13

# def f1(a,b):
#     print("a=",a,"b=",b)

# f1(2,3)

# #14 code

# class Test:
#     x=10
#     def f1():
#         m1=4
#     def __init__(self,a):
#         self.a=a


# t1=Test(3)
# t2=Test(5)

#All variable names in above code.
#x,m1,a,f1.a,t2.a,t1,t2 | f1,__init__, Test,self

# x --- class object variable
# m1 --- local variable
# a --- local variable
# t1.a --- Instance object variable
# t2.a --- Instance object variable
# t1 --- global variable 
# t2 --- global variable 
# self --- local variable 
# Test --- global variable
# f1 --- Variable to represent function object
# __init__ ---  Variable to represent function object


class Test:
    def f1(self):   #instance method
        self.a=10
    @staticmethod    
    def f2():
        print("Hello")
    @classmethod
    def f3(cls):
        cls.x=5

def fun():
    print("Non member function")
    
