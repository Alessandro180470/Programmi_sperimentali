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
        """
        Questo modulo ricerca il valore massimo del ck
        :return: MAX CK
        """
        risultato = [v.glicata for v in self.valore]
        return max(risultato)

    def ck_uguali(self, ck):
        """
        Questo modulo ci consente di rilevare su di
        un'analisi ematica se ci sono valori di ck
        o inserendo opportuni valori di parametri ematici
        confrontarli e vedere si ci sono valori uguali in analisi
        effettuate in date diverse
        :param ck: o altri parametri da confrontare
        :return: il valore da confronare
        """
        rilevazioni = []
        for v in self.valore:
            if v.ck == ck:
                rilevazioni.append(v)
        return rilevazioni

    def confrontare_analisi_date_uguali(self,data):
        """
        Il modulo trova se ci sono delle analisi corrispondenti alla
        stessa data e identifica l'errore di inserimento del dato
        stesse date
        :param data:data
        :return:nessuno
        """
        count = 0
        for v in self.valore:
            dati = []
            if v.data == data :
                count = count + 1
                dati.append(v.data)
        print(f'Hai inserito la stessa data di un analisi infatti ne ho trovate:{count} ')
        print('Inserisci una nuova data')






if (__name__) == '__main__':
    print('Il nome del modulo di importazione è :', __name__, )
else:
    print('Il modulo importato è :',__name__)











