print("Julian hier!")

naam = input("Wat is jouw naam? ")
if naam == "Julian":
    print("Hoi, mede-Julian!")
elif naam in ["Abel", "Bente", "Donny", "Esmee", "Felix"]:
    print(naam + ", jou ken ik al!")
else:
    print("Hallo, " + naam + "! Jou ken ik nog niet.")

def ditendat():
    print("Dit en dat")

ditendat()

def tweede_functie(iets):
    print("Je gaf me dit mee: " + iets)

tweede_functie("Hallo daar!")
tweede_functie(naam)
tweede_functie(str(1234))