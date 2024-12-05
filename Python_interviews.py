# 1. Decorators
# 2. generators
# 3. Memory Management in Python
# 4. scope in python

def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b,b+a

f1 = fib()
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))


