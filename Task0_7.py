C=24                         #C=degrees Celsius

def celsius_to_fahrenheit():
    F=int((C*1.8)+32)        #F=degrees Fahrenheit
    return F
print(celsius_to_fahrenheit())

F=50

def fahrenheit_to_celsius():
    C=int((F-32)*(5/9))
    return C
print(fahrenheit_to_celsius())
