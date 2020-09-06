from tkinter import *
from tkinter.ttk import *


class Hello:
    def run_app(self):
        root = Tk()
        self.hospital_type = StringVar()
        govt = Radiobutton(root, text="Government", value="govt", variable=self.hospital_type)
        private = Radiobutton(root, text="Private", value="private", variable=self.hospital_type)
        govt.grid(row=0, column=0, pady=2)
        private.grid(row=0, column=1, pady=2)
        btn = Button(root, text="click", command=self.on_click)
        btn.grid(row=1, column=0)
        root.mainloop()

    def on_click(self):
        print(self.hospital_type.get())


ob = Hello()
ob.run_app()
#
# # import datetime
# # x=datetime.datetime.now()
# # print(x)
# # xt=x.strftime("%d")+"-"+x.strftime("%b")+","+x.strftime("%I")+":"+x.strftime("%M")+" "+x.strftime("%p")
# # print(xt,type(xt))

# print(ObjectId('5f534d77ad794844b2b30202'))
