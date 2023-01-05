def compteur() :
    i=0
    while i < 100:
        i+=1

for n in range(1000):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)


compteur()



