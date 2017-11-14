fname = input('File: ')
try:
    fhandle = open(fname)
except FileNotFoundError:
    raise SystemExit

days = dict()
for line in fhandle:
    line = line.split()
    if len(line) < 2 or line[0] != 'From':
        continue
    domain = line[1][line[1].find('@')+1:]
    days[domain] = days.get(domain, 0) + 1

print(days)
