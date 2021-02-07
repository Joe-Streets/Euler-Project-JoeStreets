t=600851475143

x=2
store = []
while x <= t:
    if t%x == 0:
        store.append(x)
        print(x)
        t=t/x
    else:
        x=x+1


print (store)
