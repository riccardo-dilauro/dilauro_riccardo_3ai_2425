import os
from datetime import datetime

def aggiungiElemento(lista):
    """Aggiunge elemento alla collezione, se non già presente."""
    titolo = str(input(">> Inserisci elemento: "))

    luoghi = ["dalmine","verdello","stezzano","suisio","bottanuco","mapello"]
    for i in luoghi:
        print(">> ",i)
    luogo = str(input(">> "))
    luogo.lower()
    if luogo not in luoghi:
        print(">> Luogo non valido.")
        return
        
    dataInput = str(input(">> Inserisci la data (gg/mm/yyyy): "))

    try:
        data = datetime.strptime(dataInput,"%d/%m/%Y")
    except:
        print("Errore nel formato data.")
        return
    print(data)

    etaMinima = int(input(">> Inserisci Età minima: "))
    durata = str(input(">> Inserisci durata: "))

    if titolo not in lista:
        lista.append(titolo[luogo, dataInput, etaMinima, durata])
        print(f">> Elemento '{titolo}' aggiunto con successo.")
        return lista
    else:
        print(">> L'elemento è già presente o non valido.")
        return
    

def modificaElemento(vecchioTitolo, nuovoTitolo, lista):
    """Modifica un elemento esistente con uno nuovo."""

    if vecchioTitolo in lista and nuovoTitolo not in lista:
        for i in range(len(lista)):
            if lista[i] == vecchioTitolo:
                lista[i] = nuovoTitolo
        print(f">> Elemento modificato: '{vecchioTitolo}' >> '{nuovoTitolo}'.")
        return
    print(">> Modifica non valida.")
    return

def eliminaEvento(titolo,lista):
    """Elimina un elemento dalla collezione."""

    if titolo in lista:
        lista.remove(titolo)
        print(f">> Elemento: '{titolo}' eliminato con successo.")
        return
    print(">> Elemento non trovato.")
    return
