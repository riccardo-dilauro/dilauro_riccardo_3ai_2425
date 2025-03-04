import os
os.system("cls")

########################################################################################################
#Funzioni importate

def ricercaLineareMigliorata(l,numDaCercare):
    """Accetta qualiasi lista e qualsiasi valore da ricercare. Restituisce un valore TRUE se è stato trovato. Altrimenti: FALSE"""
    risultato = ">> lo strumento richiesto non c'è" #Valore con cui si restituisce il risultato della funzione
    val = len(l) #Calcola la lunghezza della lista per itinerare tot. volte il ciclo FOR

    for i in range(val): #Va in ciclo itinerando per Val. volte

        if l[i] == numDaCercare: #Se il valore è corrispondente a quello richiesto:

            risultato = ">> lo strumento richiesto c'è" #Il risultato di output diventerà TRUE
            return risultato #Viene interrotto il ciclo e viene restituito l'output di: Risultato
        
    return risultato #Viene ritornato il risultato di OUTPUT False

########################################################################################################

#Esercizio 1

a = open("strumenti.txt","r",encoding="utf-8") #Assegna alla variabile "a" l'appertura del file in modalità reading con formato utf-8
l = []  #Inizializza la lista "l" per contnere gli strumenti

for riga in a: #Ciclo che permette di scorrere le righe all'interno del file.

    riga = riga.strip() #Rimozione dei caratteri di spaziatura all'inizio e alla fine della riga (/n)

    riga= riga.lower() #Trasformazione in minuscolo dei caratteri

    l.append(riga) #Inserimento nella lista del valore assegnato alla variabile "Righe"

    print(f">> ",riga) #"Stampo la riga"

strumento = str(input(">> Che strumento si desidera ricercare? ")) #Assegnazione alla variabile "strumento" del valore stringa dato in input dall'utente.
strumento = strumento.lower() #Trasformazione dell'input in caratteri minuscoli.

print(ricercaLineareMigliorata(l,strumento)) #Utilizzo della funzione "RicercaLineareMigliorata" per ricercare lo strumento dato in input precedentemente.

