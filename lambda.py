#Program -

def return_sum(func, L):
    result = 0

    for i in L:
        if func(i):
            result = result + i
        
    return result
    
L = [11, 13, 19, 18, 56, 68, 35, 39, 48]

x = lambda x: x%2 == 0
y = lambda x: x%2 != 0
z = lambda x: x%3 == 0

print(return_sum(x, L))
print(return_sum(y, L))
print(return_sum(z, L))

#Program -

def return_sum(func, L):
    result = 0

    for i in L:
        if func(i):
            result = result + i

    return result   # <-- fixed indentation


L = [11, 14, 21, 23, 56, 78, 45, 29, 28]

x = lambda x: x % 2 == 0
y = lambda x: x % 2 != 0
z = lambda x: x % 3 == 0

print(return_sum(x, L))  # sum of even numbers
print(return_sum(y, L))  # sum of odd numbers
print(return_sum(z, L))  # sum of numbers divisible by 3

#Program -

def return_sum(func, L):
    result = 0

    for i in L:
        if func(i):
            result = result + i

    return result

L = [11, 14, 16, 18, 21, 25, 29, 31, 33, 35]

x = lambda x: x%2 == 0
y = lambda x: x%2 != 0
z = lambda x: x%3 == 0

print(return_sum(x, L))
print(return_sum(y, L))
print(return_sum(z, L))
