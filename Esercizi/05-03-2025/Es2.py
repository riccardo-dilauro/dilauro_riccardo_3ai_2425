import os
from termcolor import colored
import random

os.system("cls")

#Esercizio 2

a = open("frutta.txt","r",encoding="utf-8") #Assegna alla variabile "a" l'appertura del file in modalità reading con formato utf-8
l = []  #Inizializza la lista "l" per contnere gli strumenti
colori = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]

######################################################################################################################################

for riga in a: #Ciclo che permette di scorrere le righe all'interno del file.

    riga = riga.strip() #Rimozione dei caratteri di spaziatura all'inizio e alla fine della riga (/n)

    riga = riga.lower() #Trasformazione in minuscolo dei caratteri

    l.append(riga) #Inserimento nella lista del valore assegnato alla variabile "Righe"

    print(f">> ",riga) #"Stampo la riga"

t = (l) #assegnazione ad una tupla del valore della lista
print(t) #stampa della tupla

a = 0 #Assegnazione alla variabile a (indice del valore da trovare) del valore iniziale: 0

for i in t: #Ciclo che permette lo scorrimento dei valori all'interno della tupla

    colore = random.choice(colori)  #Sceglie il colore casualmente fra la lista di colori

    print(colored(t[a], colore), end=" ")  # Stampa parola colorata

    a += 1 #Incrementa l'indice per continuare il ciclo.