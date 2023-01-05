L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
Maximum=L[0]
Minimum=L[0]
for i in L :
    if i > Maximum :
        Maximum=i
    if i < Minimum :
        Minimum=i
        
print("le chiffre minimum:",Minimum)
print("le chiffre maximum:",Maximum)