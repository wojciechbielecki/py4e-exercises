minimum = None
maximum = None
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
    if minimum is None or minimum > value:
        minimum = value
    if maximum is None or maximum < value:
        maximum = value
print(minimum, maximum)
