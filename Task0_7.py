
def celsius_to_fahrenheit(C):
    F=int((C*1.8)+32)        #C=degrees celsius,F=degrees Fahrenheit
    return F
print(celsius_to_fahrenheit(24))

def fahrenheit_to_celsius(F):
    C=int((F-32)*(5/9))
    return C
print(fahrenheit_to_celsius(50))
