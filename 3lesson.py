# cviceni 1
# def mult (a,b):
#     return a * b
# print(mult(5,8))


# cviceni 3
# def month_of_birth (rc):
#     mm = int(rc[2:4])
#     if mm > 12:
#         mm -= 50
#     print(f'Měsíc narození je {mm}')
# print(month_of_birth('7111054456'))

# cviceni 4
from random import randint, random

srajtofle = 5000

def roulette (rada, sazka):
    nahoda = randint(0,36)
    print(nahoda)
    if nahoda == 0:
        (print(f('Prohráváš, padla {nahoda}')))
        c_rady = 9
    elif nahoda % 3 == 0:
        c_rady = 3
    elif nahoda % 3 == 2:
        c_rady = 2
    elif (nahoda % 3) == 1:
        c_rady = 1
    print(c_rady)

    if c_rady == rada:
        vyhra = sazka * 2
        print(f'trefils, vyhráváš {vyhra} Kč')
    elif c_rady != rada:
        vyhra = -sazka
        print(f'netrefil, netrefil, rozluč se se {sazka} Kč')
    
    return srajtofle + vyhra
    
print(roulette(2,100))



