import tkinter as tk
from tkinter import messagebox
import csv

def calculeaza_cost():
    try:
        nr_piese = int(entry_piese.get())
        cost_material = float(entry_material.get())
        cost_manopera = float(entry_manopera.get())
        profit_percent = float(entry_profit.get())

        cost_total_fara_profit = nr_piese * (cost_material + cost_manopera)
        cost_total_cu_profit = cost_total_fara_profit * (1 + profit_percent / 100)
        cost_per_bucata = cost_total_cu_profit / nr_piese

        rezultat.config(
            text=f"Cost total: {cost_total_cu_profit:.2f} lei\n"
                 f"Preț pe bucată: {cost_per_bucata:.2f} lei"
        )

        # Salvare automată în CSV
        with open("cost_productie.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Nr Piese", "Cost Total", "Preț/Bucată"])
            writer.writerow([nr_piese, f"{cost_total_cu_profit:.2f}", f"{cost_per_bucata:.2f}"])

    except ValueError:
        messagebox.showerror("Eroare", "Completează toate câmpurile cu valori numerice!")

# Fereastra principală
root = tk.Tk()
root.title("Calculator Cost Producție")

# Etichete și câmpuri input
tk.Label(root, text="Număr piese:").grid(row=0, column=0, sticky="e")
tk.Label(root, text="Cost material/piesă:").grid(row=1, column=0, sticky="e")
tk.Label(root, text="Cost manoperă/piesă:").grid(row=2, column=0, sticky="e")
tk.Label(root, text="Profit dorit (%):").grid(row=3, column=0, sticky="e")

entry_piese = tk.Entry(root)
entry_material = tk.Entry(root)
entry_manopera = tk.Entry(root)
entry_profit = tk.Entry(root)

entry_piese.grid(row=0, column=1)
entry_material.grid(row=1, column=1)
entry_manopera.grid(row=2, column=1)
entry_profit.grid(row=3, column=1)

# Buton de calcul
tk.Button(root, text="Calculează", command=calculeaza_cost).grid(row=4, column=0, columnspan=2, pady=10)

# Etichetă pentru rezultat
rezultat = tk.Label(root, text="")
rezultat.grid(row=5, column=0, columnspan=2)

root.mainloop()
