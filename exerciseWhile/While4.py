num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
cnt = num1 - 1
num = 0

if num1 < num2:
    print(f"Los numeros van desde {num1} hasta {num2} son:")
    while cnt != num2:
        num += cnt
        cnt += 1
        print(cnt)
else:
    print("El primer número debe ser menor al segundo")
