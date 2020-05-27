import math

print("Input variabel untuk rumus = ax^2+bx=c=0")
a = int(input("Input a : "))
b = int(input("Input b : "))
c = int(input("Input c : "))
if a!=0:
    print("Persamaan kuadrat : ",a,"x^2+",b,"x+",c,"=0")
    diskriminan = float((b**2)-(4*a*c))
    if diskriminan < 0:
        print("Persamaan tidak memiliki akar-akar yang real")
    elif diskriminan == 0:
        x = (-b+math.sqrt(diskriminan))/(2*a)
        print("Akarnya adalah ",x)
    elif diskriminan > 0:
        x1 = (-b+math.sqrt(diskriminan))/(2*a)
        x2 = (-b-math.sqrt(diskriminan))/(2*a)
        print("Akar-akarnya adalah : ")
        print("x1 : ",x1)
        print("x2 : ",x2)
elif a==0:
    print("Persamaan kuadrat : ",b,"x+",c,"=0")
    x = -c/b
    print(x)
