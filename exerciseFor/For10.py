num = int(input("Ingrese un número superior a 0: "))

if num > 0:
    for i in range(1,num + 1): 
        if num % i == 0:
            print(f"{i} es divisor de {num}")
else:
    print("El número debe ser superior a 0...")