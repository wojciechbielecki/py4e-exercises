def computegrade(score):
    if score > 1:
        grade = 'Bad score'
    elif score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    elif score >= 0:
        grade = 'F'
    else:
        grade = 'Bad score'
    return grade

try:
    score = input('Enter score: ')
    score = float(score)
    print(computegrade(score))
except:
    print('Bad score')
