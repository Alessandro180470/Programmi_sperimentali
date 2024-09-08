from patologia_diabete1 import calcolo_valore, patologia_dt1

analisi_ematiche = calcolo_valore()
analisi1 = patologia_dt1(6.3,56,320,'2020/10/21')
analisi_ematiche.append(analisi1)
analisi_ematiche.append(patologia_dt1(6.3,55,320,'2022/09/21'))
analisi_ematiche.append(patologia_dt1(6.8,52,560,'2023/10/21'))
analisi_ematiche.append(patologia_dt1(6.7,51,540,'2021/10/21'))
analisi_ematiche.append(patologia_dt1(6.9,55,325,'2024/09/06'))
analisi_ematiche.append(patologia_dt1(6.7,55,540,'2023/11/29'))
print(f'Il valore medio del ck è :{analisi_ematiche.media_ck()},mentre quello della glicata è :{analisi_ematiche.media_glicata()}')
print(f'Il valore MAX e MIN della glicata sono: MAX {analisi_ematiche.val_max_glicata()} e MIN {analisi_ematiche.val_min_glicata()}')
valore1 = analisi_ematiche.ck_uguali(540)
for v in valore1:
   print(f'data delle analisi trovate con valore ck uguale: ({v.data}) con valore di ck :{v.ck} e glicata {v.glicata}')

"""

analisi = patologia_dt1(float(input('Inserisci valore glicata: ')), float(input('Inserisci valore mmol: ')),
                float(input('Inserisci valore ck: ')), input('Inserisci la data delle analisi: '))
analisi1 =patologia_dt1(float(input('Inserisci valore glicata: ')),int(input('Inserisci valore mmol: ')),int(input('Inserisci valore ck: ')),input('Inserisci data del prelievo: '))


"""
valore2 = analisi_ematiche.trova_corrispondenza_ck_glicata(320,6.3)
for v in valore2:
   print(v)
valore3 = analisi_ematiche.ck_uguali(540)





