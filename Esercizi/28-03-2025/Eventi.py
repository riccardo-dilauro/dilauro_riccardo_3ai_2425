import os
import time
from termcolor import cprint
from LibreriaCrud import aggiungiElemento,modificaElemento,eliminaEvento
os.system("cls")

lista = []
val = True

while val:

    cprint("Opzioni:             ","red")
    print("1. Nuovo evento      ")
    print("2. Visualizza eventi ")
    print("3. Modifica evento   ")
    print("4. Elimina evento    ")
    print("                     ")
    cprint("0. Esci              ","cyan")
    print("                     ")
    
    scelta = str(input(">> "))

    if scelta == "1":
        aggiungiElemento(lista)
        print(lista)
        time.sleep(1)
        os.system("cls")

    if scelta == "2":
        for i in lista:
            print(i)
        time.sleep(3)
        os.system("cls")

    if scelta == "3":
        vecchioEvento = str(input(">> Titolo da modificare: "))
        NuovoEvento = str(input(">> Nuovo titolo: "))
        modificaElemento(vecchioEvento,NuovoEvento,lista)
        time.sleep(1)
        os.system("cls")

    if scelta == "4":
        EventoRemove = str(input(">> Evento da eliminare: "))
        eliminaEvento(EventoRemove,lista)
        time.sleep(1)
        os.system("cls")

    if scelta == "0":
        cprint(">> Chiusura del programma...","red")
        time.sleep(1)
        os.system("cls")

        val = False