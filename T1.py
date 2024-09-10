from patologia_diabete1 import calcolo_valore, patologia_dt1

analisi_ematiche = calcolo_valore()
analisi1 = patologia_dt1(6.3,56,320,'2020/10/21')
analisi_ematiche.append(analisi1)
analisi_ematiche.append(patologia_dt1(6.3,55,320,'2022/09/21'))
analisi_ematiche.append(patologia_dt1(6.8,52,560,'2024/10/21'))
analisi_ematiche.append(patologia_dt1(6.7,51,54,'2023/10/21'))
analisi_ematiche.append(patologia_dt1(6.9,55,325,'2024/09/06'))
analisi_ematiche.append(patologia_dt1(6.7,55,120,'2023/11/29'))
#analisi_ematiche.append(patologia_dt1(float(input('Iserisci v gli')),int(input('ins val m')),int(input('ins v ck')),input('inserisci data')))

"""

analisi = patologia_dt1(float(input('Inserisci valore glicata: ')), float(input('Inserisci valore mmol: ')),
                float(input('Inserisci valore ck: ')), input('Inserisci la data delle analisi: '))
analisi1 =patologia_dt1(float(input('Inserisci valore glicata: ')),int(input('Inserisci valore mmol: ')),int(input('Inserisci valore ck: ')),input('Inserisci data del prelievo: '))
"""
try:
   valore2 = analisi_ematiche.trova_corrispondenza_ck_glicata(320,6.3,'2022/09/21')
   for v in valore2:
      print(v)
except ValueError:
   print(f'Valori non corrispondenti ')
valore3 = analisi_ematiche.ck_uguali(540)

try:
   nuovo1 = analisi_ematiche.has_data('2024/09/06')
except ValueError:
   print(f'Data non valida o non trovata')


nuovo2 = analisi_ematiche.has_data1('2024/10/21')
if nuovo2 is None:
   print('Data non trovata')
else:
   print(nuovo2)


