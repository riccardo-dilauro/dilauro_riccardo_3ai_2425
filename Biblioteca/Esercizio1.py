import os
import time
os.system("cls")

listaFile = os.listdir(".") #Assegnazione directory libri a listafile

print("Libri disponibili: ")
print(" ")
for l in listaFile: #Stampa la lista dei libri con .txt (l'if sotto lo permette)
    time.sleep(0.05)
    if ".txt" in l:
        print(">>",l)
print(" ")

namefile = str(input(">> Inserisci il nome file: ")) #Input del nomefile
time.sleep(0.05)
print(" ")

if os.path.exists(namefile) == False: #verifica di esistenza file
    time.sleep(0.05)
    print("<<!>> file non trovato")
    quit()

libro = open(namefile,"r",encoding="utf-8")
parolacce = open("parolacce.txt","r",encoding="utf-8")
ListaParolacce = []
conta = 0

for i in parolacce:
    i = i.strip()
    ListaParolacce.append(i)
    
linea = libro.readline()

for i in ListaParolacce:
    conta += linea.count(i)

print(conta)