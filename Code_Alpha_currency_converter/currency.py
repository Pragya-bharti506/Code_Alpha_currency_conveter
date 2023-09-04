import tkinter as tk
from tkinter import ttk
import requests

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        
        self.root.geometry("400x300") 
        self.root.configure(bg="#458B74")

        self.frame = ttk.Frame(root)
        self.frame.pack(expand=True)

        self.from_currency_label = ttk.Label(self.frame, text="From Currency:", font=("Arial", 12))
        self.from_currency_label.pack()

        self.from_currency_combobox = ttk.Combobox(self.frame, values=["USD", "EUR", "GBP", "JPY" , "INR"], font=("Arial", 12))
        self.from_currency_combobox.pack()

        self.amount_label = ttk.Label(self.frame, text="Enter Amount:", font=("Arial", 12))
        self.amount_label.pack()

        self.amount_entry = ttk.Entry(self.frame, font=("Arial", 12))
        self.amount_entry.pack()

        self.to_currency_label = ttk.Label(self.frame, text="To Currency:", font=("Arial", 12))
        self.to_currency_label.pack()

        self.to_currency_combobox = ttk.Combobox(self.frame, values=["USD", "EUR", "GBP", "JPY" , "INR"], font=("Arial", 12))
        self.to_currency_combobox.pack()

        self.convert_button = ttk.Button(self.frame, text="Convert", command=self.convert_currency, style="C.TButton")
        self.convert_button.pack()

        self.result_label = ttk.Label(self.frame, text="", font=("Arial", 14, "bold"), foreground="green")
        self.result_label.pack()

        self.style = ttk.Style()
        self.style.configure("C.TButton", font=("Arial", 12), foreground="black", background="blue")
        

    def convert_currency(self):
        amount = float(self.amount_entry.get())
        from_currency = self.from_currency_combobox.get()
        to_currency = self.to_currency_combobox.get()

        url = f" https://v6.exchangerate-api.com/v6/b87aeb98b088135e362605c6/latest/{from_currency}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if 'conversion_rates' in data:
                conversion_rates = data['conversion_rates']
                if to_currency in conversion_rates:
                    exchange_rate = conversion_rates[to_currency]
                    converted_amount = amount * exchange_rate
                    self.result_label.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
                else:
                    self.result_label.config(text=f"Invalid 'To Currency'")
            else:
                self.result_label.config(text="Invalid API response")
        else:
            self.result_label.config(text="Error fetching data")




if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
