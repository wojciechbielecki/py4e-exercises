fname = input('File: ')
try:
    fhandle = open(fname)
except FileNotFoundError:
    raise SystemExit

wordmap = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        wordmap[word] = wordmap.get(word, 0) + 1

print(wordmap)
