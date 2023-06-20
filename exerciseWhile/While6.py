end = 0
notes = []
sum = 0

while not end:
    note = float(input("Ingrese la nota del estudiante aquí: "))
    exit = input("Desea sacar el promedio ahora? ingrese \"si\" para sacar el promedio: ")
    notes.append(note)
    sum += note
    if exit.lower() == "si":
        prm = sum / len(notes)
        print(f"El promedio de las notas es de {prm}")
        break
