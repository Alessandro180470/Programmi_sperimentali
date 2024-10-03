from time import sleep

import flet as ft


def main(page: ft.Page):
    txtIn = ft.Text(value="Buongiorno Alessandro", color="blue", size=25)
    # page.controls.append(txtIn)
    # page.update() #equivalente a sotto
    page.add(txtIn)

    # txtOut = ft.Text(value="Counter:", color="red",size=30)
    # page.add(txtOut)

    # for i in range (1,100):
    #     txtOut.value = "Counter: " + str(i)
    #     if i == 10 :
    #         a = ft.Text(value=f"Sono passati {10} secondi",color="green",size=24)
    #         # page.controls.append(a)
    #         # page.update()
    #         page.add(a)

    # txtOut.update()
    # sleep(1)
    def handleBottone(e):
       txtOut.value = ""
       page.update()
       sleep(1)
       txtOut.value="Pulsante cliccato."
       page.update()

    txt1 = ft.Text(value="Colonna 1", color='red')
    txt2 = ft.Text(value="Colonna 2", color='blue')
    btn = ft.ElevatedButton(text="Premi qui!", on_click=handleBottone)

    row1 = ft.Row([txt1, txt2, btn])
    txtOut = ft.Text(value="", color="red", size=30)
    page.add(row1,txtOut)


ft.app(target=main, view=ft.AppView.FLET_APP)
