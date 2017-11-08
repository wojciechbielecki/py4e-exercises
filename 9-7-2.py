fname = input('File: ')
try:
    fhandle = open(fname)
except:
    raise SystemExit

days = dict()
for line in fhandle:
    line = line.split()
    if len(line) < 3 or line[0] != 'From': continue
    days[line[2]] = days.get(line[2], 0) + 1

print(days)
