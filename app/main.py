import tkinter as tk
from tkinter import Entry, Listbox, Scrollbar, ttk
from functools import partial
import tkinter
from tkinter.constants import COMMAND
from typing import Text
import backend


        

class JobApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.title(self,'Job offers')
        tk.Tk.geometry(self,newGeometry='450x350')
        self._frame = None
        self.switch_frame(LoginPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class LoginPage(tk.Frame):
    @staticmethod
    def validateLogin(master, username, password):
        if username.get() == 'admin' and password.get() == '123456':
            master.switch_frame(MainPage)
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Login").pack(side="top", fill="x", pady=10)
        tk.Label(self, text="Username").pack(side="top", fill='x',pady=10)
        username = tk.StringVar()
        usernameEntry = ttk.Entry(self, textvariable=username).pack(side="top", fill='x', pady=10)
        tk.Label(self, text="Password").pack(side="top", fill='x',pady=10)
        password = tk.StringVar()
        passwordEntry = ttk.Entry(self, textvariable=password).pack(side="top", fill='x', pady=10)
        validateLogin = partial(self.validateLogin, master, username, password)
        tk.Button(self, text="Connect",
                  command=validateLogin).pack(side="top", fill='x', pady=10)

class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="ID job").grid(row=0,column=0, pady=10)
        id_emploi = tk.StringVar()
        id_emploiEntry = ttk.Entry(self,textvariable=id_emploi).grid(row=0,column=1, pady=10)
        tk.Label(self, text="Society").grid(row=0,column=2, pady=10)
        societe = tk.StringVar()
        societeEntry = ttk.Entry(self,textvariable=societe).grid(row=0,column=3, pady=10)
        tk.Label(self, text="Adress").grid(row=1,column=0, pady=10)
        adresse = tk.StringVar()
        adresseEntry = ttk.Entry(self,textvariable=adresse).grid(row=1,column=1, pady=10)
        tk.Label(self, text="E-mail").grid(row=1,column=2, pady=10)
        e_mail = tk.StringVar()
        e_mailEntry = ttk.Entry(self,textvariable=e_mail).grid(row=1,column=3, pady=10)
        tk.Label(self, text="Profile needed").grid(row=2,column=0, pady=10)
        profil = tk.StringVar()
        profilEntry = ttk.Entry(self,textvariable=profil).grid(row=2,column=1, pady=10)
        tk.Label(self, text="Mission").grid(row=2,column=2, pady=10)
        mission = tk.StringVar()
        missionEntry = ttk.Entry(self,textvariable=mission).grid(row=2,column=3, pady=10)

        scroll_bar = tkinter.Scrollbar(self)
        scroll_bar.grid(row=3, column=2, rowspan=6, pady=10)

        list_jobs = tkinter.Listbox(self, height=6, width=35)
        list_jobs.grid(row=3,column=0,rowspan=6,columnspan=2, pady=10)
        list_jobs.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.configure(command=list_jobs.yview)
        def view_command():
            list_jobs.delete(0,len(backend.view()))
            for i,row in enumerate(backend.view()):
                list_jobs.insert(i,row)
        def add_command():
            backend.insert(id_emploi.get(), societe.get(), adresse.get(), e_mail.get(), profil.get(), mission.get())
            list_jobs.delete(0,len(backend.view()))
            for i,row in enumerate(backend.view()):
                list_jobs.insert(i,row)
        def delete_command():
            backend.delete(id_emploi.get())
            list_jobs.delete(0,len(backend.view()))
            for i,row in enumerate(backend.view()):
                list_jobs.insert(i,row)
        def update_command():
            backend.update(id_emploi.get(), societe.get(), adresse.get(), e_mail.get(), profil.get(), mission.get())
            list_jobs.delete(0,len(backend.view()))
            for i,row in enumerate(backend.view()):
                list_jobs.insert(i,row)
        button_view = ttk.Button(self, text="View all", width=12, command=view_command).grid(row=3, column=3, pady=10)
        button_add = ttk.Button(self, text="Add job", width=12, command=add_command).grid(row=4, column=3, pady=10)
        button_update = ttk.Button(self, text="Update offer", width=12, command=update_command).grid(row=5, column=3, pady=10)
        button_delete = ttk.Button(self, text="Delete offer", width=12, command=delete_command).grid(row=6,column=3, pady=10)
        button_quit = ttk.Button(self, text="Quit", command=lambda: master.switch_frame(LoginPage), width=12).grid(row=7,column=3, pady=10)


        # tk.Button(self, text="Logout",
        #           command=lambda: master.switch_frame(LoginPage)).pack()

# class PageTwo(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
#         tk.Button(self, text="Return to start page",
#                   command=lambda: master.switch_frame(LoginPage)).pack()

if __name__ == "__main__":
    app = JobApp()
    app.mainloop()