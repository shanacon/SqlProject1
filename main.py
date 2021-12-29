import tkinter as tk
import tkinter.font as font
from Event import *
window = tk.Tk()
###
BtnFont = font.Font(size=20)
EntryFont = font.Font(size=14)
###
TypeList = []
TagList = []
TagBtnList = []
Now_fileID = -1
### function
def AddTagByDropDown() :
    tag_id = GetTagidByName(tag_var.get(), StatusText)
    file_id = GetFileidByPath(file_path.get(), StatusText)
    if file_id != -1 :
        SetFileTag(file_id, tag_id)
        SetTagsShow()
def AddTagByEntry() :
    tag_id = GetTagidByName(Tag_E.get(), StatusText)
    file_id = GetFileidByPath(file_path.get(), StatusText)
    Tag_E.delete(0, 'end')
    if file_id != -1 :
        SetFileTag(file_id, tag_id)
        SetTagsShow()
def SetTagsShow() :
    RemoveAllTagBtn()
    FileTagList = GetTagsByFileID(Now_fileID)
    count = 0
    for id in FileTagList :
        newBtn = tk.Button(window, text = GetNameByTagid(id, StatusText), bg = "antique white", width = '10', height = '1', font = EntryFont)
        newBtn.config(command = lambda id = id :_DeleteRelation(Now_fileID, id))
        GetPos(count, newBtn)
        TagBtnList.append(newBtn)
        count += 1
def RemoveAllTagBtn() :
    global TagBtnList
    for Btn in TagBtnList :
        Btn.destroy()
    TagBtnList.clear()
def SetSearchResultWindow(PathList) :
    SearchResult = tk.Toplevel(window)
    SearchResult.geometry('200x500')
    ###
    count = 0
    for path in PathList :
        newBtn = tk.Button(SearchResult, text = os.path.basename(path), bg = "antique white", width = '10', height = '1', font = EntryFont)
        newBtn.config(command = lambda path = path :OpenExploer(path))
        GetPosOfSearch(count, newBtn)
        count += 1
def OpenExploer(path):
    os.startfile(path)
def _NewTag() :
    NewTag(Tag_Input, variable, StatusText)
    RefreshTagSystem(tag_d, tag_var, type_var.get())
def _Browse() :
    global Now_fileID
    Now_fileID = Browse(file_path, StatusText)
    SetTagsShow()
def _Check_Path() :
    global Now_fileID
    Now_fileID = Check_Path(file_path.get())
    SetTagsShow()
def _DeleteRelation(file_id, tag_id) :
    DeleteRelation(file_id, tag_id)
    SetTagsShow()
def _SearchByString() :
    FileidList = SearchByString(Search_Input.get(), StatusText)
    PathList = []
    for id in FileidList :
        PathList.append(GetPathByFileid(id, StatusText))
    SetSearchResultWindow(PathList)
def _Login():
    if Login(User_Input.get(), PSW_Input.get()) :
        Hide_Login()
        ShowUI()
        StatusText['text'] = ""
    else :
        StatusText['text'] = "login error"
def _Disconnect():
    global con
    con = None
    Show_Login()
    HideUI()
def _SignUp():
    global con
    if SignUp(R_User_Input.get(), R_PSW_Input.get()) :
        StatusText['text'] = ""
        R_User_Input.delete(0, 'end')
        R_PSW_Input.delete(0, 'end')
    else :
        StatusText['text'] = "SignUp error"
### Label
StatusText = tk.Label(window, text ="", font = EntryFont)
StatusText.place(x = 380, y = 60)
### button
New_Type_Btn = tk.Button(window, text ="New Type", bg = "light blue", width = '10', height = '1', font = BtnFont)
New_Tag_Btn = tk.Button(window, text ="New Tag", bg = "light blue", width = '10', height = '1', font = BtnFont)
Browse_Btn = tk.Button(window, text ="Browse", bg = "light blue", width = '10', height = '1', font = BtnFont)
Add_Tag_Btn = tk.Button(window, text ="Add Tag", bg = "light blue", width = '10', height = '1', font = BtnFont)
Check_Btn = tk.Button(window, text ="Check", bg = "light blue", width = '10', height = '1', font = EntryFont)
Add_Tag_Btn2 = tk.Button(window, text ="Add Tag", bg = "light blue", width = '10', height = '1', font = EntryFont)
Search_Btn = tk.Button(window, text ="Search", bg = "light blue", width = '10', height = '1', font = BtnFont)
Disconnect_Btn = tk.Button(window, text ="Disconnect", bg = "light blue", width = '10', height = '1', font = EntryFont)
##
Regis_Btn = tk.Button(window, text ="Sign up", bg = "light blue", width = '10', height = '1', font = BtnFont)
Login_Btn = tk.Button(window, text ="Login", bg = "light blue", width = '10', height = '1', font = BtnFont)
### input entry
Type_Input = tk.Entry(window, font = BtnFont, width = '11')
Tag_Input = tk.Entry(window, font = BtnFont, width = '11')
file_path = tk.Entry(window, font = EntryFont, width = '38')
file_path.insert(0, 'input path')
Tag_E = tk.Entry(window, font = EntryFont, width = '16')
Tag_E.insert(0, 'input tag')
Search_Input = tk.Entry(window, font = EntryFont, width = '34')
#
User_Input = tk.Entry(window, font = EntryFont, width = '20')
User_Input.insert(0, 'input username')

