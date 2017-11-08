fhandle = open('words.txt')
wordmap = dict()
for line in fhandle:
    words = line.split()
    for word in words:
        wordmap[word] = 'foo'

while True:
    check = input('|> ')
    if check == 'done': break
    if check in wordmap:
        print(' <--OK--> ')
