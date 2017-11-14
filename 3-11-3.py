# 3.11.3
score = input('Enter score: ')
e = 'Bad score'
try:
    score = float(score)
except ValueError:
    print(e)

if type(score) != float:
    pass
elif score > 1:
    print(e)
elif score >= 0.9:
    print('A')
elif score >= 0.8:
    print('B')
elif score >= 0.7:
    print('C')
elif score >= 0.6:
    print('D')
elif score >= 0:
    print('F')
else:
    print(e)
