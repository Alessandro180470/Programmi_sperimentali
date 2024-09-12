from patologia_diabete1 import calcolo_valore, patologia_dt1

analisi_ematiche = calcolo_valore()
analisi1 = patologia_dt1(6.3,56,320,'2020/10/21')
analisi_ematiche.append(analisi1)
analisi_ematiche.append(patologia_dt1(6.3,55,320,'2020/09/21'))
analisi_ematiche.append(patologia_dt1(6.8,52,560,'2021/10/21'))
analisi_ematiche.append(patologia_dt1(6.7,51,54,'2022/10/21'))
analisi_ematiche.append(patologia_dt1(6.9,55,325,'2023/09/06'))
analisi_ematiche.append(patologia_dt1(7.0,55,120,'2023/11/29'))
analisi_ematiche.append(patologia_dt1(6.1,39,220,'2024/10/23'))
#analisi_ematiche.append(patologia_dt1(float(input('Iserisci v gli')),int(input('ins val m')),int(input('ins v ck')),input('inserisci data')))

"""

analisi = patologia_dt1(float(input('Inserisci valore glicata: ')), float(input('Inserisci valore mmol: ')),
                float(input('Inserisci valore ck: ')), input('Inserisci la data delle analisi: '))
analisi1 =patologia_dt1(float(input('Inserisci valore glicata: ')),int(input('Inserisci valore mmol: ')),int(input('Inserisci valore ck: ')),input('Inserisci data del prelievo: '))
"""
nuovo2 = analisi_ematiche.has_data1('2022/10/23')
if nuovo2 is None:
   print('Data non trovata')
else:
   print(nuovo2)

valore3 = analisi_ematiche.ck_uguali(540)
for v in valore3:
   print(str.v)
try:
    nuovo1 = analisi_ematiche.has_data('2022/10/23')

except ValueError:
   print(f'Data non valida o non trovata')
try:
    valore = analisi_ematiche.find_data('2022/10/23')
    for t in valore:
        print(t.ck,t.glicata)

except ValueError:
    print(f'Data inserita non valida o non esistente')





