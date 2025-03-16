import os
import time

fileDati = "strumenti.txt"

#Creazione di funzioni

def caricaDati(): # Funzione che carica i dati dal file "strumenti.txt" e li restituisce come lista
    listaDati = []
    if os.path.exists(fileDati): 
        f = open(fileDati, "r") 
        righe = f.readlines()  

        for riga in righe: 
            parti = riga.strip().split()  # Rimuove spazi e divide la riga in parole
            if len(parti) == 4:  # Se la riga ha 4 elementi, è un dato valido
                listaDati.append([parti[0], parti[1], parti[2], parti[3]])  # Aggiunge il dato alla lista

    return listaDati


def salvaDati(listaDati): # Funzione che salva i dati nel file "strumenti.txt"

    f = open(fileDati, "w") 
    for strumento in listaDati: 
        f.write(strumento[0] + " " + strumento[1] + " " + strumento[2] + " " + str(strumento[3]) + "\n")  #\n serve per andare a capo
    f.close() 
    print(">> Dati salvati.") 


def aggiungiStrumento(listaDati, nome, marca, modello, quantita): # Funzione che aggiunge un nuovo strumento o aggiorna la quantità di uno esistente

    for strumento in listaDati: 
        if strumento[0] == nome and strumento[1] == marca and strumento[2] == modello:  
            strumento[3] = ((strumento[3]) + quantita)  
            return listaDati
    listaDati.append([nome, marca, modello, (quantita)])
    return listaDati


def eliminaStrumento(listaDati, nome, marca, modello):   # Funzione che elimina uno strumento dalla lista

    nuoviDati = []
    for strumento in listaDati:  
        if not (strumento[0] == nome and strumento[1] == marca and strumento[2] == modello): 
            nuoviDati.append(strumento)  
    return nuoviDati


def visualizzaDisponibilita(listaDati, nome, marca):  # Funzione che visualizza la disponibilità degli strumenti

    strumentiTrovati = []
    for strumento in listaDati: 
        if strumento[0] == nome and strumento[1] == marca:  
            strumentiTrovati.append(strumento) 
    
    # Ordina gli strumenti per quantità in ordine decrescente

    for i in range(len(strumentiTrovati)):
        for j in range(i + 1, len(strumentiTrovati)):
            if (strumentiTrovati[i][3]) < (strumentiTrovati[j][3]):
                strumentiTrovati[i], strumentiTrovati[j] = strumentiTrovati[j], strumentiTrovati[i]
    
    for s in strumentiTrovati:  # Stampa i dettagli
        print(">> Modello:", s[2])
        print(">> Quantità:", s[3])
        print(">> ---")


def vendiStrumento(listaDati, nome, marca, modello):  # Funzione che gestisce la vendita di uno strumento

    for strumento in listaDati:
        if strumento[0] == nome and strumento[1] == marca and strumento[2] == modello and (strumento[3]) > 0: 
            strumento[3] = ((strumento[3]) - 1)  
            print(">> Venduto 1", nome, marca, modello)  
            return listaDati
    print(">> Strumento non disponibile.") 
    return listaDati


def menu():
    listaDati = caricaDati()  # Carica i dati dal file
    while True:
        os.system("cls")
        print("Gestione Strumenti Musicali")
        print(">> 1. Aggiungi strumento")
        print(">> 2. Elimina strumento")
        print(">> 3. Visualizza disponibilità")
        print(">> 4. Vendi strumento")
        print(">> 5. Salva ed Esci")
        scelta = input(">> Scegli un'opzione: ")
        
        if scelta == "1":
            nome = input(">> Nome: ")
            marca = input(">> Marca: ")
            modello = input(">> Modello: ")
            quantita = input(">> Quantità: ")
            listaDati = aggiungiStrumento(listaDati, nome, marca, modello, (quantita))  

        elif scelta == "2":
            nome = input(">> Nome: ")
            marca = input(">> Marca: ")
            modello = input(">> Modello: ")
            listaDati = eliminaStrumento(listaDati, nome, marca, modello)  

        elif scelta == "3":
            nome = input(">> Nome: ")
            marca = input(">> Marca: ")
            visualizzaDisponibilita(listaDati, nome, marca)  

        elif scelta == "4":
            nome = input(">> Nome: ")
            marca = input(">> Marca: ")
            modello = input(">> Modello: ")
            listaDati = vendiStrumento(listaDati, nome, marca, modello)  

        elif scelta == "5":
            salvaDati(listaDati) 
            print(">> Chiusura in corso!")  
            time.sleep(1)
            os.system("cls")
            return
        
        else:
            print(">> Scelta non valida, riprova.") 

#Sezione ESECUTIVA

menu()