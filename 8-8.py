numlist = list()
while True:
    value = input('Enter a number: ')
    if value == 'done': break
    try:
        numlist.append(float(value))
    except:
        print('Invalid input')

try:
    average = sum(numlist) / len(numlist)
except:
    average = None
print('Average:', average)
print(numlist)
