
import tkinter as tk
from tkinter import messagebox
def calcola_colesterolo():
     try:
          # Ottieni i valori inseriti dall'utente
          ldl = float(entry_ldl.get())
          hdl = float(entry_hdl.get())
          trigliceridi = float(entry_trigliceridi.get())

          # Calcola il colesterolo totale
          colesterolo_totale = ldl -( hdl + (trigliceridi / 5))
         # col_t - (col_c + (trigliceridi / 5))
          # Mostra il risultato
          messagebox.showinfo("Risultato", f"Colesterolo Totale: {colesterolo_totale:.2f} mg/dL")
     except ValueError:
          messagebox.showerror("Errore", "Per favore, inserisci valori numerici validi.")


# Crea la finestra principale
root = tk.Tk()
root.title("Calcolatore di Colesterolo")

# Crea le etichette e le caselle di input
tk.Label(root, text="LDL (mg/dL):").grid(row=0, column=0, padx=10, pady=10)
entry_ldl = tk.Entry(root)
entry_ldl.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="HDL (mg/dL):").grid(row=1, column=0, padx=10, pady=10)
entry_hdl = tk.Entry(root)
entry_hdl.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Trigliceridi (mg/dL):").grid(row=2, column=0, padx=10, pady=10)
entry_trigliceridi = tk.Entry(root)
entry_trigliceridi.grid(row=2, column=1, padx=10, pady=10)

# Crea il pulsante per calcolare
button_calcola = tk.Button(root, text="Calcola Colesterolo", command=calcola_colesterolo)
button_calcola.grid(row=3, columnspan=2, pady=20)

root.mainloop()