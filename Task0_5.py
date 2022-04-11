from math import sqrt

#a,b,c represent triangle sides
a=int(input())
b=int(input())
c=int(input())

def area_of_a_triangle(a,b,c):

    s=(a+b+c)/2                #s=semiperimeter
    area=sqrt(s*(s-a)*(s-b)*(s-c))
    return area

print(area_of_a_triangle(a,b,c))
