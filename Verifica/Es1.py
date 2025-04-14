import os
os.system("cls")

f = open("Verifica\input.txt")
a = f.readlines()

for i in a:
    for o in i:
        if o == "-":
            if f[i] > f[i-1]: 
                f[i] , f[i-1] = f[i-1], f[i]
        else:
            pass
a.sort()
g = open("Verifica\output.txt")

"""
for i in range(len(a)):
    for f in a:
        if f[i] > f[i-1]: 
            f[i] , f[i-1] = f[i-1], f[i]
"""
print(a)



f.close()
g.close()