end = 0
sum = 0

while not end:
    num = int(input("Ingrese todos los numeros enteros del teclado: "))
    sum += num
    if num == end:
        print(f"La suma de los numeros del teclado ingresados es {sum}")
        break
