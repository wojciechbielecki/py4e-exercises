fhand = open('mbox-short.txt')
for line in fhand:
    # if line.startswith('From:'):
    #     print(line.rstrip())
    # if not line.startswith('From:'):
    #     continue
    if line.find('@uct.ac.za') == -1: continue
    print(line.rstrip())
