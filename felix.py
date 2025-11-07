print("hoi allemaal")
a = 15

a = "maandag"

print(a)
b = input("noem je voornaam: ")
print("je voornaam is: " +b)
if b == "joost":
    print("je bent niet welkom")
    print("go")
leeftijd = input("wat is je leeftijd")
leeftijd = int(leeftijd)
print(leeftijd + 25)
print("over 25 jaar badsfasdfen je dus ", leeftijd)
def ditendat():
    print("doe dit en dat")

ditendat()
ditendat()
ditendat()
ditendat()
ditendat()
ditendat()
ditendat()
ditendat()
ditendat()
# functie procedure methode
def tweedefunctie(param, tweedparam = "donderdag"):  # parameter
    print("print dit maar", param)
    print("print dit maar", tweedparam)
    return "vrijdag" # returntype  / hetgeen dat gereturned wordt

# een aanroep van een methode mag je evalueren tot datgene dat hij returned

uitkomst = tweedefunctie(34, 44) # argument
print(tweedefunctie(42)) # vrijdag

print(uitkomst)

def geefzes():
    return 6

print(geefzes() + geefzes())