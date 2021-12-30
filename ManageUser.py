import tkinter as tk
from Event import *
import MySQLdb
class ManageUser:
    def __init__(self, window, BtnFont, EntryFont):
        ManagePanel = tk.Toplevel(window)
        ManagePanel.geometry('600x500')
        self.UserList = GetAllUser()
        count = 0
        for user in self.UserList :
            newBtn = tk.Button(ManagePanel, text = user, bg = "antique white", width = '10', height = '1', font = BtnFont)
            newBtn.config(command = lambda user = user :self.OpenUser(user))
            newBtn.place(x = 0, y = 0 + count * 50)
            count += 1
        CanSelect = tk.BooleanVar()
        CanSelect_Box = tk.Checkbutton(ManagePanel, text='Can Search', var = CanSelect, font = EntryFont)
        CanSelect_Box.place(x= 300, y = 0)
        CanInsert = tk.BooleanVar()
        CanInsert_Box = tk.Checkbutton(ManagePanel, text='Can Add Tag', var = CanInsert, font = EntryFont)
        CanInsert_Box.place(x= 300, y = 100)
        CanDelete = tk.BooleanVar()
        CanDelete_Box = tk.Checkbutton(ManagePanel, text='Can Delete Tag', var = CanDelete, font = EntryFont)
        CanDelete_Box.place(x= 300, y = 200)
        print(self.UserList)
    def OpenUser(self, user):
        print("doing " + user)