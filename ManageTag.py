import tkinter as tk
from Event import *
class ManageTag: 
    def __init__(self, window, BtnFont, EntryFont):
        self.ManagePanel = tk.Toplevel(window)
        self.ManagePanel.geometry('600x500')
        self.TypeList = GetAllType()
        self.TagBtnList = []
        self.SelectType = None
        self.SelectTag = None
        self.EntryFont = EntryFont
        count = 0
        for TypeName in self.TypeList :
            newBtn = tk.Button(self.ManagePanel, text = TypeName, bg = "antique white", width = '10', height = '1', font = BtnFont)
            newBtn.config(command = lambda TypeName = TypeName :self.OpenType(TypeName, EntryFont))
            newBtn.place(x = 0, y = 0 + count * 50)
            count += 1
        ###
        self.Rename_Input = tk.Entry(self.ManagePanel, font = BtnFont, width = '11')
        self.Rename_Btn = tk.Button(self.ManagePanel, text = "Rename", bg = "antique white", width = '10', height = '1', font = BtnFont)
        self.Rename_Btn.config(command = lambda:self._Rename())
    def OpenType(self, TypeName, EntryFont) :
        self.ClearBtn()
        self.HideEditUI()
        TagList = GetAllTag(TypeName)
        count = 0
        for tag in TagList :
            newBtn = tk.Button(self.ManagePanel, text = tag, bg = "antique white", width = '10', height = '1', font = EntryFont)
            newBtn.config(command = lambda tag = tag :self.ShowEditUI(tag))
            pos = self.GetPos(count)
            newBtn.place(x = pos[0], y = pos[1])
            self.TagBtnList.append(newBtn)
            count += 1
        self.SelectType = TypeName
    def ShowEditUI(self, tag):
        self.Rename_Input.place(x = 200, y = 400)
        self.Rename_Btn.place(x = 400, y = 390)
        self.Rename_Input.delete(0, 'end')
        self.Rename_Input.insert(0, tag)
        self.SelectTag = tag
    def HideEditUI(self):
        self.Rename_Input.place_forget()
        self.Rename_Btn.place_forget()
    def GetPos(self, count):
        ret = [250 + (count%3) *110, 0 + int(count/3) * 35]
        return ret
    def ClearBtn(self):
        for Btn in self.TagBtnList :
            Btn.destroy()
        self.TagBtnList.clear()
    def RenameRefresh(self, selectType):
        self.ClearBtn()
        TagList = GetAllTag(selectType)
        count = 0
        for tag in TagList :
            newBtn = tk.Button(self.ManagePanel, text = tag, bg = "antique white", width = '10', height = '1', font = self.EntryFont)
            newBtn.config(command = lambda tag = tag :self.ShowEditUI(tag))
            pos = self.GetPos(count)
            newBtn.place(x = pos[0], y = pos[1])
            self.TagBtnList.append(newBtn)
            count += 1
    def _Rename(self):
        Rename(self.SelectTag, self.Rename_Input.get())
        self.Rename_Input.delete(0, 'end')
        self.RenameRefresh(self.SelectType)