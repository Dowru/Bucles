end = 0
ttl = 0

while not end:
    fct = float(input("Digite el valor de su factura: "))
    ttl += fct
    if fct == end:
        if ttl > 1000:
            dsc = ttl * .10
            nTotal = ttl - dsc
            print(f"Su total a pagar será de {nTotal}")
            break
        else:
            print(f"Su total a pagar será de {ttl}")
            break 
