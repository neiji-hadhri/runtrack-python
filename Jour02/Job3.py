def compteur() :
    i=0
    while i < 100:
        i+=1
        if i in (26,37,88):
            continue
        print(i)
    

compteur()
