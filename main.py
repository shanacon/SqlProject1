import tkinter as tk
from typing import Text
window = tk.Tk()
Type_Input = tk.Entry(window)
Type_Input.place(x = 100, y = 0)
Type_Label = tk.Label(window, text = "Input Type:")
Type_Label.place(x = 0, y = 0)
window.title('FileTagger')
window.geometry('800x600')
window.mainloop()