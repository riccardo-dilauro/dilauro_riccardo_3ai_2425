import os
os.system("cls")

def bubbleSort(l):
    """Accetta liste con qualsiasi valore e restituisce la lista ordinata con BubbleSort: bubbleSort( lista )"""
    for n in range(len(l) -1, 0,-1): #Ciclo che parte dall'ultimo indirizzo e finisce alla posizione 0 dando step -1 al valore N
        
        valore = False  #Valore è una variabile che serve a verificare se vi sono stati degli scambi di posto.

        for i in range(n): #Ciclo di verifica e confronto degli elementi all'interno della lista

            if l[i] > l[i + 1]:

                l[i], l[i + 1] = l[i + 1], l[i] #Operazione di scambio elementi

                valore = True #Valore true per segnalare lo scambio avvenuto con successo.
        
        if not valore: #Valore che in caso di nessuno scambio avvenuto fa terminare il ciclo.
            return

def insertionSort(l):
    """Accetta liste con qualsiasi valore e restituisce la lista ordinata con insertionSort: insertionSort( lista )"""
    for i in range(1, len(l)): #Ciclo che parte dalla seconda posizione e arriva alla fine della lista

        valore = l[i]  # Elemento da posizionare nella parte ordinata

        a = i - 1 #Indice usato per spostare gli elementi
        
        while a >= 0 and l[a] > valore:# Sposta gli elementi della parte ordinata per fare spazio

            l[a + 1] = l[a]  # Sposta in avanti nella posizione successiva

            a -= 1 #Decremento per controllare i valori precedenti

        l[a + 1] = valore # Inserisce l'elemento nella posizione corretta


#Esempi di prova

l = [5, 3, 8, 6, 2]
insertionSort(l)
print(l) 


l = [6,49,52,121,8,0,6,2]
bubbleSort(l)
print(l)