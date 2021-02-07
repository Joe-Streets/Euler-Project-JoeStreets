#The sum of the squares of the first ten natural numbers is,

#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,

#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.
#sumSquareDifference(100) should return 25164150.
#sumSquareDifference(20) should return 41230.

n = input("Enter an integer value 'n' to find outthe difference between the sum of the squares of the first n natural numbers and the square of the sum:")
n = int(n)

def SumSquares(x):
    SuSq = 0
    i=x
    for i in range(1,x+1):
        SuSq=SuSq + i**2
    print(SuSq)
    return SuSq

def SquareSum(x):
    SqSu = 0
    i=x
    for i in range(1,x+1):
        SqSu=SqSu+i
    SqSu=SqSu**2
    print(SqSu)
    return SqSu

def sumSquareDifference(x):
    return SquareSum(x)-SumSquares(x)

print(sumSquareDifference(n))