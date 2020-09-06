from tkinter import *
from db import *
from tkinter.ttk import *
from tkinter import messagebox
import datetime
from tree_view import display


class Bed:
    def __init__(self):
        self.db = DB()
        self.title = "Covid-19 Bed Management System"
        self.error = None

    def run_app(self):
        window = Tk()
        window.geometry('600x400')
        window.title(self.title)
        self.login_btn = Button(window, text="Login", command=self.login)
        self.login_btn.grid(row=0, column=0)
        self.register_btn = Button(window, text="Register", command=self.register)
        self.register_btn.grid(row=0, column=1)
        self.show_data = Button(window, text="Show Hospital List", command=display)
        self.show_data.grid(row=0, column=2)
        window.mainloop()

    def register(self):
        window = Tk()
        window.geometry('400x150')
        window.title(self.title)
        email_label = Label(window, text="Email: ")
        email_label.grid(row=0, column=0)
        self.register_email = Entry(window, width=35)
        self.register_email.grid(row=0, column=1, pady=2)
        # Enter Password
        password_label = Label(window, text="Password: ")
        password_label.grid(row=1, column=0, pady=2)
        self.register_password = Entry(window, show="*", width=35)
        self.register_password.grid(row=1, column=1, pady=2)
        # confirm Password
        password_label = Label(window, text="Confirm Password: ")
        password_label.grid(row=2, column=0)
        self.register_password2 = Entry(window, show="*", width=35)
        self.register_password2.grid(row=2, column=1, pady=4)
        # Register Button
        register_btn = Button(window, text="Register", command=lambda: self.handle_register(window))
        register_btn.grid(row=4, column=1)
        window.mainloop()

    def login(self):
        window = Tk()
        window.geometry('300x100')
        window.title(self.title)
        email_label = Label(window, text="Email: ")
        email_label.grid(row=0, column=0)
        self.login_email = Entry(window, width=35)
        self.login_email.grid(row=0, column=1, pady=2)
        password_label = Label(window, text="Password: ")
        password_label.grid(row=1, column=0)
        self.login_password = Entry(window, show="*", width=35)
        self.login_password.grid(row=1, column=1, pady=2)
        login_btn = Button(window, text="Login", command=lambda: self.handle_login(window))
        login_btn.grid(row=2, column=1)
        window.mainloop()

    def handle_login(self, window):
        self.error = None
        if self.login_email == "":
            self.error = "Email can not be empty"
        if self.login_password == "":
            self.error = "Password can not be empty"
        if self.error is not None:
            messagebox.showerror(message=self.error)
        else:
            credentials = [self.login_email.get(), self.login_password.get()]
            user = self.db.retrieve_user(credentials)
            window.destroy()
            if not user:
                messagebox.showerror(message="User Doesn't exist. Please first register yourself")
            elif 'hospital_details' not in user[0]:
                self.add_hospital(id=user[0]['_id'])
            else:
                data = self.db.edit_hospital(user[0]['_id'])
                self.edit_hospital(id=user[0]['_id'], detail=data)
                # update existing hospital details

    def handle_register(self, window):
        self.error = None
        if self.register_email.get() == "":
            self.error = "Email is empty"
        if self.register_password.get() != self.register_password2.get():
            self.error = "Passwords donot match"
        if self.error is not None:
            messagebox.showerror(message=self.error)
        else:
            record = {'email': self.register_email.get(), 'password': self.register_password.get()}
            id = self.db.register_user(record)
            if id:
                window.destroy()
                self.add_hospital(id)

    def add_hospital(self, id):
        root = Tk()
        root.title(self.title)
        root.geometry('400x300')
        # Hospital Name
        hospital_label = Label(root, text="Hospital Name:")
        hospital_label.grid(row=0, column=0, pady=2)
        self.hospital_name = Entry(root, width=35)
        self.hospital_name.grid(row=0, column=1, pady=2)
        # Hospital address
        hospital_address = Label(root, text="Address:")
        hospital_address.grid(row=1, column=0, pady=2)
        self.hospital_address = Entry(root, width=35)
        self.hospital_address.grid(row=1, column=1, pady=2)
        # Hospital Phone Number
        hospital_phone = Label(root, text="Phone Number:")
        hospital_phone.grid(row=2, column=0, pady=2)
        self.hospital_phone = Entry(root, width=35)
        self.hospital_phone.grid(row=2, column=1, pady=2)
        # oxygen bed count
        oxygen_count = Label(root, text="Total oxygen beds:")
        oxygen_count.grid(row=3, column=0, pady=2)
        self.oxygen_count = Entry(root, width=35)
        self.oxygen_count.grid(row=3, column=1, pady=2)
        # vacant oxygen count
        vacant_oxygen = Label(root, text="Vacant Oxygen Beds:")
        vacant_oxygen.grid(row=4, column=0, pady=2)
        self.vacant_oxygen = Entry(root, width=35)
        self.vacant_oxygen.grid(row=4, column=1, pady=2)
        # total ventilator count
        ventilator_count = Label(root, text="Total Ventilators:")
        ventilator_count.grid(row=5, column=0, pady=2)
        self.ventilator_count = Entry(root, width=35)
        self.ventilator_count.grid(row=5, column=1, pady=2)
        # vacant ventilator
        vacant_ventilator = Label(root, text="Vacant Ventilators:")
        vacant_ventilator.grid(row=6, column=0, pady=2)
        self.vacant_ventilator = Entry(root, width=35)
        self.vacant_ventilator.grid(row=6, column=1, pady=2)
        # Select Hospital Type
        hospital_type = Label(root, text="Select Hospital Type:")
        hospital_type.grid(row=7, column=0, pady=2)
        self.hospital_type = StringVar()
        self.hospital_type.set("private")
        govt = Radiobutton(root, text="Government", value="govt", variable=self.hospital_type)
        private = Radiobutton(root, text="Private", value="private", variable=self.hospital_type)
        govt.grid(row=7, column=1, pady=2)
        private.grid(row=7, column=2, pady=2)
        # Submit button
        submit = Button(root, text="Submit", command=lambda: self.handle_add_hospital(auth_id=id, window=root))
        submit.grid(row=9, column=1, pady=6)
        root.mainloop()

    def handle_add_hospital(self, auth_id, window):
        self.error = None
        lst = [self.hospital_name, self.hospital_address, self.hospital_phone, self.oxygen_count,
               self.vacant_oxygen, self.ventilator_count, self.vacant_ventilator]
        for i in range(0, len(lst)):
            if lst[i].get() == "":
                self.error = "Please fill up all the fields"
                break
        if self.error is not None:
            messagebox.showerror(message=self.error)
        else:
            x = datetime.datetime.now()
            timestamp = x.strftime("%d") + "-" + x.strftime("%b") + "," + x.strftime("%I") + ":" + x.strftime(
                "%M") + " " + x.strftime("%p")
            detail = {'hospital_name': self.hospital_name.get(),
                      'hospital_address': self.hospital_address.get(),
                      'hospital_phone': self.hospital_phone.get(),
                      'oxygen_count': self.oxygen_count.get(),
                      'vacant_oxygen': self.vacant_oxygen.get(),
                      'ventilator_count': self.ventilator_count.get(),
                      'vacant_ventilator': self.vacant_ventilator.get(),
                      'hospital_type': self.hospital_type.get(),
                      'timestamp': timestamp}

            print(auth_id, detail)
            self.db.save_hospital(id=auth_id, data=detail)
            window.destroy()
            messagebox.showinfo(message="Registration Successful")
            display()

    def edit_hospital(self, id, detail):
        root = Tk()
        root.title(self.title)
        root.geometry('400x200')
        # Total oxygen beds
        total_oxygen = Label(root, text="Total Oxygen Beds")
        total_oxygen.grid(row=0, column=0)
        self.edit_total_oxygen = Entry(root, width=35)
        self.edit_total_oxygen.insert(0, string=detail['oxygen_count'])
        self.edit_total_oxygen.grid(row=0, column=1, pady=2)
        # Vacant Oxygen Beds
        vacant_oxygen = Label(root, text="Vacant Oxygen Beds")
        vacant_oxygen.grid(row=1, column=0)
        self.edit_vacant_oxygen = Entry(root, width=35)
        self.edit_vacant_oxygen.insert(0, string=detail['vacant_oxygen'])
        self.edit_vacant_oxygen.grid(row=1, column=1, pady=2)
        # Total Ventilators
        total_ventilators = Label(root, text="Total Ventilators")
        total_ventilators.grid(row=2, column=0)
        self.edit_total_ventilators = Entry(root, width=35)
        self.edit_total_ventilators.insert(0, string=detail['ventilator_count'])
        self.edit_total_ventilators.grid(row=2, column=1, pady=2)
        # Vacant Ventilators
        vacant_ventilators = Label(root, text="Vacant Ventilators")
        vacant_ventilators.grid(row=3, column=0)
        self.edit_vacant_ventilators = Entry(root, width=35)
        self.edit_vacant_ventilators.insert(0, string=detail['vacant_ventilator'])
        self.edit_vacant_ventilators.grid(row=3, column=1, pady=2)
        update = Button(root, text="Update", command=lambda: self.update_hospital(id, detail,root))
        update.grid(row=4, column=1, pady=4)
        root.mainloop()

    def update_hospital(self, id, detail, root):
        detail['oxygen_count'] = self.edit_total_oxygen.get()
        detail['vacant_oxygen'] = self.edit_vacant_oxygen.get()
        detail['ventilator_count'] = self.edit_total_ventilators.get()
        detail['vacant_ventilator'] = self.edit_vacant_ventilators.get()
        x = datetime.datetime.now()
        timestamp = x.strftime("%d") + "-" + x.strftime("%b") + "," + x.strftime("%I") + ":" + x.strftime(
            "%M") + " " + x.strftime("%p")
        detail['timestamp'] = timestamp
        self.db.save_hospital(id, detail)
        root.destroy()
        messagebox.showinfo(message="Bed Details Updated")
        display()


if __name__ == '__main__':
    ob = Bed()
    ob.run_app()
