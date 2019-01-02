def func(n):
    f = lambda a,b : 0
    for i in range(n):
        f =  lambda a,b : (a**i)*(b**(n-i))
    return f

quad = func(4)
print(quad(2,3))
