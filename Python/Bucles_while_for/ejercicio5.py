cant=int(input("Introduce la cantidad a invertir: "))
inter=int(input("Introduce el interes anual: "))
año=int(input("¿Cuantos años? "))
i=0

inter=inter/100
inter_tot=cant*inter
cant=cant+inter_tot
while i<=año:
    print("Has generado por año:",cant)
    i=i+1
