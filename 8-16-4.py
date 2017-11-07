fname = input('File: ')
try:
    fhandle = open(fname)
except:
    raise SystemExit
all_words = list()
for line in fhandle:
    line_words = line.split()
    for word in line_words:
        if word in all_words: continue
        all_words.append(word)
# all_words.sort()
all_words.sort(key=str.lower)
print(all_words)
