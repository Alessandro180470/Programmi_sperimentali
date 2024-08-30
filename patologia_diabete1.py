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

        if self.ck >=200:
            print(f'Attenzio:il valore del ck {self.ck} è alto ')
        if self.glicata == 0:
           raise  ValueError(f'Attenzione:valore glicata {self.glicata} non valido')

    def __str__(self):
        return f'La glicata è: {self.glicata} con {self.mmol} mmol e un ck: {self.ck} analisi eseguita in data {self.data}'
class calcolo_valore:
    
    def __init__(self):
        self.valore = []

    def append(self,value):
        self.valore.append(value)

    def media_ck(self):
        if len(self.valore) == 0:
            raise ValueError('Attenzione non ci sono valori da valutare')
        risultato = [v.ck for v in self.valore]
        return sum(risultato)/len(risultato)

    def media_glicata(self):
        if len(self.valore) == 0:
            raise ValueError('Attenzione non ci sono valori da valutare')
        risultato = [v.glicata for v in self.valore]
        return sum(risultato)/len(risultato)


#analisi = patologia_dt1(float(input('Inserisci valore glicata: ')), float(input('Inserisci valore mmol: ')),
        #                float(input('Inserisci valore ck: ')), input('Inserisci la data delle analisi: '))
#analisi1 =patologia_dt1(float(input('Inserisci valore glicata: ')),int(input('Inserisci valore mmol: ')),int(input('Inserisci valore ck: ')),input('Inserisci data del prelievo: '))
analisi = patologia_dt1(6.3,51,330,'2024/09/12')
analisi1 = patologia_dt1(6.9,55,451,'2024/10/21')
analisi2 = patologia_dt1(5.9,51,412,'2024/11/22')
def calcola_valore_maggiore():
    val = max(analisi.ck,analisi1.ck,analisi2.ck)
    val_min = min(analisi.ck,analisi1.ck,analisi2.ck)
    print(f'Il valore massimo riscontrato del CK rilevato nelle analisi è: {val}')
    print(f'Mentre il valore minimo riscontrato è: {val_min}')
def esegui_funzione():
    print(analisi)
    print(analisi1)
    miei_valori = calcolo_valore()
    miei_valori.append(analisi)
    miei_valori.append(analisi1)
    print(f'Il valore medio del ck è: {miei_valori.media_ck()}')
    print(f'Il valore medio della glicata è: {miei_valori.media_glicata()}')
    calcola_valore_maggiore()
if(__name__)=='__main__':
    esegui_funzione()
print('Il nome del modulo è :',__name__,)
