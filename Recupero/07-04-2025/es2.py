import os
os.system("cls")

valore = int(input(">> Inserisci un numero dispari >= a 3: "))
val = True

if valore %2 != 0:

    while val:
        print("*"*valore)