import secrets
import math
import string

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

def modInverse(a,n):
  i=1
  while True:
    c = n * i + 1;
    if(c%a==0):
      c = c/a
      break;
    i = i+1

  return c

def chavePublica(e, n, p):
    c = (p ** e) % n
    return c

def chavePrivada(c, d, n):
    P = (c ** d) % n
    return P

def abc(letra):
    i = 1
    l = letra
    # print(l)

    while i <= 26:
        a = list(string.ascii_lowercase[:i])
        # print(a[i - 1] + ' =', i)

        if l == a[i - 1]:
            return i
        elif l == ' ':
            return 27
        elif l == 'T':
            return 28
        i += 1

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

d = round(modInverse(e, totN))
print('d:', d)

result = 0
if result != 1:
    result = (e * d) % totN
#print('result:', result)

#Criptografar - Chave Pública
print('------------ Criptografando frase ------------\n')
j = 0
msg = 'The information security is of great importance to ensure the privacy of communications'

while j <= msg.__len__():
    b = list(msg)
    P = abc(b[j])
    criptografado = chavePublica(e, n, P)
    print(P, '\t-> ', b[j],' -> ', criptografado)
    j += 1

print('------------ Decriptografando frase ------------')
print('criptografado', criptografado)

#Decriptografar - Chave Privada
decriptografar = chavePrivada(criptografado, d, n)
print ('decriptografado:', decriptografar)

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