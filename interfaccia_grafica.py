from time import sleep

import flet as ft

def main(page: ft.Page):
    txtIn = ft.Text(value="Buongiorno Alessandro", color="blue")
    page.controls.append(txtIn)
    page.update()

    txtOut = ft.Text(value="Counter:", color="red",size=30)
    page.controls.append(txtOut)
    page.update()
    for i in range (1,100):
        txtOut.value = "Counter: " + str(i)
        if i == 10 :
            a = ft.Text(value=f"Sono passati {10} secondi",color="green",size=24)
            page.controls.append(a)
            page.update()


        txtOut.update()
        sleep(0.5)


ft.app(target=main, view=ft.AppView.FLET_APP)

