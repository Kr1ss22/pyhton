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

# Rakenduse peamine klass
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Teenusepõhise Arveldussüsteem')
        self.geometry('600x400')
        self.create_widgets()

    def create_widgets(self):
        # Stiilide seadistamine
        self.style = ttk.Style(self)
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TButton', background='#e1e1e1', font=('Arial', 10))
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))

        # Peamenüü nuppude loomine
        main_frame = ttk.Frame(self, padding="10 10 10 10")
        main_frame.pack(expand=True, fill='both')

        ttk.Button(main_frame, text="Halda Teenuseid", command=self.manage_services).pack(pady=10, fill='x')
        ttk.Button(main_frame, text="Koosta Arve", command=self.create_invoice).pack(pady=10, fill='x')
        ttk.Button(main_frame, text="Vaata Arveid", command=self.view_invoices).pack(pady=10, fill='x')

    # Teenuste haldamise akna loomine
    def manage_services(self):
        # Akna seadistused
        self.service_window = tk.Toplevel(self, bg='#f0f0f0')
        self.service_window.title("Teenuste Haldamine")
        self.service_window.geometry('400x300')
        self.refresh_services_list()

    # Teenuste nimekirja värskendamine
    def refresh_services_list(self):
        for widget in self.service_window.winfo_children():
            widget.destroy()

        global services
        services = load_data(services_file)
        service_list_frame = ttk.Frame(self.service_window, padding="10 10 10 10")
        service_list_frame.pack(expand=True, fill='both')

        for service in services:
            service_frame = ttk.Frame(service_list_frame)
            service_frame.pack(fill='x', padx=5, pady=5)
            ttk.Label(service_frame, text=f"{service['name']} - {service['price']}").pack(side='left')
            ttk.Button(service_frame, text="Kustuta", command=lambda srv=service: self.delete_service(srv)).pack(side='right')

        ttk.Button(self.service_window, text="Lisa uus teenus", command=self.add_service_ui).pack(pady=10)

    # Uue teenuse lisamise dialoogi kuvamine
    def add_service_ui(self):
        new_service_name = simpledialog.askstring("Uus Teenus", "Sisesta teenuse nimi:", parent=self)
        new_service_price = simpledialog.askstring("Uus Teenus", "Sisesta teenuse hind:", parent=self)
        if new_service_name and new_service_price:
            try:
                new_service_id = max([int(service['id']) for service in services]) + 1 if services else 1
                new_service = {'id': str(new_service_id), 'name': new_service_name, 'price': new_service_price}
                services.append(new_service)
                save_data(services_file, services, ['id', 'name', 'price'])
                messagebox.showinfo("Teenus lisatud", "Uus teenus on edukalt lisatud.", parent=self)
                self.refresh_services_list()
            except ValueError as e:
                messagebox.showerror("Viga", "Hind peab olema numbriline väärtus.", parent=self)
        else:
            messagebox.showwarning("Tühistatud", "Teenus ei lisatud, sisend oli tühi või operatsioon tühistati.", parent=self)

    # Teenuse kustutamise funktsioon
    def delete_service(self, service):
        global services
        services = [srv for srv in services if srv['id'] != service['id']]
        save_data(services_file, services, ['id', 'name', 'price'])
        self.refresh_services_list()
        messagebox.showinfo("Teenus kustutatud", "Teenus on edukalt kustutatud.", parent=self)

    # Arve koostamise akna loomine
    def create_invoice(self):
        # Akna seadistused
        self.invoice_window = tk.Toplevel(self, bg='#f0f0f0')
        self.invoice_window.title("Koosta Arve")
        self.invoice_window.geometry('400x300')

        invoice_frame = ttk.Frame(self.invoice_window, padding="10 10 10 10")
        invoice_frame.pack(expand=True, fill='both')

        ttk.Label(invoice_frame, text="Vali teenus:").pack()
        self.service_var = tk.StringVar()
        service_dropdown = ttk.Combobox(invoice_frame, textvariable=self.service_var)
        service_dropdown['values'] = [service['name'] for service in services]
        service_dropdown['state'] = 'readonly'  # Don't allow user to type a value
        service_dropdown.pack(pady=5)

        ttk.Label(invoice_frame, text="Kuupäev:").pack()
        self.date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        date_label = ttk.Label(invoice_frame, textvariable=self.date_var)
        date_label.pack(pady=5)

        ttk.Button(invoice_frame, text="Salvesta Arve", command=self.save_invoice).pack(pady=10)
        ttk.Button(invoice_frame, text="Sulge", command=self.invoice_window.destroy).pack()

    # Arve salvestamise funktsioon
    def save_invoice(self):
        selected_service = self.service_var.get()
        invoice_date = self.date_var.get()
        for service in services:
            if service['name'] == selected_service:
                new_invoice = {
                    'id': str(len(invoices) + 1),
                    'service': selected_service,
                    'date': invoice_date,
                    'amount': service['price']
                }
                invoices.append(new_invoice)
                save_data(invoices_file, invoices, ['id', 'service', 'date', 'amount'])
                messagebox.showinfo("Arve salvestatud", "Arve on edukalt salvestatud.", parent=self)
                self.invoice_window.destroy()
                return
        messagebox.showerror("Viga", "Valitud teenust ei leitud.", parent=self)

    # Arvete vaatamise akna loomine
    def view_invoices(self):
        self.invoice_view_window = tk.Toplevel(self, bg='#f0f0f0')
        self.invoice_view_window.title("Vaata Arveid")
        self.invoice_view_window.geometry('600x400')

        invoice_list_frame = ttk.Frame(self.invoice_view_window, padding="10 10 10 10")
        invoice_list_frame.pack(expand=True, fill='both')

        for invoice in invoices:
            ttk.Label(invoice_list_frame, text=f"Arve ID: {invoice['id']}, Teenus: {invoice['service']}, Kuupäev: {invoice['date']}, Summa: {invoice['amount']}").pack(pady=5)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
