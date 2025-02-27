import os
os.system("cls")


def ricercaLineareBase(l,numDaCercare):
    """Accetta qualiasi lista e qualsiasi valore da ricercare. Restituisce un valore TRUE se è stato trovato. Altrimenti: FALSE"""
    risultato = False #Valore con cui si restituisce il risultato della funzione
    val = len(l) #Calcola la lunghezza della lista per itinerare tot. volte il ciclo FOR

    for i in range(val): #Va in ciclo itinerando per Val. volte

        if l[i] == numDaCercare: #Se il valore è corrispondente a quello richiesto:

            risultato = True #Il risultato di output diventerà TRUE

    return risultato #Viene ritornato il risultato di OUTPUT


def ricercaLineareMigliorata(l,numDaCercare):
    """Accetta qualiasi lista e qualsiasi valore da ricercare. Restituisce un valore TRUE se è stato trovato. Altrimenti: FALSE"""
    risultato = False #Valore con cui si restituisce il risultato della funzione
    val = len(l) #Calcola la lunghezza della lista per itinerare tot. volte il ciclo FOR

    for i in range(val): #Va in ciclo itinerando per Val. volte

        if l[i] == numDaCercare: #Se il valore è corrispondente a quello richiesto:

            risultato = True #Il risultato di output diventerà TRUE
            return risultato #Viene interrotto il ciclo e viene restituito l'output di: Risultato
        
    return risultato #Viene ritornato il risultato di OUTPUT False


#Codice di Testing

l = [1,2,3,4,5]

print(ricercaLineareBase(l,6))

print(ricercaLineareMigliorata(l,6))