"""
Realizzare un programma che analizzi tutti i valori ematici riscontrati durante le varie
analisi del sangue e osservare le evoluzioni dei valori riscontrati.Ricordiamo che il valore
della glicata rappresenta la media della glicemia valutata nel range di un periodo di durata 3 mesi
In questo programma utilizzeremo anche lo SQM cioè lo scarto quadratico medio o chiamato anche
deviazione stadard questi parametri ci permettono di capire di quanto si discostano i valori
della distribuzione (dati delle analisi specifici es. mmol oppure glicata)dalla media
"""
import collections
import dataclasses
import keyword
import operator
from math import sqrt


# class patologia_dt1:
#     def __init__(self, glicata, mmol, ck, data):
#         self.glicata = glicata
#         self.mmol = mmol
#         self.ck = ck
#         self.data = data
#         if self.glicata == 0:
#             raise ValueError(f'Attenzione:valore glicata {self.glicata} non valido')
#         elif 6.6 <= self.glicata <= 6.7:
#             print(f'Attenzione il tuo valore della glicata {self.glicata} è potenzialmente in PREDIABETE ')
#         elif 6.8 <= self.glicata <= 7.0:
#             print(f'Attenzione il tuo valore della glicata {self.glicata} è alto sei a rischio DIABETE')
#
#     def __str__(self):
#         return f'La glicata è: {self.glicata} con {self.mmol} mmol e un ck: {self.ck} analisi eseguita in data {self.data}'
@dataclasses.dataclass
class patologia_dt1:
    glicata: float
    mmol: int
    creatinina: float
    colesterolo: int
    ck: int
    data: str

    def copy(self):
        """
        Questo modulo effettua una copia di se stesso
        :return:
        """
        return patologia_dt1(self.glicata, self.mmol, self.creatinina, self.colesterolo, self.ck, self.data)

    def __str__(self):
        return f'Valore glicata: {self.glicata}, valore mmol: {self.mmol}, valore ck: {self.ck}, valore creatinina mg/dl: {self.creatinina},valore colesterolo :{self.colesterolo}, analisi eseguite in data: {self.data}'


