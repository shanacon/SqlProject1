import sqlite3 as lite
import tkinter as tk
import os
from tkinter import filedialog
###
def NewType(Type_Input, DropDown_1, var_1, DropDown_2, var_2, StatusText) :
    con = lite.connect('FileData.db')
    if Type_Input.get()=="":
        StatusText['text'] = "Please input Type name"
    else :
        with con:
            cur=con.cursor()
            cur.execute(f"INSERT into Type Values(null, '{Type_Input.get()}')")
    Type_Input.delete(0, 'end')
    return RefreshTypeList(DropDown_1, var_1, DropDown_2, var_2)
###
def RefreshTypeList(DropDown_1, var_1, DropDown_2, var_2):
    DropDown_1['menu'].delete(0, 'end')
    DropDown_2['menu'].delete(0, 'end')
    con = lite.connect('FileData.db')
    cur=con.cursor()
    TypeList = []
    for item in cur.execute ("SELECT name from Type") :
        TypeList.append(item[0])
    for item in TypeList: 
        DropDown_1['menu'].add_command(label=item, command=tk._setit(var_1, item))
        DropDown_2['menu'].add_command(label=item, command=tk._setit(var_2, item))
    if TypeList :
        var_1.set(TypeList[0])
    return TypeList
###
def NewTag(Tag_Input, variable, StatusText):
    con = lite.connect('FileData.db')
    with con:
        cur=con.cursor()
        if Tag_Input.get() != "":
            if variable.get() != "":
                cur.execute(f"SELECT type_id from Type WHERE name='{variable.get()}'")
                id = cur.fetchone()[0]
                cur.execute(f"INSERT into Tag Values(null, '{Tag_Input.get()}', '{id}')")
                Tag_Input.delete(0, 'end')
            else:
                StatusText['text'] = "Please select Type"
        else:
            StatusText['text'] = "Please input Tag"
###
def Browse(file_path, StatusText):
    file_path.delete(0, 'end')
    filename = filedialog.askdirectory(initialdir = os.getcwd(),title = "Select a File")
    if filename == None or filename == "":
       StatusText['text'] = "please choose folder"
       return None
    file_path.insert(0, filename)
    return Check_Path(filename)
###
def Check_Path(path) :
    if path == "" :
        return
    con = lite.connect('FileData.db')
    cur=con.cursor()
    cur.execute (f"SELECT file_id from File WHERE path = '{path}'")
    tmp = cur.fetchone()
    if tmp == None :
        file_id = InsertPath(path)
    else :
        file_id = tmp[0]
    return file_id
###
def InsertPath(path):
    con = lite.connect('FileData.db')
    with con:
        cur=con.cursor()
        cur.execute(f"Insert into File Values(null, '{path}', '{os.path.basename(path)}')")
        cur.execute(f"SELECT file_id from File WHERE path = '{path}'")
        return cur.fetchone()[0]
###
def SetFileTag(file_id,tag_id):
    con = lite.connect('FileData.db')
    with con:
        cur=con.cursor()
        cur.execute(f"Insert into Relation Values('{file_id}', '{tag_id}')")
##
def RefreshTagSystem(DropDown_1, var_1, type):
    DropDown_1['menu'].delete(0, 'end')
    con = lite.connect('FileData.db')
    cur=con.cursor()
    cur.execute (f"SELECT type_id from Type WHERE name = '{type}'")
    type = cur.fetchone()[0]
    TagList = []
    for item in cur.execute(f"SELECT name from Tag WHERE type = {type}") :
        TagList.append(item[0])
    for item in TagList: 
        DropDown_1['menu'].add_command(label=item, command=tk._setit(var_1, item))
    if TagList :
        var_1.set(TagList[0])
###
def DeleteRelation(file_id, tag_id) :
    con = lite.connect('FileData.db')
    cur=con.cursor()
    cur.execute(f"Delete from Relation WHERE file_id = {file_id} AND tag_id = {tag_id}")
    con.commit()
###
def GetTagsByFileID(file_id) :
    con = lite.connect('FileData.db')
    cur=con.cursor()
    TagList = []
    for tag_id in cur.execute(f"SELECT tag_id from Relation WHERE file_id = {file_id}") :
        TagList.append(tag_id[0])
    return TagList
###
def GetPos(count, item) :
    item.place(x = 540 + (count%2) * 130, y = 15 + int(count/2) * 35)
def GetPosOfSearch(count, item) :
    item.place(x = 40, y = 15 + count * 35)
###
def GetTagidByName(TagName, StatusText):
    con = lite.connect('FileData.db')
    cur=con.cursor()
    cur.execute(f"SELECT tag_id from Tag WHERE name = '{TagName}'")
    tmp = cur.fetchone()
    if tmp :
        return tmp[0]
    else :
        StatusText['text'] = "no such tag"
def GetFileidByPath(path, StatusText):
    if path == None or path == "input path" :
        StatusText['text'] = "no such file"
        return -1
    con = lite.connect('FileData.db')
    cur=con.cursor()
    cur.execute (f"SELECT file_id from File WHERE path = '{path}'")
    tmp = cur.fetchone()
    if tmp :
        return tmp[0]
    else :
        StatusText['text'] = "no such file"
def GetNameByTagid(TagID, StatusText):
    con = lite.connect('FileData.db')
    cur=con.cursor()
    cur.execute(f"SELECT name from Tag WHERE tag_id = {TagID}")
    tmp = cur.fetchone()
    if tmp :
        return tmp[0]
    else :
        StatusText['text'] = "no such tag id"
def GetPathByFileid(fileID, StatusText):
    con = lite.connect('FileData.db')
    cur=con.cursor()
    cur.execute (f"SELECT path from File WHERE file_id = '{fileID}'")
    tmp = cur.fetchone()
    if tmp :
        return tmp[0]
    else :
        StatusText['text'] = "no such fileid"
####
def SearchByString(input, StatusText) :
    tagList = []
    LogicList = []
    ret = []
    if input == None or input == "" :
        con = lite.connect('FileData.db')
        cur=con.cursor()
        command = "SELECT DISTINCT  file_id FROM Relation"
        cur.execute(command)
        tmp = cur.fetchall()
        if tmp :
            for item in tmp :
                ret.append(item[0])
        else :
            StatusText['text'] = "No file Found"
        return ret
    And_1 = "SELECT file_id FROM(SELECT * FROM Relation WHERE file_id IN("
    ## succuess :"SELECT file_id FROM(SELECT * FROM Relation WHERE file_id IN(SELECT file_id FROM Relation WHERE tag_id = 8)) as a WHERE tag_id = 10"
    tmp = input.split(' ')
    for str in tmp :
        if len(tagList) == len(LogicList) :
            tagList.append(str)
        else :
            LogicList.append(str)
    command = f"SELECT file_id FROM Relation WHERE tag_id = {GetTagidByName(tagList[0], StatusText)}"
    count = 1
    for logic in LogicList :
        if logic == "and":
            command = And_1 + command + f")) as a WHERE tag_id = {GetTagidByName(tagList[count], StatusText)}"
        elif logic == "or":
            orcmd = f"SELECT file_id FROM Relation WHERE tag_id = {GetTagidByName(tagList[count], StatusText)}"
            command = command + " UNION " + orcmd
        count+=1
    con = lite.connect('FileData.db')
    cur=con.cursor()
    # print(command)
    cur.execute(command)
    tmp = cur.fetchall()
    if tmp :
        for item in tmp :
            ret.append(item[0])
    else :
        StatusText['text'] = "No file Found"
    return ret