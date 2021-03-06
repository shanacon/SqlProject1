import tkinter as tk
import os
from tkinter import filedialog
import MySQLdb
###
UserName = ""
Pswd = ""
rootName = "root"
rootPswd = "w123741852"
con = None
ManagerCon = None
def NewType(Type_Input, DropDown_1, var_1, DropDown_2, var_2, StatusText) :
    if Type_Input.get()=="":
        StatusText['text'] = "Please input Type name"
    else :
        try :
            cur=con.cursor()
            cur.execute(f"INSERT into type Values(null, '{Type_Input.get()}')")
            con.commit()
            StatusText['text'] = ""
        except MySQLdb.OperationalError as e :
            print(e)
            StatusText['text'] = "no access.\nPlease contact admin"
    Type_Input.delete(0, 'end')
    return RefreshTypeList(DropDown_1, var_1, DropDown_2, var_2)
###
def RefreshTypeList(DropDown_1, var_1, DropDown_2, var_2):
    DropDown_1['menu'].delete(0, 'end')
    DropDown_2['menu'].delete(0, 'end')
    cur=con.cursor()
    TypeList = []
    cur.execute ("SELECT name from type")
    for item in cur.fetchall():
        TypeList.append(item[0])
    for item in TypeList: 
        DropDown_1['menu'].add_command(label=item, command=tk._setit(var_1, item))
        DropDown_2['menu'].add_command(label=item, command=tk._setit(var_2, item))
    if TypeList :
        var_1.set(TypeList[0])
    return TypeList
###
def NewTag(Tag_Input, variable, StatusText):
    cur=con.cursor()
    if Tag_Input.get() != "":
        if variable.get() != "":
            try :
                cur.execute(f"SELECT type_id from Type WHERE name='{variable.get()}'")
                id = cur.fetchone()[0]
                cur.execute(f"INSERT into Tag Values(null, '{Tag_Input.get()}', '{id}')")
                con.commit()
                Tag_Input.delete(0, 'end')
                StatusText['text'] = ""
            except MySQLdb.OperationalError as e :
                print(e)
                StatusText['text'] = "no access.\nPlease contact admin"
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
    StatusText['text'] = ""
    file_path.insert(0, filename)
    return Check_Path(filename, StatusText)
###
def Check_Path(path, StatusText) :
    if path == "" :
        return
    cur=con.cursor()
    cur.execute (f"SELECT file_id from File WHERE path = '{path}'")
    tmp = cur.fetchone()
    if tmp == None :
        file_id = InsertPath(path, StatusText)
    else :
        file_id = tmp[0]
    return file_id
###
def InsertPath(path, StatusText):
    try:
        cur=con.cursor()
        cur.execute(f"Insert into File Values(null, '{path}', '{os.path.basename(path)}')")
        con.commit()
        cur.execute(f"SELECT file_id from File WHERE path = '{path}'")
    except MySQLdb.OperationalError as e :
        print(e)
        StatusText['text'] = "no access.\nPlease contact admin"
    return cur.fetchone()[0]
###
def SetFileTag(file_id, tag_id, StatusText):
    try:
        cur=con.cursor()
        cur.execute(f"Insert into Relation Values('{file_id}', '{tag_id}')")
        con.commit()
        return True
    except MySQLdb.OperationalError as e :
        print(e)
        StatusText['text'] = "no access.\nPlease contact admin"
        return False
##
def RefreshTagSystem(DropDown_1, var_1, type):
    DropDown_1['menu'].delete(0, 'end')
    cur=con.cursor()
    cur.execute (f"SELECT type_id from Type WHERE name = '{type}'")
    if type != "" :
        type = cur.fetchone()[0]
        TagList = []
        cur.execute(f"SELECT name from Tag WHERE type = {type}")
        for item in cur.fetchall():
            TagList.append(item[0])
        for item in TagList: 
            DropDown_1['menu'].add_command(label=item, command=tk._setit(var_1, item))
        if TagList :
            var_1.set(TagList[0])
        else : 
            var_1.set("")
