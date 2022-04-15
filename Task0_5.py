from math import sqrt

def area_of_a_triangle(a,b,c):

    s=(a+b+c)/2                #s=semiperimeter
    area=sqrt(s*(s-a)*(s-b)*(s-c))
    return area

print(area_of_a_triangle(3,4,5))
