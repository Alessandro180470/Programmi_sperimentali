numero_dichetti = int(input("Inserisci numero dischetti: "))
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

print(mosse_singole)
print(f'Il numero totale delle mosse è: {numero_m}')
pos = ['AC', 'AB', 'CB', 'AC', 'BA', 'BC', 'AC']
if numero_dichetti % 2 != 0:
    i = 0
    while i < numero_m:
        print(pos[i], end=' ')

        i = i + 1
    print()











