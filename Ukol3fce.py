cislo = input("Zadejte telefonní číslo BEZ MEZER: ")

def testovani (cislo):
    delka = len(cislo)
    znak = 0 
    for _ in range(delka): 
        hodnota_znaku = cislo[(znak)]
        # print(f'Hodnota znaku je {hodnota_znaku}.')
        
        if cislo[(znak)] in "0123456789": 
            if znak + 1 < delka:     
                znak += 1
                upravene = cislo
        else:
            if cislo.replace(cislo[(znak)], "") == "":       
                upravene = "bez číslic"   
                delka = 0
                # znak -= 1
            
            else:
                upravene = cislo.replace(cislo[(znak)], "")
                # print(f'Císlo po vyloučení literek je {upravene}')
                cislo = upravene
                delka = len(cislo)
                # print(delka)
                if znak + 1 >= delka :     
                    znak -= 1                
    return upravene

adapted = testovani(cislo)
print(f'Zadané číslo je {adapted}.')

def spravnost(adapted):
    if len(adapted) != 9 and len(adapted) != 12:
        print(f'Číslo neobsahuje odpovídající počet číslic. Zkus to znovu')
        vracej = False
    else:
        print(f'Číslo má správný formát.')
        vracej = True
    return vracej
accuracy = spravnost(adapted)    

if accuracy == True:
    zprava = input("Zadejte zprávu: ") 

    def sms (zprava):
        delka_sms = len(zprava)
        print(f'Délka zprávy je {delka_sms}.')
        pocet_sms = (delka_sms//20) 
        if delka_sms % 20 != 0:
            pocet_sms +=1
        cena = pocet_sms * 3
        return cena

    price = sms(zprava)
    print(f'Cena zprávy je {price}.')

