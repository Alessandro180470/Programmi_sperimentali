from view import View
from patologia_diabete1 import calcolo_valore
from T1 import patologia_dt1


class Controller(object):
    def __init__(self,view: View):
        self._view = view
        self._model = calcolo_valore()
        self.startupcalcolo_valore()








    def startupcalcolo_valore(self):
        self._model.append(patologia_dt1(6.4, 40, 0.12, 87, 220, '2024/09/26'))
        self._model.append(patologia_dt1(7.0, 53, 0.3, 128, 560, '2023/02/28'))
        self._model.append(patologia_dt1(7.1, 55, 0.5, 165, 540, '2022/10/21'))
        self._model.append(patologia_dt1(7.4, 53, 0.66, 160, 250, '2023/09/30'))
        self._model.append(patologia_dt1(6.4, 48, 0.66, 185, 366, '2024/09/30'))
        self._model.append(patologia_dt1(6.9, 49, 0.1, 195, 120, '2017/11/29'))
        self._model.append(patologia_dt1(7.0, 49, 0.25, 240, 220, '2021/10/23'))







