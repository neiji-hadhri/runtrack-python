def resultnotes(notes):
    arrondi=[]
    for i in notes:
        if 40.00 <= i <= 100.00:
            i+(5-i%5)
            print(i,"Bravo!!!!!!!!!!!!!")
            if i+1%5==0:
                i=i+1
                arrondi=[i]
            elif i+2%5==0:
                i=i+2
        else:
            print("bof")
    
notes= [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
resultnotes(notes)
