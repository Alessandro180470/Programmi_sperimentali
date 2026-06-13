#Il programma consiste in un algoritmo che calcola lo spostamento dei dischetti da un pirolo nominato A ad un pirolo nominato C
#il numero dei dischetti totali è 10 l'algoritmo deve calcolare quante mosse ci vogliono inserendo a piacimento il numero dei dischetti#
"""
Con un numero  N piattelli il piattello
più piccolo D1 si muoverà 2^N/2 e il pittello D2 si muoverà 2^N/4 il piattello D3 si muoverà 2^N/8
#Il piattello più grande si muoverà sempre 1 volta sola cioè 2^N/2^N
Le variabili sono cosi' definite:
-numero_dischetti numero dei dischetti che vogliamo inserire
-numero_m_s è il numero di mosse che fa il singolo dischetto
-numero_m è il numero di mosse totali dei dischetti
-ricordiamo che il programma è basato su ricorsione
"""


numero_dichetti = int(input("Inserisci numero dischetti: "))#inseriamo il numero di dischetti
numero_m = 0
numero_m_s = 0
for i in range(numero_dichetti):
    numero_m = 2 ** (numero_dichetti) - 1  # Calcolo del numero totale delle mosse
i = 1

mosse_singole = []
while i <= numero_dichetti:
    numero_m_s = 2 ** (numero_dichetti - i)  # Calcolo mosse di ogni singolo dischetto

    mosse_singole.append(numero_m_s)  # Creazione di una lista delle mosse dei singoli dischetti

    i = i + 1
i = 1
while i <= numero_dichetti:
    print(f'D{i}',end=' ')
    i = i + 1
print()
print(f'mosse singoli dischetti: {mosse_singole}')
print(f'Il numero totale delle mosse è: {numero_m}')
pos_dispari = ['D1->AC','D2->AB','D1->CB','D3->AC','D1->BA','D2->BC', 'D1->AC']#giro completo di 3 dischetti
pos_pari = ['AB', 'AC', 'BC', 'AB', 'CA', 'CB', 'AB', 'AC', 'BC', 'BA', 'CA', 'BC', 'AB', 'AC', 'BC']#giro completo di 4 dischetti

if numero_dichetti % 2 != 0 and numero_m <=15 :  #Calcolo le mosse con un numero di dischetti dispari e va da uno a tre
    i = 0
    while i < numero_m:
        print(f'{pos_dispari[i]}', end=' ')

        i = i + 1
print()

if numero_dichetti %2!=0 and numero_m >=31:
            totale = []
            for r in  (pos_dispari*numero_m):
                totale.append(r)
            print(totale[0:numero_m],end='')
print()

if numero_dichetti % 2 == 0 and numero_m <= 15 :  # Abbiamo il numero dei dischetti è pari e va da due a quattro
    i = 0
    while i < numero_m:
        print(f'{pos_pari[i]}', end=' ')

        i = i + 1
    print()
if numero_dichetti %2==0 and numero_m >15:
            totale = []
            for r in  (pos_pari*numero_m):
                totale.append(r)
            print(totale[0:numero_m])

def posizione_dischetti(n):
    if n <=0:  # Caso base
        return
    else:
        posizione_dischetti(n - 2)  # Chiamata ricorsiva
        a =numero_m*pos_dispari#pos_pari
    print ('D1',a[n-1],n)
#b = posizione_dischetti(11)


p =posizione_dischetti(numero_m)







