import os
os.system("cls")

pacchetti = [
 {'nome':'Parigi', 'prezzo':500, 'inizio':'3/05/2025', 'fine':'10/05/2025', 'posti':10},
 {'nome':'Londra', 'prezzo':520, 'inizio':'11/05/2025', 'fine':'16/05/2025', 'posti':2},
 {'nome':'Barcellona', 'prezzo':380, 'inizio':'13/06/2025', 'fine':'15/06/2025', 'posti':12},
 {'nome':'Amsterdam', 'prezzo':650, 'inizio':'14/04/2025', 'fine':'19/04/2025', 'posti':5},
 {'nome':'Amsterdam', 'prezzo':600, 'inizio':'25/05/2025', 'fine':'1/06/2025', 'posti':8}
]
prezzi = []
conta = 0
val = True
while val:
    print("                                 ")
    print("opzioni:                         ")
    print("                                 ")
    print("1. Visualizza pacchetti          ")
    print("2. Aggiungi pacchetto            ")
    print("3. Modifica prezzo               ")
    print("4. Visualizza in ordine crescente")
    print("                                 ")  
    print("0. Esci                          ")

    scelta = int(input(">> "))

    if scelta == 1:
        os.system("cls")
        print("Visualizza Pacchetti!")

        for i in pacchetti:
            for a in i.items():
                conta += 1
                print(conta,a[0]," : ",a[1])
    
    if scelta == 2:
        os.system("cls")
        print("Aggiungi pacchetto!")
        
        nome = str(input(">> Inserisci la destinazione: "))
        prezzo = float(input(">> Inserisci il prezzo: "))
        inizio = str(input(">> Inserisci la data di inizio (gg/mm/YYYY): "))
        fine = str(input(">> Inserisci la data di fine (gg/mm/YYYY): "))
        posti = int(input(">> Inserisci numero di posti: "))

        insieme = {"nome":nome,"prezzo":prezzo,"inizio":inizio,"fine":fine,"posti":posti}
        pacchetti.append(insieme)
        print("Salvato con successo!")

    if scelta == 3:
        os.system("cls")
        print("Modifica prezzo!")
        
        sceltaCittà = str(input(">> Inserisci la città del pacchetto da modificare: "))
        for i in pacchetti:
            if sceltaCittà in i.values():
                nuovoPrezzo = int(input(">> Inserisci nuovo prezzo: "))
                i["prezzo"] = nuovoPrezzo
                print("Salvato con successo!")

    if scelta == 4:
        os.system("cls")
        print("Visualizza in ordine crescente!")        

        for i in pacchetti:
            valore = i['prezzo']
            prezzi.append(valore)
            prezzi.sort()
            print(prezzi)
            
    if scelta == 0:
        val = False
        os.system("cls")
        print("uscita dal programma...")