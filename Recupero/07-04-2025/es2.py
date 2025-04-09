import os
os.system("cls")

    #Sezione dichiarativa
try:
    base = int(input(">> Inserisci la base dell'albero compresa tra 3 e 20:  "))

except:
    print("Errore")
    #Sezione di richiesta

while base < 3 or base > 20 or base % 2 == 0:
    print(">> Errore: valoren non consentito. Inserisci un numero dispari compreso tra 3 e 20!")
    base = int(input(">> Inserisci la base dell'albero compresa tra 3 e 20: "))

#Sezione di creazione della chioma

for i in range(1, base + 1, 2):
    for A in range((base - i) // 2):
        print(" ", end="")
    for B in range(i):
        print("*", end="")
    print()

#Sezione di creazione del tronco

if base == 3:
    print(" *")
if base == 5:
    print("  *")
if base == 7:
    print("   *")
if base == 9:
    print("    *")
if base == 11:
    print("     *")
if base == 13:
    print("      *")
if base == 15:
    print("       *")
if base == 17:
    print("        *")
if base == 19:
    print("         *")



