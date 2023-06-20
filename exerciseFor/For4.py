num = int(input("Digite un número: "))
acm = 0

for i in range(0, num + 1, 2):
    acm += i

print(f"El resultado de la suma de los numeros pares de {num} es {acm}")
