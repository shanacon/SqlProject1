import tkinter as tk
class ManageUser:
    def __init__(self, window, BtnFont):
        ManagePanel = tk.Toplevel(window)
        ManagePanel.geometry('600x500')
        User_Btn = tk.Button(ManagePanel, text ="User", bg = "light blue", width = '10', height = '1', font = BtnFont)
        User_Btn.place(x = 0, y = 0)