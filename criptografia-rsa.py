from random import randint
### Etapa 1 - Escolher p e q aleatóriamente(números primos) e calcular N=p.q ###

# Verificando se p e q são números primos:
primo = False
count = 0
while (primo == False):
    print(count,':')
    # Gerando números aleatórios p e q em Python
    p = (randint(0, 1000))
    q = (randint(0, 1000))

    if(p > 1) and (p % 2 != 0) and (p % 3 != 0) and (p % 5 != 0) and (p % 7 != 0) or (p == 2) or (p == 3) or (p == 5) or (p == 7):
        # 1. um número natural é primo se ele é maior que 1
        # 2. números pares não são primos, apenas o 2
        # 3. números múltiplos de 3 não podem ser primos, exceto o 3
        # 4. números múltiplos de 5 não podem ser primos, exceto o 5
        # 5. números múltiplos de 7 não podem ser primos, exceto o 7
        print('p: ', p)
        primo = True
    count+=1