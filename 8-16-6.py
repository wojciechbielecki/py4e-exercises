numbers = list()
while True:
    value = input('Enter a number: ')
    if value == 'done':
        break
    try:
        value = float(value)
    except ValueError:
        print('Invalid input')
        continue
    numbers.append(value)

if numbers:
    print(f'Maximum: {max(numbers)}\nMinimum: {min(numbers)}')
