temps = []
prm = 0
end = 0

while not end:
    nTemp = float(input("Ingrese aqui la temperatura: "))
    temps.append(nTemp)
    prm += nTemp
    
    if nTemp == end:
        temps.pop()

        mayor = max(temps)
        menor = min(temps)
        prm /= len(temps)

        print(f"El promedio de las temperaturas es {prm}")
        print(f"La temperatura mayor es {mayor}")
        print(f"La temperatura menor es {menor}")

        break

