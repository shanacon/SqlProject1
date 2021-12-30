import tkinter as tk
from Event import *
import MySQLdb
class ManageUser: 
    def __init__(self, window, BtnFont, EntryFont):
        self.ManagePanel = tk.Toplevel(window)
        self.ManagePanel.geometry('600x500')
        self.UserList = GetAllUser()
        count = 0
        for user in self.UserList :
            newBtn = tk.Button(self.ManagePanel, text = user, bg = "antique white", width = '10', height = '1', font = BtnFont)
            newBtn.config(command = lambda user = user :self.OpenUser(user))
            newBtn.place(x = 0, y = 0 + count * 50)
            count += 1
        self.CanSelect = tk.BooleanVar()
        self.CanSelect_Box = tk.Checkbutton(self.ManagePanel, text='Can Search', var = self.CanSelect, font = EntryFont)
        self.CanInsert = tk.BooleanVar()
        self.CanInsert_Box = tk.Checkbutton(self.ManagePanel, text='Can Add Tag', var = self.CanInsert, font = EntryFont)
        self.CanDelete = tk.BooleanVar()
        self.CanDelete_Box = tk.Checkbutton(self.ManagePanel, text='Can Delete Tag', var = self.CanDelete, font = EntryFont)
        ###
        self.SaveBtn = tk.Button(self.ManagePanel, text = "Save", bg = "antique white", width = '10', height = '1', font = BtnFont)
        self.SaveBtn.config(command = lambda:self._Save())
        self.SelectUser = None
    def OpenUser(self, user):
        grants = GetGrant(user)
        self.ShowUI(grants)
        self.SelectUser = user
    def ShowUI(self, grants) :
        self.CanSelect_Box.place(x= 300, y = 0)
        self.CanInsert_Box.place(x= 300, y = 100)
        self.CanDelete_Box.place(x= 300, y = 200)
        self.SaveBtn.place(x = 400, y = 300)
        if grants[0]:
            self.CanSelect.set(True)
        else :
            self.CanSelect.set(False)
        if grants[1]:
            self.CanInsert.set(True)
        else :
            self.CanInsert.set(False)
        if grants[2]:
            self.CanDelete.set(True)
        else :
            self.CanDelete.set(False)
    def _Save(self):
        grants = [self.CanSelect.get(), self.CanInsert.get(), self.CanDelete.get()]
        Save(self.SelectUser, grants)