num = int(input("Digite un número superior a 0: "))
cnt = 1

while cnt != num+1:
    if num % cnt == 0:
        print(f"{cnt} es divisor de {num}")
    elif num == 0:
        print("El número debe ser superior que 0...")
    cnt += 1

