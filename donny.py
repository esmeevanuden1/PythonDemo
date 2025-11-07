print("hallo allemaal")

a = 15

a = "maandag"

print(a)

b = input("noem je voornaam: ")
print("je voornaam is: " + b)

if b == "joost":
    print("je bent niet welkom")
    print("go")
leeftijd = input("wat is je leeftijd?: ")
leeftijd = int(leeftijd)
print(leeftijd + 25)
print("over 25 jaar ben je dus:", leeftijd)

def ditendat():
    print("doe dit en dat")

ditendat()
ditendat()
ditendat()
ditendat()

def tweedefunctie(param): #parameter
    print("print dit maar", param)

tweedefunctie(34)
tweedefunctie(42)