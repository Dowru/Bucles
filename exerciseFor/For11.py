numT = int(input("Ingrese el número de temperaturas que desea ingresar: "))
tem = []
prom = 0

for i in range(1, numT + 1):
    print(f"Ingrese la {i} temperatura:", end=" ")
    temp = float(input())
    tem.append(temp)
    prom += temp
    
mayor = max(tem)
menor = min(tem)
pme = prom / len(tem)

print(f"La temperatura promedio es {pme}")
print(f"La temperatura mayor es: {mayor}")
print(f"La temperatura menor es: {menor}")




