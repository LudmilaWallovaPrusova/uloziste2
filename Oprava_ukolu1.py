baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}


kodbaliku = input("Zadejte číslo balíku: ")
if kodbaliku in baliky:
    if baliky[kodbaliku] == True:
            print("Balík už byl předán kurýrovi")
    elif baliky[kodbaliku] == False:
            print("Balík zatím nebyl předán kurýrovi")
else:
            print("Balík neevidován")

