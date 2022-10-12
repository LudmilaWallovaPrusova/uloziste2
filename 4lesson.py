# Vytvoř třídu Balik, která bude mít tři atributy - adresa, hmotnost a doruceno. První dva atributy nastav pomocí 
# parametrů funkce __init__. Parametr doruceno nastav na začátku jako False.
# Připoj ke třídě funkci doruc, která změní hodnotu parametru doruceno na True.
# Přidej metodu __str__, která vypíše adresu, hmotnost a informaci o tom, zda byl balík již doručen.
# Zkus si vytvořit nějaké objekty ze třídy Balik a ověř, že vše funguje.

# class Balik:
#     def __init__(self, adresa, hmotnost, doruceno = False):
#         self.adresa = adresa
#         self.hmotnost = hmotnost
#         self.doruceno = doruceno
    
#     def doruc (self):
#         self.doruceno = True
    
#     def __str__(self):
#         return (
#             f"Balik na adresu {self.adresa}, hmotnost {self.hmotnost}"
#             f' - {"doručen" if self.doruceno else "nedoručen"}'
#         )

       
# balik1 = Balik("Liliová 16", "450g")
# balik2 = Balik("Růžová 17", "1200g")
# balik3 = Balik("Okurková 18", "900g")

# print(balik3)
# balik2.doruc()
# print(balik2)


# Zkus pro našeho nakladatele vytvořit software s využitím tříd a objektů. 
# Vytvoř tedy třídu Kniha, která reprezentuje knihu. 
# každá kniha bude mít atributy nazev, pocet_stran a cena. Hodnoty nastav ve funkci __init__.
# Přidej knize funkci __str__, která vypíše informace o knize v nějakém pěkném formátu.
# Občas se stane, že se kniha moc neprodává a knihkupec se snaží nalákat kupující slevou. 
# Přidej metodu sleva(), která bude mít jeden parametr - velikost slevy v procentech. Funkce sníží cenu knihy o dané procento.

# class Kniha:
#     def __init__(self, nazev, stran, cena):
#         self.nazev = nazev
#         self.stran = stran
#         self.cena = cena
    
#     def sleva (self, procento):
#         self.cena -= self.cena * procento * 0.01

#     def __str__(self):
#         return (f"Svazek {self.nazev} má {self.stran} stran a stojí po slevě {self.cena} Kč.")

# kniha1 = Kniha("Kája Mařík", 450, 280)
# kniha2 = Kniha("Rumcajs", 1200, 300 )

# kniha1.sleva(20)
# print(str(kniha1))


# U zaměstnanců budeme nově evidovat, jestli jsou ve zkušební době.
# Rozšiř metodu __init__ třídy Zamestnanec o parametr zkusebni_doba, který bude typu bool. 
# Tuto hodnotu ulož jako atribut třídy Zamestnanec.
# Uprav metodu __str__. Pokud je zaměstnanec ve zkušební době, přidej k jeho/jejímu výpisu text Je ve zkušební době.

class Zamestnanec:
    def __init__(self, jmeno, pozice, zkusebka):
        self.jmeno = jmeno
        self.pozice = pozice
        self.zkusebka = zkusebka
    
    def __str__(self):
        hlaska = f"Zaměstnanec {self.jmeno}, který pracuje na pozici {self.pozice}, "
        if self.zkusebka:
            return hlaska + ' ve zkušební době je.'
        return hlaska + ' ve zkušební době není.'

lojza = Zamestnanec("Alois Nový", "recepční", False)
print(lojza)