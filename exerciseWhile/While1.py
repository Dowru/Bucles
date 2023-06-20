num = int(input("Digite un número: "))
cnt = 0

if num > 10:
    acm = 1
    while cnt != 10:
        cnt += 1
        acm *= cnt
    print(f"El resultado es: {acm}")

else:
    acm = 0
    while cnt < num:
        cnt += 1
        acm += cnt
    print(f"El resultado es: {acm}")


