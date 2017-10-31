def computepay(hours, rate):
    if hours <= 40:
        pay = (rate) * (hours)
    else:
        print('\n1.5x rate after 40 hours')
        pay = (rate) * 40 + (rate * 1.5) * (hours - 40)
    return pay

try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    print('Pay: ' + str(round(computepay(hours, rate), 2)))
except:
    print('Error: enter only numbers')
