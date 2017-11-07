fhand = open('mbox-short.txt')
for line in fhand:
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])
