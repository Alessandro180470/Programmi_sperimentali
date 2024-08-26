class libro:
    def __init__(self,cap1,cap2,cap3):

        self.cap1 = cap1
        self.cap2 = cap2
        self.cap3 = cap3
        self._voltage = 12
    def __str__(self):
        return f'{self.cap2} {self.cap3} {self.cap1}'
    def __repr__(self):
        return f"libro('{self.cap2}' '{self.cap3}' '{self.cap1}')"
    @property
    def voltage(self):
        return self._voltage
    @voltage.setter
    def voltage(self,volts):
        print('Warning:this can cause problem')
        self._voltage = volts
    def __add__(self, stringa2):
        return self.cap1 + stringa2
class num_pagine:
    def __init__(self,pag_geografia,pag_storia,pag_matematica):
        self.pag_geografia = pag_geografia
        self.pag_storia = pag_storia
        self.pag_matematica = pag_matematica
        if self.pag_storia > 999:
            raise ValueError(f'Numero pagine non consentito hai superato il limite di pagine => 999')


arg1 = num_pagine(int(input(f'inserisci numero pagine di geografia: ')), int(input('inserisci il numero di pagine di storia: ')),int(input('inserisci il numero di pagine di  mat: ')))
argomento1 = libro("geografia","storia","matematica")
inserimento1 = str('ciao')

#print(argomento1.__repr__())
#print(argomento1.__str__())
#print(f'il numero di pagine di {argomento1.cap1} è {arg1.pag_geografia}')
print(f'Totale pagine è: {arg1.pag_geografia+arg1.pag_storia+arg1.pag_matematica}')
print(argomento1.cap1,arg1.pag_matematica,argomento1.cap3)
print(type(arg1.pag_geografia))
print(f'{argomento1._voltage} volt')
print(arg1.__class__)
print(inserimento1+' Alessandro')
