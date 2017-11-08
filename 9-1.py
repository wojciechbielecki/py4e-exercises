word = input('Word: ')
counter = dict()
for letter in word:
    letter = letter.lower()
    counter[letter] = counter.get(letter, 0) + 1
print(sorted(counter.items()))
