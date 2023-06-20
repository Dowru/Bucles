num = int(input("Digite un número: "))
sum = 0
par = 0
cnt = 0

while cnt <= num:
    if cnt % 2 == 0:
        sum += cnt
        par += 1
    cnt += 1

print(f"Los numeros pares dentro del número {num} son: {par}")
print(f"La suma de los numeros pares dentro del numero {num} es: {sum}")