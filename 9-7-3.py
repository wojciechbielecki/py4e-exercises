fname = input('File: ')
try:
    fhandle = open(fname)
except FileNotFoundError:
    raise SystemExit

days = dict()
largest_day = None
largest_value = None
for line in fhandle:
    line = line.split()
    if len(line) < 3 or line[0] != 'From':
        continue
    days[line[1]] = days.get(line[1], 0) + 1
for day in days.items():
    if largest_value is None or day[1] > largest_value:
        largest_day = day[0]
        largest_value = day[1]
print(days)
print(largest_day, largest_value)
