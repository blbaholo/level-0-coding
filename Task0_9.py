word="Umuzi"

def split(word):
    return list(word)
split(word)

List_of_vowels=[]

def vowels():

    for i in word:
        if (i=="u" or i=="U"):
            List_of_vowels.append("u")
            break
    for i in word:
        if (i=="o" or i=="O"):
            List_of_vowels.append("o")
            break
    for i in word:
        if (i=="i" or i=="I"):
            List_of_vowels.append("i")
            break
    for i in word:
        if (i=="e" or i=="E"):
            List_of_vowels.append("e")
            break
    for i in word:
        if (i=="a" or i=="A"):
            List_of_vowels.append("a")
            break
    print(List_of_vowels)

vowels()



