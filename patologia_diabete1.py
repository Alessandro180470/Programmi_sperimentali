"""
Realizzare un programma che analizzi tutti i valori ematici riscontrati durante le varie
analisi del sangue e osservare le evoluzioni dei valori riscontrati.Ricordiamo che il valore
della glicata rappresenta la media della glicemia valutata nel range di un periodo di durata 3 mesi
"""


class patologia_dt1:
    def __init__(self, glicata, mmol, ck, data):
        self.glicata = glicata
        self.mmol = mmol
        self.ck = ck
        self.data = data

    def __str__(self):
        return f'La glicata è: {self.glicata} con {self.mmol} mmol e un ck: {self.ck} analisi eseguita in data {self.data}'


analisi = patologia_dt1(float(input('Inserisci valore glicata: ')), float(input('Inserisci valore mmol: ')),
                        float(input('Inserisci valore ck: ')), input('Inserisci la data delle analisi: '))

print(analisi)
