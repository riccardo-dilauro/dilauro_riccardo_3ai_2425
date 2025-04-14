import os
os.system("cls")

f = open("Verifica\input.txt")
a = f.readlines()

conta = 0
for i in a:
    a.append(conta)

print(a)
Stato = str(input(">> Vuoi adottare un nuovo animale? y/n "))
Animale = int(input(">> Numero dell'animale che si desidera adottare: "))


conta = 1
for i in a:
    i.append(conta)
    conta += 1

print(a)