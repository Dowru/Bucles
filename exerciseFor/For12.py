acm = 0
cnt = 0

for i in range(1,4+1):
    print(f"Ingrese la {i} nota:", end=" ")
    note = float(input())
    acm += note

    if cnt == 0:
        mayor = note
        menor = note
    else:
        if note > mayor:
            mayor = note
        elif note < menor:
            menor = note

    cnt += 1
    prom = acm / cnt

print(f"El promedio de las notas es {prom}")
print(f"La nota mayor es {mayor}")
print(f"La nota menor es {menor}")


