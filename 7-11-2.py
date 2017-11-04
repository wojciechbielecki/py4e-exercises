fname = input('File: ')
try:
    fhandle = open(fname)
except FileNotFoundError:
    # Easter Egg from Exercise 3
    if fname == 'na na boo boo':
        print('Easter Egg!')
    else:
        print('File {} not found'.format(fname))
    raise SystemExit
total = 0
count = 0
for line in fhandle:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    col_pos = line.find(':')
    try:
        confidence = float(line[col_pos+1:])
    except ValueError:
        print('Illegal characters in line')
        raise SystemExit
    total = total + confidence
    count = count + 1
try:
    average = total / count
except ZeroDivisionError:
    print('Spam condifdence values not found')
    raise SystemExit
print('Average spam confidence', average)
