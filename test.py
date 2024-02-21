import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import csv
from datetime import datetime

# Andmefailid
services_file = 'services.csv'
invoices_file = 'invoices.csv'

# Andmete laadimine ja salvestamine
def load_data(filename):
    data = []
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        open(filename, "w").close()
    return data

def save_data(filename, data, fieldnames):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

services = load_data(services_file)
invoices = load_data(invoices_file)

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Teenusepõhise Arveldussüsteem')
        self.geometry('600x400')
        self.create_widgets()

    def create_widgets(self):
        self.style = ttk.Style(self)
        self.style.configure('TFrame', background='#fefefe')
        self.style.configure('TButton', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TLabel', background='#fefefe', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'))

        main_frame = ttk.Frame(self, padding="30 30 30 30")
        main_frame.pack(expand=True, fill='both')

        header_label = ttk.Label(main_frame, text="Teenusepõhise Arveldussüsteem", style='Header.TLabel')
        header_label.pack(pady=10)

        ttk.Button(main_frame, text="Halda Teenuseid", command=self.manage_services).pack(pady=10, fill='x')
        ttk.Button(main_frame, text="Koosta Arve", command=self.create_invoice).pack(pady=10, fill='x')
        ttk.Button(main_frame, text="Vaata Arveid", command=self.view_invoices).pack(pady=10, fill='x')

    # Järgnevad meetodid (manage_services, refresh_services_list, add_service_ui, delete_service, create_invoice, save_invoice, view_invoices) jäävad samaks nagu eelmises näites.

if __name__ == "__main__":
    app = Application()
    app.mainloop()
