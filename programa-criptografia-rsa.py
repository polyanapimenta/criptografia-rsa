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

def paresPrimosEntreSi(totN, e):
    p1 = totN
    p2 = e
    p3 = 1
    #i = 0

    while p3 != 0:
        p3 = p1 % p2
        #p4 = p1 / p2
        #print('i:', i, 'P1:', p1, 'P2:', p2, 'P3:', p3)
        #print('Divisão:', p4)
        mdc = p2
        p1 = p2
        p2 = p3
        #i += 1

    return mdc

# Etapa 1 - Escolher p e q (números primos) e calcula N=p.q

p = calcularPrimo(10) #parâmetro é qtd. de bits para o núm. randomizado
q = calcularPrimo(10)
n = p * q

print('p:',p)
print('q:',q)
print('N:',n)

# Etapa 2 - Calcular a função totiente ϕ(N) = (p-1).(q-1)

totN = (p-1) * (q-1)
print('ϕ(N):', totN)

# Etapa 3 – Escolha 1 < e < ϕ(N), talque e e ϕ(N) sejam primos entre si

e = secrets.randbelow(totN)
mdc = paresPrimosEntreSi(totN, e)

while mdc != 1:
    e = secrets.randbelow(totN)
    mdc = paresPrimosEntreSi(totN, e)

print('e:',e)
print('MDC:', mdc)

#Etapa 4 – Escolha d talque e.d mod ϕ(N) =1

'''
Explicação função paresPrimosEntreSi():
Dois ou mais números são primos entre si quando o máximo divisor comum (MDC) desses números é 1.)

Nesse processo efetuamos várias divisões até chegar a uma divisão exata.
#1º) dividimos o número maior (p1) pelo número menor(p2);
#2º) dividimos o divisor (p2), que é divisor da divisão anterior, por (p3), que é o resto da divisão anterior, e assim sucessivamente;
#3º) O divisor da divisão exata é (p2). Então m.d.c. entre(p1,p2) = p2 (p3 resto da divisão anterior) 

p1       p2            p3
totN   / e      = bla (resto)
p2       p3            p3
e      / resto  = bla (resto1)
p3       p3            p3
resto  / resto1 = bla (resto2)
...
resto1 / resto2 = bla (resto3)
...
resto2 / resto3 = bla ...
'''