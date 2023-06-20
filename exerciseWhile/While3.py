num = int(input("Ingrese un número: "))
cnt = 0
sum = 0

print(f"Los numeros impares que hay desde 1 hasta {num} son:")
while cnt != num+1:
    if cnt % 2 != 0:
        sum += cnt 
        print(cnt)
    cnt += 1
print(f"La suma de los numeros impares que hay desde 1 hasta {num} es: {sum}")