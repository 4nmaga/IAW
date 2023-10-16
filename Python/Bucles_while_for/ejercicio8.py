
r=input("Introduce una frase: ")
letra=input("Introduce la letra que quieres buscar en la frase: ")
i=0
a=0
for i in r:
    
    if letra==i:
        a=a+1

print("Hay",str(a),"veces en la frase")
   
   