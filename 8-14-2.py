fname = input('File: ')
try:
    fhand = open(fname)
except:
    raise SystemExit
count = 0
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) <= 2 : continue
    if words[0] != 'From' : continue
    print(words[2])
