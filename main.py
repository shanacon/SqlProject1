import tkinter as tk
import tkinter.font as font
from Event import *
window = tk.Tk()
###
BtnFont = font.Font(size=20)
EntryFont = font.Font(size=14)
###
New_Type_Btn = tk.Button(window, text ="New Type", bg = "light blue", width = '10', height = '1', font = BtnFont)
New_Type_Btn.place(x = 50, y = 50)
New_Tag_Btn = tk.Button(window, text ="New Tag", bg = "light blue", width = '10', height = '1', font = BtnFont)
New_Tag_Btn.place(x = 50, y = 100)
Browse_Btn = tk.Button(window, text ="Browse", bg = "light blue", width = '10', height = '1', font = BtnFont)
Browse_Btn.place(x = 50, y = 175)
Add_Tag_Btn = tk.Button(window, text ="Add Tag", bg = "light blue", width = '10', height = '1', font = BtnFont)
Add_Tag_Btn.place(x = 210, y = 175)
Save_Btn = tk.Button(window, text ="Save", bg = "light blue", width = '10', height = '1', font = BtnFont)
Save_Btn.place(x = 370, y = 175)
###
Type_Input = tk.Entry(window, font = BtnFont, width = '11')
Type_Input.place(x = 210, y = 58)
Tag_Input = tk.Entry(window, font = BtnFont, width = '11')
Tag_Input.place(x = 210, y = 108)
file_path = tk.Entry(window, font = EntryFont, width = '52')
file_path.insert(0, 'input path')
file_path.place(x = 50, y = 150)
###
variable = tk.StringVar(window)
type_of_tag = tk.OptionMenu(window, BtnFont, variable)
type_of_tag.config(width = 11, bg = "light blue")
type_of_tag.place(x = 370, y = 108)
### set command
New_Type_Btn.config(command = lambda:NewType(Type_Input.get()))
window.title('FileTagger')
window.geometry('800x300')
window.mainloop()