#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n?

from functools import reduce
#users value entered as 'n'
n = input("Enter an integer value 'n' to find out the smallest positive number that is evenly divisible by all of the numbers from 1 to n:")
n = int(n)
#First attempt
#create gaurenteed value to start from.
#StartPointValue = math.factorial(n)
#SmallestPossible = StartPointValue
#TestValue = StartPointValue
#i= n
#while TestValue >= n:
#    while i > 1 :
#        if TestValue%i == 0:
#            i=i-1
#            if i == 2:
#                SmallestPossible = TestValue
#                TestValue = TestValue -n
#        else:
#            TestValue = TestValue -n
#            i=1
#    i=n
#print(SmallestPossible)

#SLow for values over 11, needs a different approach

#Dont on paper, we'd write out all factors in the valuese 1-n, then remove commonalities that are not required.
#Product of the remaining is what is required.

def GreatestCommonDivisor(x,y):
    while y>0:
        x, y = y, x%y
    return x

def LowestCommonMultiple(x,y):
    return x*y//GreatestCommonDivisor(x,y)

def RecursiveLCM(*args):
    return reduce(LowestCommonMultiple,args)

print(RecursiveLCM(*range(1,n+1)))