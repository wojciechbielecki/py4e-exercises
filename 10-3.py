text = input()
words = text.split()
t = list()
for word in words:
    t.append((len(word), word))
t.sort(reverse=True)
print(t)
result = list()
for length, word in t:
    result.append(word)
print(result)
