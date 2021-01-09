a=1
b=2
c=0
n=4000000

Count = 0

while b <= n:
    if b % 2 == 0:
       Count = Count + b
    c = a + b
    print(b)
    a = b
    b = c

print(Count)