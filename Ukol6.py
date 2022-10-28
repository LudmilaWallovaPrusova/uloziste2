with open('seniori.txt', encoding='utf-8') as vstup:
    radky = vstup.readlines()
print(radky)

radky = [radek.split('\t') for radek in radky]
print(radky)

tab = []
line = []

for radek in radky: 
    for sloupec in range(0,2):
        line.append(str(radek[sloupec]) + '\t')
    for sloupec in range(2,8):
        if  radek[sloupec] == '1':
            line.append('A\t')
        elif radek[sloupec] == '2':
            line.append('B\t')
        elif radek[sloupec] == '3':
            line.append('C\t')
        elif radek[sloupec] == '4':
            line.append('D\t')
        elif radek[sloupec] == '5':
            line.append('F\t')
        elif radek[sloupec] == '1\n':
            line.append('A\n')
        elif radek[sloupec] == '2\n':
            line.append('B\n')
        elif radek[sloupec] == '3\n':
            line.append('C\n')
        elif radek[sloupec] == '4\n':
            line.append('D\n')
        elif radek[sloupec] == '5\n':
            line.append('F\n')
        else:
            line.append(radek[sloupec])
print(line)    

with open('seniori.txt', mode='w', encoding='utf-8') as vystup:
    vystup.writelines(line)

# ----------------------------------------------------

with open('seniori.txt', encoding='utf-8') as vstup:
    radky = vstup.readlines()
print(radky)

radku = len(radky)
tab = []

for radek in radky:
    if radek.startswith("Příjmení"):
        None
    else:
        radek = radek.replace("1","A")
        radek = radek.replace("2","B")
        radek = radek.replace("3","C")
        radek = radek.replace("4","D")
        radek = radek.replace("5","F")
    print(radek)
    tab.append(radek)
with open('seniori.txt', mode='w', encoding='utf-8') as vystup:
    vystup.writelines(tab)

    



