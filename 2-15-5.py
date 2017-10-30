celsius = input('Temperature in Celsius: ')
try:
    fahrenheit = float(celsius) * (9/5) + 32
    print(celsius + '°C is equal to ' + str(fahrenheit) + '°F')
except:
    pass
