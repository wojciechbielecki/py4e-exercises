def addtwo(a, b):
    result = a + b
    return result

try:
    x = float(input('x: '))
    y = float(input('y: '))
    z = addtwo(x, y)
    print(z)
except:
    print('Enter a number')
