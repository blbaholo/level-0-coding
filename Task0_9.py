def split(word):
    return list(word)
split("Umuzi")

List_of_letters=[]

def vowels(word):

    for i in word:
        if (i=="u" or i=="U"):
            List_of_letters.append("u")
            break
    for i in word:
        if (i=="o" or i=="O"):
            List_of_letters.append("o")
            break
    for i in word:
        if (i=="i" or i=="I"):
            List_of_letters.append("i")
            break
    for i in word:
        if (i=="e" or i=="E"):
            List_of_letters.append("e")
            break
    for i in word:
        if (i=="a" or i=="A"):
            List_of_letters.append("a")
            break
    print(','.join(List_of_letters))

vowels("Umuzi")



