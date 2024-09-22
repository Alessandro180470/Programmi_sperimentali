import array

import patologia_diabete1
from patologia_diabete1 import calcolo_valore, patologia_dt1

analisi_ematiche = calcolo_valore()
analisi1 = patologia_dt1(6.3, 56, 0.22, 540, '2020/10/21')
analisi_ematiche.append(analisi1)
analisi_ematiche.append(patologia_dt1(6.3, 55, 0.12, 20, '2020/06/21'))
analisi_ematiche.append(patologia_dt1(6.8, 52, 0.3, 560, '2021/10/21'))
analisi_ematiche.append(patologia_dt1(6.7, 51, 0.5, 540, '2022/10/21'))
analisi_ematiche.append(patologia_dt1(6.9, 55, 0.66, 250, '2023/09/30'))

analisi_ematiche.append(patologia_dt1(7.0, 55, 0.1, 120, '2023/11/29'))
analisi_ematiche.append(patologia_dt1(7.3, 39, 0.25, 190, '2021/10/23'))

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
#     print(v)
analisi4 = analisi_ematiche.ck_uguali(540)
for g in analisi4:
    print(g)