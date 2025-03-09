import os
from termcolor import cprint
import time
os.system("cls")

val1 = True

while val1:
    try:
        percorso = str(input(">> Inserisci il percorso: "))
        if percorso != "":
            val1 = False    
        
    except:
        print("")
      

estensione = []
try:
    path1 = os.listdir(percorso)
except:
    print("")

if os.path.exists(percorso) == True:

    for i in path1:
        if not os.path.isdir(i):
            print(i)
        
    val = True

    while val:
        valore = str(input("Vuoi aggiungere altre estensioni? "))
        valore.lower()
        if valore == "y":
            estensione1 = str(input(">> Inserisci l'estensione file: "))
            if estensione1.find(".") == True:
                estensione1.lower()
                estensione.append(estensione1)
            else:
                print("Estensione non valida")
        if valore == "n":

            cartelle = str(input("Vuoi vedere le cartelle? "))
            cartelle.lower()
            
            if cartelle == "y":
                valcart = 1
            if cartelle == "n":
                valcart = 0

            if estensione == []:
                for l in path1: 
                    print(l)

            if estensione != []:
                cprint("File: ","red")
                print("")
                for l in path1: #Stampa la lista dei libri con .txt (l'if sotto lo permette)
                    time.sleep(0.05)
                    for i in estensione:
                        if valcart == 1:
                            if os.path.isdir(percorso+l) == True:
                                print(">>",l)
                        if valcart == 0:
                            if os.path.isdir(percorso+l) == False:
                                print(">>",l)
    print("")

else:
    print("<<!>> Errore: Percorso inesistente!")

#c:\Users\RICCARDODILAURO\OneDrive - IIS G. Marconi\3Ai RiccardoDL\Informatica A.S. 2024-2025 3Ai Riccardo Di Lauro\ProveFile