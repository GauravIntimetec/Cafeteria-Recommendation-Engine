
def decorator_add_two(fun):
    def inner(*args, **kwargs):
          print("about to execute fun")
          set =  fun(*args, **kwargs)
          print("Fun Executed")
          return set
    return inner

# @decorator_add_two
def sqr_numbers(num):
    print("sqr function")
    return num*num

decorated_fun = decorator_add_two(sqr_numbers)
print(decorated_fun(6))
# print(sqr_numbers(6))

