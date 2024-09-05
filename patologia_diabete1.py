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

        if self.ck >= 200:
            print(f'Attenzio:il valore del ck {self.ck} è alto ')
        if self.glicata == 0:
            raise ValueError(f'Attenzione:valore glicata {self.glicata} non valido')
        if self.glicata > 6.7:
            print(f'Attenzione hai un valore di glicata {self.glicata} inizio PREDIABETE')

    def __str__(self):
        return f'La glicata è: {self.glicata} con {self.mmol} mmol e un ck: {self.ck} analisi eseguita in data {self.data}'



class calcolo_valore:

    def __init__(self):
        self.valore = []

    def append(self, value):
        self.valore.append(value)

    def media_ck(self):
        if len(self.valore) == 0:
            raise ValueError('Attenzione non ci sono valori da valutare')
        risultato = [v.ck for v in self.valore]
        return sum(risultato) / len(risultato)

    def media_glicata(self):
        if len(self.valore) == 0:
            raise ValueError('Attenzione non ci sono valori da valutare')
        risultato = [v.glicata for v in self.valore]
        return sum(risultato) / len(risultato)

    def val_min_glicata(self):
        risultato = [v.glicata for v in self.valore]
        return min(risultato)

    def val_max_glicata(self):
        risultato = [v.glicata for v in self.valore]
        return max(risultato)

if (__name__) == '__main__':
    print('Il nome del modulo di importazione è :', __name__, )
else:
    print('Il modulo importato è :',__name__)











