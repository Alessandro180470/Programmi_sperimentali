import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('380x150')
window.iconbitmap(r"C:\Users\aless\Downloads\apple.ico")
def area_rettangolo():
    try:

        base = float(base1.get())
        altezza = float(altezza1.get())
        area = float(base * altezza)
        messagebox.showinfo('Risultato',f'area totale : {area} cm')
    except ValueError:
        messagebox.showerror("Errore", "Per favore, inserisci valori numerici validi.")
window.title("CALCOLO AREA RETTANGOLO")
tk.Label(text="Calcolo dell'area del rettangolo").grid(row=0,column=0)
tk.Label(text="base").grid(row=1,column=0,padx=10,pady=10)
base1 = tk.Entry(window)
base1.grid(row=1,column=1)
base1.focus()
tk.Label(text="altezza").grid(row=3,column=0,padx=10,pady=10)
altezza1 = tk.Entry(window)
altezza1.grid(row=3,column=1)

bottone = tk.Button(text="Calcola",command=area_rettangolo)
bottone.grid(row=5,column=2)

window.mainloop()