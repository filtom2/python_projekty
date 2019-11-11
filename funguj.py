from math import sqrt

print("Vitaj v programe na výpočet kvadratickej rovnice.")


a = int(input("Vložte koeficient a: "))
b = int(input("Vložte koeficient b: "))
c = int(input("Vložte koeficient c: "))

d = b**2-4*a*c


print("Tvoja rovnica vyzerá",a,"x2 +",b,"x + ",c," = 0")


if d < 0:
    print("Funkcia nemá riešenie..")

elif 0 < d:
    x1 = (-b+sqrt(d))/2*a
    x2 = (-b-sqrt(d))/2*a
    print("Riešenie x1 je ",x1,"a riešenie x2 je",x2,".")

else:
    x3 = -b/2*a
    print("x1 = x2 čiže riešenie je: ",x3,".")
    