# def estrai_campo_data(d):
#     return d.data
class calcolo_valore:

    def __init__(self):

        self.valore = []

    def append(self, value):
        self.valore.append(value)

    def media_ck(self):
        """
               Questo modulo ci consente di effettuare
               una media di tutti i valori analizzati
               della ck presa in esame
               :return: Il risultato della media del ck
               """
        if len(self.valore) == 0:
            raise ValueError('Attenzione non ci sono valori da valutare')
        risultato = [v.ck for v in self.valore]
        return sum(risultato) / len(risultato)

    def valore_nullo_ck(self):
        for v in self.valore:
            if v.ck == 0:
                raise ValueError('Hai inserito un valore di  CK nullo')

    def ck_alto(self):
        """
        Questo modulo ci consente di verificare
        se il valore riscontrato nelle analisi
        risulti superare la soglia di 200
        :return: il valore di ck
        """
        val_max = []

        for v in self.valore:

            if v.ck >= 220:
                val_max.append(v.ck)
                print(f'Attenzione il valore di ck che è :{v.ck} risulta essere molto alto rilevato in data:{v.data}')
        print(f'Ho rilevato {len(val_max)} valori alti del CK sopra i 200')
        return val_max

    def media_glicata(self):
        """
        Questo modulo ci consente di effettuare
        una media di tutti i valori analizzati
        della glicata presa in esame
        :return: Il risultato della media della glicata
        """
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
    def media(self):
        """
        da rivedere dobbiamo calcolare il sigma
        :return:
        """
        risultato = [t.mmol for t in self.valore]
        media = sum(risultato)/len(risultato)
        return len(self.valore)/media



    def conta_valori_ck(self):
        """
        Questo modulo ci consente di individuare
        valori uguali del CK nelle varie analisi
        effettuate
        :return: risultato (valori ck trovati)
        """
        risultato = collections.Counter(self.ck_alto())
        for v in risultato:
            if risultato[v] > 1:
                val = str('valori')
            else:
                val = str('valore')
            print(f'Ho rilevato {risultato[v]} {str(val)} con un ck {v} ')
        return risultato.most_common()

    def media_e_valore_sqm_mmol(self):
        """
        Questo modulo consente di calcolare lo scostamento
        quadratico medio di un insieme di valori assegnati
        :return: il valore sqm e della media
        """
        mmol = []
        for v in self.valore:
            mmol.append(v.mmol)
            media = sum(mmol)/len(mmol)
            val = []
        for i in range (len(mmol)):
            val.append((mmol[i] - media))
        sqm_tot = []
        for f in range (len(val)):
            sqm = (val[f]**2)
            sqm_tot.append(sqm)
        valore_sqm = (sum(sqm_tot)/len(val))#Ricordiamo che lo sqm è lo scarto quadratico medio
        coefficiente_variazione = round(sqrt(valore_sqm)/media*100,4)
        return (f'Il valore del SQM dei mmol è: {round(sqrt(valore_sqm),3)} la media dei mmol è : {round(media,3)} i valori MMOL :{mmol} il coefficiente di variazione {coefficiente_variazione}%')


    def media_e_valore_sqm_glicata(self):
        """
        Questo modulo consente di calcolare lo scostamento
        quadratico medio di un insieme di valori assegnati
        :return: il valore sqm e della media
        """
        glicata = []
        for v in self.valore:
            glicata.append(v.glicata)
            media = sum(glicata)/len(glicata)
            val = []
        for i in range (len(glicata)):
            val.append((glicata[i] - media))
        sqm_tot = []
        for f in range (len(val)):
            sqm = (val[f]**2)
            sqm_tot.append(sqm)
        valore_sqm = (sum(sqm_tot)/len(val))#Ricordiamo che lo sqm è lo scarto quadratico medio
        coefficiente_variazione = round(sqrt(valore_sqm) / media*100, 4)
        return (f'Il valore del SQM della glicata è: {round(sqrt(valore_sqm),3)} la media della glicata è : {round((media),3)} i corrispettivi valori:{glicata} il valore della varianza è : {round((valore_sqm),3)} coefficiente di variazione {coefficiente_variazione}%')

    def calcolo_coefficiente_variazione(self):
        """
        Questo modulo ci consente di verificare la
        variabilita tra due grandezze di unità di
        misura differenti
        :return: coefficiente di variabilità
        """
        value2 = []
        for v in self.valore:

            value2.append(v.mmol)
            media = sum(value2) / len(value2)
            val = []
        for i in range(len(value2)):
            val.append((value2[i] - media))
        sqm_tot = []
        for f in range(len(val)):
            sqm = (val[f] ** 2)
            sqm_tot.append(sqm)
        valore_sqm = (sum(sqm_tot) / len(val))  # Ricordiamo che lo sqm è lo scarto quadratico medio
        coefficiente_variazione = round(sqrt(valore_sqm) / media * 100, 4)
        coef_ = coefficiente_variazione/media
        value3 = []

        for v in self.valore:
            value3.append(v.glicata)
            media1 = sum(value3) / len(value3)
            val = []
        for i in range(len(value3)):
            val.append((value3[i] - media1))
        sqm_tot = []
        for f in range(len(val)):
            sqm = (val[f] ** 2)
            sqm_tot.append(sqm)
        valore_sqm = (sum(sqm_tot) / len(val))  # Ricordiamo che lo sqm è lo scarto quadratico medio
        coefficiente_variazione1 = round(sqrt(valore_sqm) / media1 * 100, 4)
        coef1 = coefficiente_variazione1/media1
        if coef_ > coef1:
            return f'Variabilita della glicata che è:{round(coef_,4)} e maggiore di quella dei mmol che è:{round(coef1,4)}'

        return (f'Variabilità mmol che è :{round(coef1,4)} è maggiore di quella della glicata che è:{round(coef_,4)}')

    def elimina_dati(self,valore):
        risultato = [v for v in self.valore if v.ck >= valore]
        print(f'Ho eliminato tutti i valori di ck speriori a {valore}')
        return risultato


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
        print(f'Ho trovato {len(rilevazioni)} valori uguali')

        return rilevazioni

    def find_data(self, data):
        """
        Questo modulo ci consente inserendo la
        data dell'analisi di trovare i valori
        da noi inseriti nell'append della classe
        di analisi_ematiche
        :param data: La data del'analisi
        :return: l'oggetto che appartiene a
        tale data
        """

        rilevazioni = []
        for v in self.valore:
            if v.data == data:
                rilevazioni.append(v)
                return rilevazioni
        raise ValueError(f'Data inserita non trovata ')

    def has_data(self, data):
        """
        Cerca la data dell'analisi se la data non c'è il
        dato non viene trovato
        :param data:la data dell'analisi
        :return: v se il dato è trovato
        altrimenti abbiamo un'eccezione dove non viene
        trovata la data
        """
        for v in self.valore:
            if v.data == data:
                return v
        raise ValueError(f'data non valida {data} ')

    def has_data1(self, data):
        for v in self.valore:
            if v.data == data:
                return v
        return None

    def copy(self):
        nuovo = calcolo_valore()

        for v in self.valore:
            nuovo.valore.append(v.copy())
        return nuovo

    def crea_migliorato(self):
        """
        Crea una copia del totale delle analisi inserite
        e aggiungie un determinato valore di glicata non toccando
        i valori delle analisi ematiche
        :return: nuovo
        """
        nuovo = self.copy()
        #nuovo.valore = self.valore.copy()

        for v in nuovo.valore:
            if 6.0 <= v.glicata <= 6.6:
                v.glicata += 1
            elif 6.7 <= v.glicata <= 6.9:
                v.glicata += 2
            elif 7.0 <= v.glicata <= 7.5:
                v.glicata += 3
        return nuovo

    def crea_ordinato_per_data(self):
        nuovo = self.copy()
        # ordina_per_data
        nuovo.ordina_per_data()
        return nuovo

    def ordina_per_parametri(self,valore):
        """
        Questo modulo ci consente di ordinare i valori in ordine crescente mmol
        :return: \
        """
        #ordina self.valore per data analisi
        #self.valore.sort(key=estrai_campo_data)
        self.valore.sort(key=operator.attrgetter(valore), reverse=False)
        #self.valore.sort(key=lambda d : d.data)
        #self.valore.sort()
        print('I valori sono ordinati in senso crescente')

    def cancella_valori_analisi(self, mmol):
        """
        Questo modulo ci consente di eliminare
        delle analisi con un valore mmol maggiore o
        uguale al valore inserito
        :param mmol: è un parametro della glicemia
        :return:le analisi rimaste
        """
        nuove_analisi = [v for v in self.valore if v.mmol >= mmol]
        print("Lista delle analisi modificate:")
        print(f'Numero analisi rimaste:{len(nuove_analisi)}')
        #return nuove_analisi

    def cancella_valori_analisi_ck(self, ck):
        """
        Questo modulo ci consente di eliminare
        delle analisi con un valore ck maggiore o
        uguale al valore inserito
        :param ck: è un parametro della glicemia
        :return:le analisi rimaste
        """
        nuove_analisi = [v for v in self.valore if v.ck > ck]
        print(f'Questa è la lista delle analisi con un valore di CK maggiore di: {ck}')
        print(f'Numero analisi rimaste:{len(nuove_analisi)}')
        return nuove_analisi

    def stampa(self):
        """
        Questo modulo ci stampa sia analisi ematiche che
        il sistema migliorato più la media della glicata e del ck
        ma questi due valori possono essere modificati
        :return: non abbiamo nessun ritorno
        """
        print(f'Hai in totale {len(self.valore)} analisi')
        for v in self.valore:
            print(v)
        print(f'La media della glicata vale ({self.media_glicata():.3f})')
        print(f'La media del ck è : ({self.media_ck():.3f})')


"""

 opzione 1 :
 metodo stampa_per_nome e metodo stampa_per_altro_valore, che semplicemente stampano e non modificano nulla
 
 opzione 2 :
 metodo crea_libretto_ordinato_per_nome, ed un metodo crea_libretto_ordinato_per_punteggio, che creano
 delle copie separate, sulle quali potro' chiamare il metodo stampa()
 
 opzione 3 :
 metodo ordina_per_nome, che modifica il libretto stesso riordinando i Voti , e ordina per punteggio poi userò metodo 
 stampa()
 + aggiungiamo gratis un metodo copy()
 
 opzione 2bis :
 crea una copia shallow del libretto
"""
if (__name__) == '__main__':
    print('Il nome del modulo di importazione è :', __name__, )
else:
    print('Il modulo importato è :', __name__)
#Arrivato alla lezione L07 38:37 minuti
