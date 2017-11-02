total = 0
count = 0
average = None
while True:
    value = input('Enter a number: ')
    if value != 'done':
        try:
            value = float(value)
        except:
            print('Invalid input')
            continue
    else:
        break
    total = total + value
    count = count + 1
try:
    average = total / count
except:
    pass
print(total, count, average)
