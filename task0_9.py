def vowels(word):
    word.split(word)
    list_of_letters=[]
    for i in word:
        if (i=="u" or i=="U"):
            list_of_letters.append("u")
            break
    for i in word:
        if (i=="o" or i=="O"):
            list_of_letters.append("o")
            break
    for i in word:
        if (i=="i" or i=="I"):
            list_of_letters.append("i")
            break
    for i in word:
        if (i=="e" or i=="E"):
            list_of_letters.append("e")
            break
    for i in word:
        if (i=="a" or i=="A"):
            list_of_letters.append("a")
            break
    print("Vowels: " + ', '.join(list_of_letters))

vowels("Umuzi")
