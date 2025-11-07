import random 
import pandas


print("hoi")
vara = 25

if vara > 30:
    print("hoger")
else:
    print("lager")
    # initiator
                 # evaluator
                         # incrementor
# for(var x = 5; x < 10; x += 2){
#     print(x)
# }
for x in range(5, 10, 2):
    print(x)

lijst = [13,55,"vrijdag",["een", "twee"]]

print(lijst[3][0])

nummers = [35,2,77,34,2,9]

print(nummers.count(2))


print(random.randint(4,8))

pandas.read_csv("bestand.csv")