# HOW TO MAKE A SUM OF TWO TERMS ?

def sum(a, b):
    return a + b

a = float(input('What is the first therm ? '))
b = float(input('What is the second therm ? '))

print(sum(a, b))


# HOW TO MAKE A SUBSTRATION OF TWO THERMS ?

def substration(a, b):
    return a - b

a = float(input('What is the first therm ? '))
b = float(input('What is the second therm ? '))

print(sum(a, b))


# HOW TO MAKE A MULTIPLICATION OF TWO THERMS ?
def multiply(a, b, n):
    if a * b == n:
        return 'That\'s correct !'
    else:
        return 'Try again !'
    
a = int(input('What\'s the first number ? '))
b = int(input('What\'s the second number ? '))
n = int(input('What\'s the answer ? '))

print(multiply(a, b, n))


# HOW TO MAKE A DIVISION OF TWO THERMS

def divide(a, b, n):
    if a / b == n:
        return 'That\'s correct !'
    else:
        return 'Try again !'
    
a = int(input('What\'s the first number ? '))
b = int(input('What\'s the second number ? '))
n = int(input('What\'s the answer ? '))

print(divide(a, b, n))




