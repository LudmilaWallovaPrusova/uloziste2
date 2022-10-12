cislo = input("Zadejte telefonní číslo BEZ MEZER: ")

def spravnost(cislo):
    if (len(cislo) == 13 and cislo[0:5] !="+420"):
        print(f'Číslo má chybně předvolbu. Zkus to znovu')
        vracej = False

    elif len(cislo) != 9 and len(cislo) != 13:
        print(f'Číslo neobsahuje odpovídající počet znaků. Zkus to znovu')
        vracej = False
    else:
        print(f'Číslo má správný počet znaků.')
        vracej = True
    return vracej
accuracy = spravnost(cislo)  


if accuracy == True:
    zprava = input("Zadejte zprávu: ") 

    def sms (zprava):
        delka_sms = len(zprava)
        print(f'Délka zprávy je {delka_sms}.')
        pocet_sms = (delka_sms//180) 
        if delka_sms % 180 != 0:
            pocet_sms +=1
        cena = pocet_sms * 3
        return cena

    price = sms(zprava)
    print(f'Cena zprávy je {price}.')


