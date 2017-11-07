fname = input('File: ')
try:
    fhandle = open(fname)
except:
    raise SystemExit
count = 0
for line in fhandle:
    line = line.split()
    if len(line) > 1 and line[0] == 'From':
        count = count + 1
        print(line[1])
print('There were {} lines in the file with From as the first word'
      .format(count))
