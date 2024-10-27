import flet as ft
class View(object):
    def __init__(self, page):
        self._page = page
        self._titolo = None


    def caricaInterfaccia(self):
       self._titolo = ft.Text("Patologia Diabete T1", color="blue",size=24)

       # Row1
       self.txtIn = ft.TextField(label="Glicata",width=100)
       self.txtMOLL = ft.TextField(label="MOLL",width=100)
       self.txtCreatinina = ft.TextField(label="Creatinina", width=110)
       self.txtColesterolo = ft.TextField(label="Colesterolo", width=110)
       self.txtCk = ft.TextField(label="Ck", width=105)
       self.ddData = ft.Dropdown(options=[ft.dropdown.Option("Opzione1"),ft.dropdown.Option("Opzione2")],label="Data",width=100)


       row1 = ft.Row([self.txtIn,self.txtMOLL,self.txtCreatinina,self.txtColesterolo,self.txtCk,self.ddData])

       glicata: float
       mmol: int
       creatinina: float
       colesterolo: int
       ck: int
       data: str





       self._page.add(self._titolo,row1)


    def setController(self,controller):
        self._controller = controller


