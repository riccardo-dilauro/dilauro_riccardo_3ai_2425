import os
os.system("cls")

listaManga = []

#Creazione delle funzioni

def aggiungiManga(): #Funzione che permette l'aggiunta di manga alla lista.

    while True:
        try:
            titolo = input("Titolo: ").strip()
            if titolo == "":
                print("Errore: il titolo non può essere vuoto.")
                return

            autore = input("Autore: ").strip()
            if autore == "":
                print("Errore: l'autore non può essere vuoto.")
                return

            editrice = input("Casa editrice: ").strip()
            if editrice == "":
                print("Errore: la casa editrice non può essere vuota.")
                return

            completo = input("Il manga è completo? (Y/N): ").strip().lower()
            if completo != "y" and completo != "n":
                print("Errore: inserisci 'Y' o 'N'.")
                return

            volumi = 0
            if completo == "y":
                volumi = int(input("Numero di volumi: "))
                if volumi <= 0:
                    print("Errore: il numero di volumi deve essere maggiore di zero.")
                    return

            listaManga.append({
                "titolo": titolo,
                "autore": autore,
                "editrice": editrice,
                "volumi": volumi,
                "completo": completo == "y"
            })

            return
        except ValueError:
            print("Errore: inserisci un valore valido.")


def bubbleSort(l):
    """Accetta liste con qualsiasi valore e restituisce la lista ordinata con BubbleSort: bubbleSort( lista )"""
    for n in range(len(l) -1, 0,-1): #Ciclo che parte dall'ultimo indirizzo e finisce alla posizione 0 dando step -1 al valore N
        
        valore = False  #Valore è una variabile che serve a verificare se vi sono stati degli scambi di posto.

        for i in range(n): #Ciclo di verifica e confronto degli elementi all'interno della lista

            if l[i]["volumi"] > l[i + 1]["volumi"]:

                l[i]["volumi"], l[i + 1]["volumi"] = l[i + 1]["volumi"], l[i]["volumi"] #Operazione di scambio elementi

                valore = True #Valore true per segnalare lo scambio avvenuto con successo.
        
        if not valore: #Valore che in caso di nessuno scambio avvenuto fa terminare il ciclo.
            return


def mostraAutore(): #Funzione che permette la ricerca dei manga scritti da un determinato autore.
    autore = input("Autore da cercare: ").strip()
    mangaAutore = []
    for manga in listaManga:
        if manga["autore"].lower() == autore.lower():
            mangaAutore.append(manga)
    
    if len(mangaAutore) == 0:
        print("Nessun manga trovato.")
        return
    
    bubbleSort(mangaAutore)
    for manga in mangaAutore:
        print(manga)


def mostraVolumi(): #Funzione che ricerca il manga che supera un numero minimo di volumi dato in input

    try:
        x = int(input("Numero minimo di volumi: "))
        mangaFiltrati = []
        for manga in listaManga:
            if manga["volumi"] > x:
                mangaFiltrati.append(manga)
        
        if len(mangaFiltrati) == 0:
            print("Nessun manga trovato con più di", x, "volumi.")
            return
        
        for manga in mangaFiltrati:
            print(f"Titolo: {manga['titolo']}, Volumi: {manga['volumi']}")
    except ValueError:
        print("Errore: inserisci un numero valido.")


def ContaManga(): #Funzione che permette di contare i manga e i volumi scritti da un determinato autore

    autore = input("Autore da cercare: ").strip()
    numManga = 0
    numvolumi = 0
    for manga in listaManga:
        if manga["autore"].lower() == autore.lower():
            numManga += 1
            numvolumi += manga["volumi"]
    
    if numManga == 0:
        print("Nessun manga trovato.")
        return
    
    print(f"L'autore {autore} ha scritto {numManga} manga con un totale di {numvolumi} volumi noti.")


def menu(): #Funzione di menù principale.

    while True:
        print("Opzioni:")
        print("1. Aggiungi Manga")
        print("2. Mostra Manga per Autore")
        print("3. Mostra Manga con più di X volumi")
        print("4. Conta Manga e Volumi per Autore")
        print("5. Esci")
        scelta = input(">> ")
        
        if scelta == "1":
            aggiungiManga()
        elif scelta == "2":
            mostraAutore()
        elif scelta == "3":
            mostraVolumi()
        elif scelta == "4":
            ContaManga()
        elif scelta == "5":
            print("Uscita dal programma.")
            return
        else:
            print("Scelta non valida, riprova.")

#Sezione ESECUTIVA

menu()