import os
os.system("cls")

#Sezione dichiarativa

try:
    base = int(input(">> Inserisci un numero dispari.  "))
except:
    print("Errore")
    
if base < 3 or base > 20 or base % 2 == 0:
    print(">> Errore: valore non consentito")
for i in range(1, base + 1, 2):
    for A in range((base - i) // 2):
        print(" ", end="")
    for B in range(i):
        print("*", end="")
    print()



if base == 3:
    print(" +")
if base == 5:
    print("  +")
if base == 7:
    print("   +")
if base == 9:
    print("    +")
if base == 11:
    print("     +")
if base == 13:
    print("      +")
if base == 15:
    print("       +")
if base == 17:
    print("        +")
if base == 19:
    print("         +")



