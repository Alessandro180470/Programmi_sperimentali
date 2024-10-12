import flet as ft
def main(page: ft.Page):
    def addCheckbox(e):
        strToAdd = txtIn.value
        txtIn.value = ""
        if strToAdd == "":#serve se si clicca a vuoto non fa nulla
            return

        page.add(ft.Checkbox(label=strToAdd))
    # Row1
    txtIn = ft.TextField(label="Agiungi un elemento.")
    btnAdd = ft.ElevatedButton(text="Add",on_click=addCheckbox)
    row1 = ft.Row([txtIn,btnAdd],alignment=ft.MainAxisAlignment.CENTER)

    page.add(row1)

ft.app(target=main, view=ft.AppView.FLET_APP)

