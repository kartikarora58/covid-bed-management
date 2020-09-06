# treeview scrollbars using tkinter

from tkinter import ttk
import tkinter as tk
from db import *


def display():
    db = DB()
    data = db.retrieve_data()
    records = [item['hospital_details'] for item in data]
    window = tk.Tk()
    window.resizable(width=1, height=1)

    # Using treeview widget
    treev = ttk.Treeview(window, selectmode='browse')

    # Calling pack method w.r.to treeview
    treev.pack()

    # Constructing vertical scrollbar
    # with treeview
    verscrlbar = ttk.Scrollbar(window,
                               orient="vertical",
                               command=treev.yview)

    # Calling pack method w.r.to verical
    # scrollbar
    verscrlbar.pack(fill='x')

    # Configuring treeview
    treev.configure(xscrollcommand=verscrlbar.set)

    # Defining number of columns
    treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")

    # Defining heading
    treev['show'] = 'headings'

    # Assigning the width and anchor to  the
    # respective columns
    treev.column("1", width=90)
    treev.column("2", width=90)
    treev.column("3", width=90)
    treev.column("4", width=90)
    treev.column("5", width=120)
    treev.column("6", width=120)
    treev.column("7", width=120)
    treev.column("8", width=120)
    treev.column("9", width=120)

    # Assigning the heading names to the
    # respective columns
    treev.heading("1", text="Name")
    treev.heading("2", text="address")
    treev.heading("3", text="phone")
    treev.heading("4", text="Hospital Type")
    treev.heading("5", text="Total Oxygen Beds")
    treev.heading("6", text="Vacant Oxygen Beds")
    treev.heading("7", text="Total Ventilators")
    treev.heading("8", text="Vacant Ventilators")
    treev.heading("9", text="Last Updated")

    # Inserting the items and their features to the
    # columns built
    for item in records:
        treev.insert("", 'end',
                     values=(
                         item['hospital_name'], item['hospital_address'], item['hospital_phone'], item['hospital_type'],
                         item['oxygen_count'],
                         item['vacant_oxygen'], item['ventilator_count'], item['vacant_ventilator'],
                         item['timestamp']))

    # Calling mainloop
    window.mainloop()
