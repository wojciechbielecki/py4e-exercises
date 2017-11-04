def count_letter(word, letter):
    count = 0
    for char in word:
        if char == letter:
            count = count + 1
    return count

while True:
    inword = input('Word: ')
    inletter = input('Letter: ')
    if len(inletter) == 1:
        break
print(count_letter(inword, inletter))
