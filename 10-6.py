# Prints ten most common words in a file.
import string

filename = input('File: ')
try:
    fhandle = open(filename)
except FileNotFoundError:
    raise SystemExit

wordmap = dict()
for line in fhandle:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        wordmap[word] = wordmap.get(word, 0) + 1

# print(wordmap)
top = list()
for word, count in wordmap.items():
    top.append((count, word))
top.sort(reverse=True)
for count, word in top[:10]:
    print(count, word)
