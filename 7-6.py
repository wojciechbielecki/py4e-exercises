fname = input('Filename: ')
try:
    fhandle = open(fname)
except:
    print('File cannot be opened:', fname)
    raise SystemExit
count = 0
for line in fhandle:
    if line.startswith('Subject:'):
        # line_subject = line.lstrip('Subject:').strip()
        # print(line_subject)
        count = count + 1
print('There are', count, 'subject lines in', fname)
