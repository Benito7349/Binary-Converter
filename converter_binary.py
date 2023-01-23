#Este programa permite convertir número decimales a números binarios.

numero_decimal = int(input("Ingrese el número decimal que desea conventir a binario: "))

residuo = 1
binario = []

if numero_decimal % 2 == 0:
    binario.append(0)
else:
    binario.append(1)
    
while residuo >= 1:
    residuo = numero_decimal // 2
    if residuo % 2 == 0:
        binario.append(0)
    else:
        binario.append(1)
    numero_decimal = residuo
binario.pop()
binario.reverse()

print("El número es binario es:")
for i in binario:
    print(i, end="")