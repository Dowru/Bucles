notes = []
prm = 0
acm = 0

while acm != 3:
    note = float(input("Ingrese aqui la nota: "))
    notes.append(note)
    prm += note
    acm += 1
    
    if acm == 3:

        mayor = max(notes)
        menor = min(notes)
        prm /= len(notes)

        print(f"El promedio de las notas es {prm}")
        print(f"La nota mayor es {mayor}")
        print(f"La nota menor es {menor}")
        break
