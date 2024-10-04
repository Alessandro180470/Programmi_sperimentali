import array
import collections

import patologia_diabete1
from patologia_diabete1 import calcolo_valore, patologia_dt1

analisi_ematiche = calcolo_valore()
analisi1 = patologia_dt1(7.1, 57, 0.22, 160, 540, '2020/10/21')
# analisi_ematiche.append(analisi1)
analisi_ematiche.append(patologia_dt1(6.4, 40, 0.12, 87, 220, '2024/09/26'))
analisi_ematiche.append(patologia_dt1(7.0, 52, 0.3, 220, 560, '2021/10/21'))
analisi_ematiche.append(patologia_dt1(7.1, 55, 0.5, 165, 540, '2022/10/21'))
analisi_ematiche.append(patologia_dt1(7.4, 53, 0.66, 160, 250, '2023/09/30'))
analisi_ematiche.append(patologia_dt1(6.4, 48, 0.66, 185, 366, '2024/09/30'))
analisi_ematiche.append(patologia_dt1(6.9, 49, 0.1, 195, 120, '2017/11/29'))
analisi_ematiche.append(patologia_dt1(7.0, 49, 0.25, 240, 220, '2021/10/23'))

#analisi_ematiche.append(patologia_dt1(float(input('Iserisci v gli')),int(input('ins val m')),int(input('ins v ck')),input('inserisci data')))

"""

analisi = patologia_dt1(float(input('Inserisci valore glicata: ')), float(input('Inserisci valore mmol: ')),
                float(input('Inserisci valore ck: ')), input('Inserisci la data delle analisi: '))
analisi1 =patologia_dt1(float(input('Inserisci valore glicata: ')),int(input('Inserisci valore mmol: ')),int(input('Inserisci valore ck: ')),input('Inserisci data del prelievo: '))
"""
# nuovo2 = analisi_ematiche.has_data1('2022/10/23')
# if nuovo2 is None:
#    print('Data non trovata')
# else:
#    print(nuovo2)
#
# valore3 = analisi_ematiche.ck_uguali(540)
# for v in valore3:
#    print(str.v)
# try:
#     nuovo1 = analisi_ematiche.has_data('2021/10/21')
#     print(nuovo1)
#
# except ValueError:
#    print(f'Data non valida o non trovata')
# try:
#     valore = analisi_ematiche.find_data('2020/09/21')
#     for t in valore:
#         print(t)
#
# except ValueError:
#     print(f'Data inserita non valida o non esistente')
#analisi_ematiche.ck_alto()
#migliorato = analisi_ematiche.crea_ordinato_per_data()
#analisi_ematiche.append(patologia_dt1(9.0, 59, 690, '2024/11/30'))
#print('Analisi iniziali')
#analisi_ematiche.stampa()

#print('Analisi modificate')
#migliorato.stampa()
#print(migliorato.val_min_glicata())
#analisi_ematiche.ordina_per_data()
# analisi_rimaste = analisi_ematiche.cancella_valori_analisi_ck(190)
# for t in analisi_rimaste:
#     print(t)
# analisi = analisi_ematiche.valore_nullo_ck()
# if analisi == None:
#     print('Non ci sono valori del CK nulli')

# ck = input("Se vuoi avere la media del CK delle tue analisi inserite premi c: ")
# if ck == 'c':
#    print(f'La media del tuo CK è {analisi_ematiche.media_ck():f}')

# array = array.array("d",(1.5,4.5,7.9,0.9))
# print(array[1])
# analisi3 = analisi_ematiche.cancella_valori_analisi_ck(200)
# for v in analisi3:
# #     print(v)
# analisi4 = analisi_ematiche.ck_uguali(540)
# for g in analisi4:
#     print(g)
# ass = frozenset('12395897410099999999')
# ass1 = set('1254')
# print(ass, ass1)
# cnt = collections.Counter('11111122335999999lalessandro55556669555887799999999')
# print(cnt.total())
# print(list(cnt))
# print(set(cnt))
# print(dict(cnt))
# print(cnt.items())
# print(cnt.values())
#lezione l9 minuti 10:08
# a = (cnt.most_common())
# print(a)
# for v in a:
#     if v[1] > 10:
#        print(f'il {v[0]} è ripetuto {v[1]} volte')
# # p = collections.Counter(a)
# # print(p)

# ris = collections.Counter(analisi_ematiche.ck_alto())
# # print(ris)
# for v in ris:
#     print(f'Ho rilevato {ris[v]} valori con un ck {v}')
# analisi_ematiche.conta_valori_ck()
# # analisi_ematiche.ordina_per_data()
# # analisi_ematiche.stampa()
# val = (analisi_ematiche.conta_valori_ck())
# val1 = analisi_ematiche.crea_ordinato_per_data()
# val1.stampa()
# analisi_ematiche.ordina_per_parametri('mmol')
# ris = analisi_ematiche.media_e_valore_sqm_mmol()
# print(ris)
# analisi_ematiche.ordina_per_parametri('glicata')
# ris1 = analisi_ematiche.media_e_valore_sqm_glicata()
# print(ris1)
ris3 = analisi_ematiche.calcolo_coefficiente_variazione()
print(ris3)
