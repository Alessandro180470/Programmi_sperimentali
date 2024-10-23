import flet as ft
class View(object):
    def __init__(self, page):
        self._page = page
        self._titolo = None


    def caricaInterfaccia(self):
       self._titolo = ft.Text("Patologia Diabete T1", color="blue",size=24)
       # Row1
       self.txtIn = ft.TextField(label="Nome",width=200)
       glicata: float
       mmol: int
       creatinina: float
       colesterolo: int
       ck: int
       data: str





       self._page.add(self._titolo)


    def setController(self,controller):
        self._controller = controller


