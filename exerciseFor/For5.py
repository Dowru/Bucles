def odd():
    n = int(input("Digite un numero: "))
    cnt = 0
    sum = 0

    for i in range(0, n + 1):
        if i % 2 != 0:
            sum += i
            cnt += 1
    
    print(f"La suma de todos los numeros impares que hay desde 0 hasta {n} es: {sum}")
    print(f"Los numeros impares que hay desde 0 hasta {n} son: {cnt}")

odd()