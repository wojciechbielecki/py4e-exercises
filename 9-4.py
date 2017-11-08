import string

fname = input('File: ')
try:
    fhandle = open(fname)
except:
    raise SystemExit

wordmap = dict()
for line in fhandle:
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        wordmap[word] = wordmap.get(word, 0) + 1

print(wordmap)
