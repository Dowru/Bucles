n = int(input("Digite el número de notas al que le quiere sacar promedio: "))
acm = 0

for i in range(1, n + 1):
    print(f"Digite la {i} nota:", end=" ")
    note = int(input())
    acm += note
    prom = acm / n 

print(f"El promedio de las notas es {prom}")

