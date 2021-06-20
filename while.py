numeros = [54, 58+5, 45, 12, 57, 84, 64, 25]

i = 0
menor = 0
while i < len(numeros):
    if menor > numeros[i]:
        menor = numeros[i]
    i+=1
print(menor)