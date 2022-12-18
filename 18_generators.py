# The Yield keyword in Python is similar to a return statement used for returning values or objects in Python. However, 
# There is a slight difference. The yield statement returns a generator object to the one who calls the function which contains yield,
# Instead of simply returning a value. 

# Next square

def next_square():
    i = 1
    while True:
        yield i * i
        i += 1


for n in next_square():
    if n > 25:
        break
    print(n)


# Fibonacii

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

for f in fib():
    if f > 100:
        break
    print(f)