PSW_Input = tk.Entry(window, font = EntryFont, width = '20', show="*")
#
R_User_Input = tk.Entry(window, font = EntryFont, width = '20')
R_User_Input.insert(0, 'input username')
R_PSW_Input = tk.Entry(window, font = EntryFont, width = '20', show="*")
### checkbox
IsAdmin = tk.BooleanVar()
IsAdmin_Btn = tk.Checkbutton(window, text='Admin', var=IsAdmin, font = EntryFont)
### dropdown
variable = tk.StringVar(window)
type_of_tag = tk.OptionMenu(window, variable, "")
type_of_tag.config(width = 11, bg = "light blue", font = EntryFont)
#
type_var = tk.StringVar(window)
type_d = tk.OptionMenu(window, type_var, "")
type_d.config(width = 12, bg = "light blue", font = EntryFont)
tag_var = tk.StringVar(window)
tag_d = tk.OptionMenu(window, tag_var, "")
tag_d.config(width = 12, bg = "light blue", font = EntryFont)
### set command
New_Type_Btn.config(command = lambda:NewType(Type_Input, type_of_tag, variable, type_d, type_var, StatusText))
New_Tag_Btn.config(command = lambda:_NewTag())
Browse_Btn.config(command = lambda:_Browse())
Check_Btn.config(command = lambda:_Check_Path())
type_var.trace("w", lambda *args: RefreshTagSystem(tag_d, tag_var, type_var.get()))
Add_Tag_Btn.config(command = lambda:AddTagByDropDown())
Add_Tag_Btn2.config(command = lambda:AddTagByEntry())
Search_Btn.config(command = lambda:_SearchByString())
Login_Btn.config(command = lambda:_Login())
Disconnect_Btn.config(command = lambda:_Disconnect())
Regis_Btn.config(command = lambda:_SignUp())
###
def ShowUI():
    global TypeList  
    TypeList = RefreshTypeList(type_of_tag, variable, type_d, type_var)
    New_Type_Btn.place(x = 50, y = 50)
    New_Tag_Btn.place(x = 50, y = 100)
    Browse_Btn.place(x = 50, y = 175)
    Add_Tag_Btn.place(x = 370, y = 190)
    Check_Btn.place(x = 410, y = 142)
    Add_Tag_Btn2.place(x = 370, y = 260)
    Search_Btn.place(x = 370, y = 325)
    Type_Input.place(x = 210, y = 58)
    Tag_Input.place(x = 210, y = 108)
    file_path.place(x = 50, y = 150)
    Tag_E.place(x = 210, y = 265)
    Search_Input.place(x = 50, y = 337)
    type_of_tag.place(x = 378, y = 108)
    type_d.place(x = 208, y = 175)
    tag_d.place(x = 208, y = 215)
    Disconnect_Btn.place(x = 0, y = 0)
def HideUI():
    New_Type_Btn.place_forget()
    New_Tag_Btn.place_forget()
    Browse_Btn.place_forget()
    Add_Tag_Btn.place_forget()
    Check_Btn.place_forget()
    Add_Tag_Btn2.place_forget()
    Search_Btn.place_forget()
    Type_Input.place_forget()
    Tag_Input.place_forget()
    file_path.place_forget()
    Tag_E.place_forget()
    Search_Input.place_forget()
    type_of_tag.place_forget()
    type_d.place_forget()
    tag_d.place_forget()
    RemoveAllTagBtn()
    StatusText['text'] = ""
    Disconnect_Btn.place_forget()
def Show_Login():
    R_User_Input.place(x = 650, y = 50)
    R_PSW_Input.place(x = 650, y = 80)
    IsAdmin_Btn.place(x = 650, y = 110)
    User_Input.place(x = 650, y = 250)
    PSW_Input.place(x = 650, y = 280)
    Regis_Btn.place(x = 650, y = 150)
    Login_Btn.place(x = 650, y = 305)
def Hide_Login() :
    R_User_Input.place_forget()
    R_PSW_Input.place_forget()
    IsAdmin_Btn.place_forget()
    User_Input.place_forget()
    PSW_Input.place_forget()
    Regis_Btn.place_forget()
    Login_Btn.place_forget()

###
Initialize()
Show_Login()
window.title('FileTagger')
window.geometry('1000x400')
window.mainloop()
###