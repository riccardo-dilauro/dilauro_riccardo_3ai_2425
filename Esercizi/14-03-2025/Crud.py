import os
import time
os.system("cls")

nomefile = "libri.txt"

libri = []

try:
    f = open(nomefile, "r")
    libri = f.readlines()
    f.close()
    for i in range(len(libri)):
        libri[i] = libri[i].strip()
except:
    libri = []

#Sezione FUNZIONI

def aggiungiLibro(titolo):
    """Aggiunge un libro alla collezione, se non già presente."""

    titolo = titolo.strip()
    if titolo not in libri:
        libri.append(titolo)
        salvaSuFile()
        print(f">> Libro '{titolo}' aggiunto con successo.")
        return
    else:
        print(">> Il titolo è già presente o non valido.")
        return

def modificaLibro(vecchioTitolo, nuovoTitolo):
    """Modifica un titolo esistente con uno nuovo."""

    vecchioTitolo, nuovoTitolo = vecchioTitolo.strip(), nuovoTitolo.strip()
    if vecchioTitolo in libri and nuovoTitolo not in libri:
        for i in range(len(libri)):
            if libri[i] == vecchioTitolo:
                libri[i] = nuovoTitolo
        salvaSuFile()
        print(f">> Libro modificato: '{vecchioTitolo}' >> '{nuovoTitolo}'.")
        return
    print(">> Modifica non valida.")
    return

def eliminaLibro(titolo):
    """Elimina un libro dalla collezione."""

    titolo = titolo.strip()
    if titolo in libri:
        libri.remove(titolo)
        salvaSuFile()
        print(f">> Libro '{titolo}' eliminato con successo.")
        return
    print(">> Libro non trovato.")
    return

def visualizzaLibri():
    """Restituisce la lista dei libri in ordine alfabetico"""

    listaOrdinata = libri[:]
    for i in range(len(listaOrdinata) - 1):
        for j in range(len(listaOrdinata) - i - 1):
            if listaOrdinata[j] > listaOrdinata[j + 1]:
                listaOrdinata[j], listaOrdinata[j + 1] = listaOrdinata[j + 1], listaOrdinata[j]
    
    if listaOrdinata:
        print(listaOrdinata)
    else:
        print(">> Nessun libro presente.")
    return

def cercaLibro(titolo):
    """Controlla se un libro è presente nella collezione."""

    if titolo in libri:
        print(f">> Il libro '{titolo}' è presente nella collezione.")
        return
    print(">> Libro non trovato.")
    return

def salvaSuFile():
    """Salva la collezione su file."""

    f = open(nomefile, "w")
    for libro in libri:
        f.write(libro + "\n")
    f.close()

#Sezione ESECUTIVA

val = True

while val:

    print("Opzioni:             ")
    print("1. Aggiungi libro    ")
    print("2. Visualizza libri  ")
    print("3. Cerca Libro       ")
    print("4. Modifica Libro    ")
    print("5. Elimina Libro     ")
    print("                     ")
    print("0. Esci              ")
    
    scelta = str(input(">> "))

    if scelta == "1":
        
        titolo = str(input(">> Inserisci il titolo del libro: "))
        aggiungiLibro(titolo)
        time.sleep(1)
    if scelta == "2":

        visualizzaLibri()
        time.sleep(1)
    if scelta == "3":

        titolo = str(input(">> Inserisci il titolo da cercare: "))
        cercaLibro(titolo)
        time.sleep(1)
    if scelta == "4":

        titolo = str(input(">> Inserisci il titolo da modificare: "))
        Nuovotitolo = str(input(">> Inserisci nuovo titolo: "))
        modificaLibro(titolo,Nuovotitolo)
        time.sleep(1)
    if scelta == "5":

        titolo = str(input(">> Inserisci il titolo da modificare: "))
        eliminaLibro(titolo)
        time.sleep(1)
    if scelta == "0":

        time.sleep(1)
        val = False
