import tkinter as tk
from Event import *
class ManageTag: 
    def __init__(self, window, BtnFont, EntryFont):
        self.ManagePanel = tk.Toplevel(window)
        self.ManagePanel.geometry('600x500')
        self.TypeList = GetAllType()
        self.TagBtnList = []
        self.SelectTag = None
        count = 0
        for TypeName in self.TypeList :
            newBtn = tk.Button(self.ManagePanel, text = TypeName, bg = "antique white", width = '10', height = '1', font = BtnFont)
            newBtn.config(command = lambda TypeName = TypeName :self.OpenType(TypeName, EntryFont))
            newBtn.place(x = 0, y = 0 + count * 50)
            count += 1
        ###
    def OpenType(self, TypeName, EntryFont) :
        self.ClearBtn()
        TagList = GetAllTag(TypeName)
        count = 0
        for tag in TagList :
            newBtn = tk.Button(self.ManagePanel, text = tag, bg = "antique white", width = '10', height = '1', font = EntryFont)
            newBtn.config(command = lambda:self.showEdit())
            pos = self.GetPos(count)
            newBtn.place(x = pos[0], y = pos[1])
            self.TagBtnList.append(newBtn)
            count += 1
    def showEdit(self):
        print("doing")
    def GetPos(self, count):
        ret = [250 + (count%3) *110, 0 + int(count/3) * 35]
        return ret
    def ClearBtn(self):
        for Btn in self.TagBtnList :
            Btn.destroy()
        self.TagBtnList.clear()