from patologia_diabete1 import calcolo_valore, patologia_dt1

analisi_ematiche = calcolo_valore()
analisi1 = patologia_dt1(6.3,56,320,'2024/05/05')
analisi_ematiche.append(analisi1)
analisi_ematiche.append(patologia_dt1(6.1,51,540,'2024/05/21'))
analisi_ematiche.append(patologia_dt1(6.8,49,320,'2024/05/23'))
print(f'Il valore medio del ck è :{analisi_ematiche.media_ck()},mentre quello della glicata è :{analisi_ematiche.media_glicata()}')
print(f'Il valore MAX e MIN della glicata sono: MAX {analisi_ematiche.val_max_glicata()} e MIN {analisi_ematiche.val_min_glicata()}')

# analisi = patologia_dt1(float(input('Inserisci valore glicata: ')), float(input('Inserisci valore mmol: ')),
#                float(input('Inserisci valore ck: ')), input('Inserisci la data delle analisi: '))
# analisi1 =patologia_dt1(float(input('Inserisci valore glicata: ')),int(input('Inserisci valore mmol: ')),int(input('Inserisci valore ck: ')),input('Inserisci data del prelievo: '))

