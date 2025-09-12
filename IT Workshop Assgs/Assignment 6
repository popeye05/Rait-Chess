#Functions in Python------------------------------------------------------------------------
'''
def f1(): #This is how we define a function in python; Here f1 doesnt   accept any parameter
    print("Hello") 
f1()
def f2(name):
    print(name)
f2("Swarnab") #This accepts a single parameter
#Now,lets see a fx which returns a value.
def sqrx(x):
    x=x**2
    return x
'''
#-----------------------------------------------------------------------------------------------

#Q1. Write a recursive function fibo(), which will take an integer as input(n) and show the Fibonacci Series
#    up to n-terms. Make sure that the default value of n is 1.
'''
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
list1 =[]
n=int(input("Enter the range: "))
for i in range (0,n):
    list1.append(fibo(i))
print(list1)

-------------------------------------Alternative Method------------------------------------------------
def fibo(n=1,a=0,b=1,i=0):
        if i<n:
            print(a," ",end='')
            return fibo(n,b,a+b,i+1)
fibo(7)
-------------------------------------------------------------------------------------------------------
'''
#Q2. Write a recursive function fibo_n(), which will take an integer as input(n) and returns the n-th
#term of Fibonacci Series. Make sure that the default value of n is 1.
'''
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("Enter Number: "))
print(fibo(n))
'''
#Write a function gcdlcm(), which will take two integers (a, b) as input and return the GCD and LCM of
#these two. Make sure that the default value b is 1.
def gcdlcm(a,b):
    if a%b==0:
        return b
    else:
        return gcdlcm(b,a%b)
    
print(gcdlcm(24,8))
#With using gcd, to compute lcm
print("LCM is: ",(24*8)//gcdlcm(24,8))
#LCM without using gcd
def lcm(a,b,i=2):
    n = max(a,b)
    if i==n:
        return a*b
    else:
        if a%i==0 and b%i!=0:
            return lcm(a//i,b,i)
        elif a%i!=0 and b%i==0:
            return lcm(a,b//i,i)
        elif a%i==0 and b%i==0:
                return lcm(a//i,b//i,i)
        elif a%i!=0 and b%i!=0:
            return lcm(a,b,i+1)
print("My LCM fx returns:",lcm(24,8))

        

    

