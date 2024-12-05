def fibanacci(n):
    a,b = 0,1
    for i in range(n):
        yield a
        a,b = b, a+b

gen = fibanacci(4)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

    
