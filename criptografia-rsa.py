from random import randint

primo = False
print('Buscando um primo..')

while not primo:
    p = (randint(10000000000000, 99999999999999))
    print('random:', p)
    div = 1

    for i in range(p):
        if(i >= 1) and (p % i == 0):
            div += 1

        if (div == 3):
            break

    print('\ndivisores:',div )

    if(p % 2 != 0) and (div <= 2):
        primo = True
        print('Primo: ',p)