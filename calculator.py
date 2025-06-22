import tkinter as tk
from tkinter import messagebox
import csv

def calculeaza_cost():
    try:
        nr_piese = int(entry_nr_piese.get())
        cost_materiale = float(entry_cost_materiale.get())
        cost_manopera = float(entry_cost_manopera.get())
        procent_profit = float(entry_procent_profit.get())

        cost_total = cost_materiale + cost_manopera
        pret_bucata = cost_total * (1 + procent_profit / 100)

        label_rezultat.config(text=f"Cost total: {cost_total:.2f} lei\nPreț/bucată: {pret_bucata:.2f} lei")

        with open('cost_productie.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([nr_piese, cost_materiale, cost_manopera, procent_profit, cost_total, pret_bucata])

    except ValueError:
        messagebox.showerror("Eroare", "Te rog introdu valori corecte.")

root = tk.Tk()
root.title("Calculator Cost Producție")

tk.Label(root, text="Număr piese:").grid(row=0, column=0)
entry_nr_piese = tk.Entry(root)
entry_nr_piese.grid(row=0, column=1)

tk.Label(root, text="Cost materiale (lei):").grid(row=1, column=0)
entry_cost_materiale = tk.Entry(root)
entry_cost_materiale.grid(row=1, column=1)

tk.Label(root, text="Cost manoperă (lei):").grid(row=2, column=0)
entry_cost_manopera = tk.Entry(root)
entry_cost_manopera.grid(row=2, column=1)

tk.Label(root, text="Procent profit (%):").grid(row=3, column=0)
entry_procent_profit = tk.Entry(root)
entry_procent_profit.grid(row=3, column=1)

btn_calc = tk.Button(root, text="Calculează", command=calculeaza_cost)
btn_calc.grid(row=4, column=0, columnspan=2)

label_rezultat = tk.Label(root, text="")
label_rezultat.grid(row=5, column=0, columnspan=2)

root.mainloop()