###
def DeleteRelation(file_id, tag_id, StatusText) :
    try :
        cur=con.cursor()
        cur.execute(f"Delete from Relation WHERE file_id = {file_id} AND tag_id = {tag_id}")
        con.commit()
        StatusText['text'] = ""
        return True
    except MySQLdb.OperationalError as e :
        StatusText['text'] = "no access.\nPlease contact admin"
        print(e)
        return False
###
def GetTagsByFileID(file_id) :
    cur=con.cursor()
    TagList = []
    cur.execute(f"SELECT tag_id from Relation WHERE file_id = {file_id}")
    for tag_id in cur.fetchall():
        TagList.append(tag_id[0])
    return TagList
###
def GetPos(count, item) :
    item.place(x = 540 + (count%2) * 130, y = 15 + int(count/2) * 35)
def GetPosOfSearch(count, item) :
    item.place(x = 40, y = 15 + count * 35)
###
def GetTagidByName(TagName, StatusText):
    cur=con.cursor()
    cur.execute(f"SELECT tag_id from Tag WHERE name = '{TagName}'")
    tmp = cur.fetchone()
    if tmp :
        StatusText['text'] = ""
        return tmp[0]
    else :
        StatusText['text'] = "no such tag"
def GetFileidByPath(path, StatusText):
    if path == None or path == "input path" :
        StatusText['text'] = "no such file"
        return -1
    cur=con.cursor()
    cur.execute (f"SELECT file_id from File WHERE path = '{path}'")
    tmp = cur.fetchone()
    if tmp :
        StatusText['text'] = ""
        return tmp[0]
    else :
        StatusText['text'] = "no such file"
def GetNameByTagid(TagID, StatusText):
    cur=con.cursor()
    cur.execute(f"SELECT name from Tag WHERE tag_id = {TagID}")
    tmp = cur.fetchone()
    if tmp :
        StatusText['text'] = ""
        return tmp[0]
    else :
        StatusText['text'] = "no such tag id"
def GetPathByFileid(fileID, StatusText):
    cur=con.cursor()
    cur.execute (f"SELECT path from File WHERE file_id = '{fileID}'")
    tmp = cur.fetchone()
    if tmp :
        StatusText['text'] = ""
        return tmp[0]
    else :
        StatusText['text'] = "no such fileid"
####
def SearchByString(input, StatusText) :
    tagList = []
    LogicList = []
    ret = []
    if input == None or input == "" :
        cur=con.cursor()
        command = "SELECT DISTINCT  file_id FROM Relation"
        cur.execute(command)
        tmp = cur.fetchall()
        if tmp :
            StatusText['text'] = ""
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
    cur=con.cursor()
    # print(command)
    cur.execute(command)
    tmp = cur.fetchall()
    if tmp :
        for item in tmp :
            ret.append(item[0])
        StatusText['text'] = ""
    else :
        StatusText['text'] = "No file Found"
    return ret
###
def Login(username, psw):
    global UserName
    global Pswd
    global con
    try :
        con = MySQLdb.connect(host="localhost", user = username, password = psw, db = "filedata")
        UserName = username
        Pswd = psw
        return True
    except Exception as e: 
        print(e)
        return False
def SignUp(username, psw):
    global con
    try :
        SignCon = MySQLdb.connect(host="localhost", user = rootName, password = rootPswd, db = "sys")
        cur = SignCon.cursor()
        command = f"CREATE USER '{username}'@'localhost' IDENTIFIED BY '{psw}';"
        cur.execute(command)
        command = f"GRANT SELECT ON `filedata`.* To  '{username}'@'localhost';"
        cur.execute(command)
        return True
    except Exception as e: 
        print(e)
        return False
