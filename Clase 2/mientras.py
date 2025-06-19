a = 0

while a < 10:
    a += 1
    if a == 7:
        break
    if a%2==0:
        continue
    print(a)
else:
    print("Fin del ciclo")    