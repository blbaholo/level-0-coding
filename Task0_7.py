def celsius_to_fahrenheit(celsius):
    fahrenheit=int((celsius*1.8)+32)
    return fahrenheit
print(celsius_to_fahrenheit(24))

def fahrenheit_to_celsius(fahrenheit):
    celsius=int((fahrenheit-32)*(5/9))
    return celsius
print(fahrenheit_to_celsius(50))
