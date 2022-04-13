a="houses"
b="computers"

def split(a):
    return list(a)
split(a)

def split(b):
    return list(b)
split(b)

List_of_common_letters=[]
def common_letters(a,b):

    for i in b:
        if (i in a):
            List_of_common_letters.append(i)
    print(List_of_common_letters)

common_letters(a,b)

