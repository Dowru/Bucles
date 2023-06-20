num = int(input("Digite un número: "))

if num > 10:
    acm = 1
    for i in range(1, 11):
        acm *= i
    print(f"El resultado de la multiplicación de los primeros 10 numeros de {num} es: {acm}")
else:
    acm = 0
    for s in range(0, num):
        acm += s
    print(f"Su resultado es: {acm}")       
