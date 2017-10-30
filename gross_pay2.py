try:
    hours = float(input('Enter Hours: '))
    try:
        rate = float(input('Enter Rate: '))
        if hours <= 40:
            pay = (rate) * (hours)
            print('Pay: ' + str(round(pay,2)))
        else:
            print('\n1.5x rate after 40 hours')
            pay = (rate) * 40 + (rate * 1.5) * (hours - 40)
            print('Pay: ' + str(round(pay,2)))
    except:
        print('Error: enter only numbers')
except:
    print('Error: enter only numbers')
