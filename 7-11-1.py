fname = input('File: ')
try:
    fhandle = open(fname)
except FileNotFoundError:
    print('File {} not found'.format(fname))
    raise SystemExit
for line in fhandle:
    print(line.rstrip().upper())
