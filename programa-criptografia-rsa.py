import secrets
import math

def calcularPrimo(bits):
    primo = False
    while not primo:
        p = secrets.randbits(bits)
        div = 1

        while (p % 2 == 0) or (p % 3 == 0) or (p % 5 == 0) or (p % 7 == 0):
            p = secrets.randbits(bits)

        r = math.trunc(p/8)

        for i in range(p):
            if (i >= 1) and (p % i == 0):
                div += 1

            if (div == 3) or (i >= r):
                break

        #print('Random:', p, ', Divisores:', div)

        if (p is not None) and (div <= 2):
            return (p)

# Etapa 1 - Escolher p e q (números primos) e calcula N=p.q

p = calcularPrimo(30) #parâmetro é qtd. de bits para o núm. randomizado
q = calcularPrimo(30)
n = p * q

print('P:',p)
print('Q:',q)
print('N:',n)

# Etapa 2 - Calcular a função totiente (N) = (p-1).(q-1)
