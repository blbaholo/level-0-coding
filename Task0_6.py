a=1
b=2
c=3

def max_number(a,b,c):

    if (a>b and a>c):
            max_number=a

    if (b>a and b>c):
            max_number=b

    if (c>a and c>b):
            max_number=c
    return max_number

print(max_number(a,b,c))
