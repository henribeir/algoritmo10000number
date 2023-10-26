import random
numeros=[]
for i in range(10000):
    numero = random.randint(0,10000)
    if(not numero in numeros):
        numeros.append(numero)
        
#BUBBLE SORT
def bubble_sort(numeros):
    n = len(numeros)
    for i in range(n-1):
        for j in range(n-i-1):
            if numeros[j] > numeros[j+1]:
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
    return numeros

#INSERTION SORT
def insertion_sort(numeros):
    n = len(numeros)
    for i in range(1, n):
        chave = numeros[i]
        j = i - 1
        while j >= 0 and numeros[j] > chave:
            numeros[j + 1] = numeros[j]
            j -= 1
        numeros[j + 1] = chave
    return numeros

#QUICK SORT
def quick_sort(numeros):
    if len(numeros) <= 1:
        return numeros
    else:
        pivo = numeros[0]
        menores = [x for x in numeros[1:] if x <= pivo]
        maiores = [x for x in numeros[1:] if x > pivo]
        return quick_sort(menores) + [pivo] + quick_sort(maiores)
    
print(quick_sort(numeros))