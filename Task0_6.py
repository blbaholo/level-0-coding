def maximum(a,b,c):

    if (a>b and a>c):
        max_num=a
    if (b>a and b>c):
        max_num=b
    if (c>a and c>b):
        max_num=c
    return max_num

print(maximum(1,2,3))
