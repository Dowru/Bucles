num1 = int(input("Digite un número: "))
num2 = int(input("Digite un número superior al número anterior: "))

if num1 < num2:
    print(f"Los numeros que van desde {num1} hasta {num2} son:")
    for i in range(num1, num2 + 1):
        print(i)
else:
    print("El segundo número debe superior al primero")