def Initialize():
    global ManagerCon
    ManagerCon = MySQLdb.connect(host="localhost", user = rootName, password = rootPswd, db = "sys")
    cur = ManagerCon.cursor()
    command = "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = 'filedata'"
    cur.execute(command)
    if cur.fetchone() == None:
        command = "CREATE DATABASE IF NOT EXISTS filedata"
        cur.execute(command)
        command = "CREATE TABLE `filedata`.`type` (`type_id` INT NOT NULL AUTO_INCREMENT,`name` VARCHAR(60) NOT NULL, PRIMARY KEY (`type_id`));"
        cur.execute(command)
        command = "CREATE TABLE `filedata`.`tag` ( `tag_id` INT NOT NULL AUTO_INCREMENT, `name` VARCHAR(60) NOT NULL, `type` INT NOT NULL, PRIMARY KEY (`tag_id`), INDEX `type_idx` (`type` ASC) VISIBLE, CONSTRAINT `type` FOREIGN KEY (`type`) REFERENCES `filedata`.`type` (`type_id`) ON DELETE NO ACTION ON UPDATE NO ACTION);"
        cur.execute(command)
        command = "CREATE TABLE `filedata`.`file` ( `file_id` INT NOT NULL AUTO_INCREMENT, `path` VARCHAR(256) NOT NULL, `filename` VARCHAR(128) NOT NULL, PRIMARY KEY (`file_id`));"
        cur.execute(command)
        command = "CREATE TABLE `filedata`.`relation` ( `file_id` INT NOT NULL, `tag_id` INT NOT NULL, INDEX `file_id_idx` (`file_id` ASC) VISIBLE, INDEX `tag_id_idx` (`tag_id` ASC) VISIBLE, CONSTRAINT `file_id` FOREIGN KEY (`file_id`) REFERENCES `filedata`.`file` (`file_id`) ON DELETE NO ACTION ON UPDATE NO ACTION, CONSTRAINT `tag_id` FOREIGN KEY (`tag_id`) REFERENCES `filedata`.`tag` (`tag_id`) ON DELETE NO ACTION ON UPDATE NO ACTION);"
        cur.execute(command)
def GetAllUser():
    ManagerCon = MySQLdb.connect(host="localhost", user = UserName, password = Pswd, db = "sys")
    cur = ManagerCon.cursor()
    command = "Select user from mysql.user;"
    cur.execute(command)
    UserList = []
    for item in cur.fetchall():
        if item[0] != "mysql.sys" and item[0] != "root" and item[0] != "mysql.infoschema" and item[0] != "mysql.session":
            UserList.append(item[0])
    return UserList
def GetAllType():
    TypeList = []
    cur = con.cursor()
    cur.execute ("SELECT name from type")
    for item in cur.fetchall():
        TypeList.append(item[0])
    return TypeList
def GetAllTag(TypeName):
    TagList = []
    cur = con.cursor()
    cur.execute (f"SELECT type_id from Type WHERE name = '{TypeName}'")
    if TypeName != "" :
        TypeName = cur.fetchone()[0]
        TagList = []
        cur.execute(f"SELECT name from Tag WHERE type = {TypeName}")
        for item in cur.fetchall():
            TagList.append(item[0])
    return TagList
def GetGrant(user):
    cur = ManagerCon.cursor()
    command = f"SHOW grants  for '{user}'@'localhost';"
    cur.execute(command)
    Data = [False, False, False]
    for item in cur.fetchall():
        aya = item[0].split(' ')
        if "`filedata`.*" in aya :
            tmp = ""
            for i in range(1, aya.index("`filedata`.*") - 1) :
                tmp += aya[i]
            tmp = tmp.split(',')
            if "SELECT" in tmp:
                Data[0] = True
            if "INSERT" in tmp:
                Data[1] = True
            if "DELETE" in tmp:
                Data[2] = True
    return Data
def Save(user, grants):
    cur = ManagerCon.cursor()
    command = ""
    if grants[0] :
        command = f"GRANT SELECT ON `filedata`.* To  '{user}'@'localhost';"
    else :
        command = f"revoke SELECT on filedata.* from '{user}'@'localhost';"
    cur.execute(command)
    if grants[1] :
        command = f"GRANT INSERT ON `filedata`.* To  '{user}'@'localhost';"
    else :
        command = f"revoke INSERT on filedata.* from '{user}'@'localhost';"
    cur.execute(command)
    if grants[2] :
        command = f"GRANT DELETE ON `filedata`.* To  '{user}'@'localhost';"
    else :
        command = f"revoke DELETE on filedata.* from '{user}'@'localhost';"
    cur.execute(command)
def Rename(OldName, NewName):
    cur = con.cursor()
    command = f"UPDATE tag SET name = '{NewName}' WHERE name = '{OldName}';"
    cur.execute(command)
    con.commit()
