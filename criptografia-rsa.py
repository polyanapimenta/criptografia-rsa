from random import randint

primo = False

while not primo:
    p = (randint(1, 1000))
    if(p > 1):
        div = 0
        for i in range(p):
            if(i>=1) and (p % i == 0):
                div += 1

        if(p % 2 != 0) and (div <= 1):
            primo = True
            print('primo: ',p)







