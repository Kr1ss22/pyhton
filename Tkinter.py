import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import csv
from datetime import datetime

services_file = 'services.csv'
invoices_file = 'invoices.csv'

# Eeldame, et failides on päised juba olemas
def load_data(filename):
    data = []
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        open(filename, "w").close()  # Loob tühja faili, kui seda ei eksisteeri
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

        ttk.Button(self, text="Halda Teenuseid", command=self.manage_services).pack(pady=10)
        ttk.Button(self, text="Koosta Arve", command=self.create_invoice).pack(pady=10)
        ttk.Button(self, text="Vaata Arveid", command=self.view_invoices).pack(pady=10)

    def manage_services(self):
        self.service_window = tk.Toplevel(self)
        self.service_window.title("Teenuste Haldamine")
        self.service_window.geometry('400x300')
        self.refresh_services_list()

    def refresh_services_list(self):
        for widget in self.service_window.winfo_children():
            widget.destroy()
        
        global services
        services = load_data(services_file)  # Refresh the list by reloading data
        for service in services:
            ttk.Label(self.service_window, text=f"{service['name']} - {service['price']}").pack()
        
        ttk.Button(self.service_window, text="Lisa uus teenus", command=self.add_service_ui).pack()

    def add_service_ui(self):
        new_service_name = simpledialog.askstring("Uus Teenus", "Sisesta teenuse nimi:")
        new_service_price = simpledialog.askstring("Uus Teenus", "Sisesta teenuse hind:")
        if new_service_name and new_service_price:
            try:
                new_service_id = max([int(service['id']) for service in services]) + 1 if services else 1
                new_service = {'id': str(new_service_id), 'name': new_service_name, 'price': new_service_price}
                services.append(new_service)
                save_data(services_file, services, ['id', 'name', 'price'])
                messagebox.showinfo("Teenus lisatud", "Uus teenus on edukalt lisatud.")
                self.refresh_services_list()
            except ValueError as e:
                messagebox.showerror("Viga", "Hind peab olema numbriline väärtus.")
        else:
            messagebox.showwarning("Tühistatud", "Teenus ei lisatud, sisend oli tühi või operatsioon tühistati.")

    def create_invoice(self):
        # Define invoice creation UI here
        pass

    def view_invoices(self):
        # Define invoice viewing logic here
        pass

if __name__ == "__main__":
    app = Application()
    app.mainloop()
