import sqlite3 as lite
import tkinter as tk
###
def NewType(Type_Input, DropDown, var) :
    con = lite.connect('FileData.db')
    if Type_Input.get()=="":
        print("todo : status Text")
    else :
        with con:
            cur=con.cursor()
            cur.execute(f"Insert into Type Values(null, '{Type_Input.get()}')")
    Type_Input.delete(0, 'end')
    return RefreshDropDown(DropDown, var)
###
def RefreshDropDown(DropDown, var):
    DropDown['menu'].delete(0, 'end')
    con = lite.connect('FileData.db')
    cur=con.cursor()
    TypeList = []
    for item in cur.execute ("select name from Type") :
        TypeList.append(item[0])
    for item in TypeList: 
        DropDown['menu'].add_command(label=item, command=tk._setit(var, item))
    return TypeList
###
def NewTag(Tag_Input, variable):
    con = lite.connect('FileData.db')
    with con:
        cur=con.cursor()
        if Tag_Input.get() != "":
            if variable.get() != "":
                cur.execute(f"SELECT type_id from Type WHERE name='{variable.get()}'")
                id = cur.fetchone()[0]
                cur.execute(f"Insert into Tag Values(null, '{Tag_Input.get()}', '{id}')")
                Tag_Input.delete(0, 'end')
            else:
                print("todo : status Text")
        else:
            print("todo : status Text")