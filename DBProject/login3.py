# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 20:34:32 2020

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 21:04:50 2020

@author: hp
""" 
import cx_Oracle
from tkinter import simpledialog
from tkinter import*
import capt_demo 
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import re 
import config as cfg
import email_demo as emd
import os
z=0
exist_table_list=[' Existing Table List']
class Register:
    #function for background image and its label
    def background(self,window_name):
        #background image and title
        self.root=root
        self.root.title(window_name)
        self.root.geometry("1350x700+0+0")
        self.root.config(bg='white')     
        self.bg=ImageTk.PhotoImage(file='images/login_background.jpg')
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
    #function for craeting a login window
    def alter_add_column(self):
        var=StringVar()
        self.attribute_name_list=[]
        self.create_table_frame=Frame(self.root,bd=0,bg='white')
        self.create_table_frame.place(x=0,y=0,width=1500,height=150)
        self.new_entry_btn=Button(self.root,text="Add Column",font=("times new roman",20,"bold"),fg="White",bg="yellow",bd=5,cursor="hand2",command=self.new_entry_box)
        self.new_entry_btn.place(x=1200,y=10,width=200)
        self.l1=Frame(self.root,bg='yellow',bd=0)
        self.l1.place(x=0,y=150,width=1500,height=500)
        self.canvas=Canvas(self.l1,height=500,bg='white',bd=0)
        self.new_frame=Frame(self.canvas,width=1500,bg='white',height=500,bd=0)
        self.myscrollbar=Scrollbar(self.l1,orient="vertical",command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.myscrollbar.set)
        self.myscrollbar.pack(side="right",fill="y")
        self.canvas.place(x=0,y=0,width=1500,height=500)
        self.canvas.create_window((0,0),window=self.new_frame,anchor='nw')
        self.new_frame.bind("<Configure>",lambda e:self.canvas.configure(scrollregion = self.canvas.bbox('all')))
        var.set(self.alter_exist_table.get())
        table_name=Label(self.create_table_frame,text="New Table Name : ",font=('times new roman',20,"bold"),bg='white',fg='Green').place(x=250,y=10,width=250)       
        self.table_name_txt=Entry(self.create_table_frame,textvariable=var,font=('times new roman',20),bg='lightgray',fg="red")
        self.table_name_txt.place(x=500,y=10,width=200) 
        attribute_label=Button(text="Attribute Name",fg="red",bg="White",font=('times new roman',20,"bold"),relief='solid',state="disabled").place(x=50,y=80,width=200)
        datatype_label=Button(text="Data Type",fg="red",bg="White",font=('times new roman',20,"bold"),relief='solid',state="disabled").place(x=319,y=80,width=200)
        datalength_label=Button(text="Data Length",fg="red",bg="White",font=('times new roman',20,"bold"),relief='solid',state="disabled").place(x=530,y=80,width=200)
        not_null_label=Button(text="Not  Null",fg="red",bg="White",font=('times new roman',20,"bold"),relief='solid',state="disabled").place(x=740,y=80,width=200)
        pk_label=Button(text="PK",fg="red",bg="White",font=('times new roman',20,"bold"),relief='solid',state="disabled").place(x=950,y=80,width=200)
        fk_label=Button(text="FK",fg="red",bg="White",font=('times new roman',20,"bold"),relief='solid',state="disabled").place(x=1170,y=80,width=200)
        last_frame=Frame(self.root,bd=0,bg='white')
        last_frame.place(x=0,y=650,width=1500,height=150)
        cancel_new_entry_btn=Button(root,text="Cancel",font=("times new roman",20,"bold"),fg="black",bg="Red",bd=5,cursor="hand2",command=self.create_table)
        cancel_new_entry_btn.place(x=500,y=700,width=200)
        submit_new_entry_btn=Button(root,text="Create Table",font=("times new roman",20,"bold"),fg="black",bg="Green",bd=5,cursor="hand2",command=self.submit_alter_add_column_data)
        submit_new_entry_btn.place(x=900,y=700,width=200)
    def alter_modify_column(self):
        var=StringVar()
        self.attribute_name_list=[]
        self.create_table_frame=Frame(self.root,bd=0,bg='white')
        self.create_table_frame.place(x=0,y=0,width=1500,height=150)
        self.new_entry_btn=Button(self.root,text="Add Column",font=("times new roman",20,"bold"),fg="White",bg="yellow",bd=5,cursor="hand2",command=self.new_entry_box)
        self.new_entry_btn.place(x=1200,y=10,width=200)
        self.l1=Frame(self.root,bg='yellow',bd=0)
        self.l1.place(x=0,y=150,width=1500,height=500)
        self.canvas=Canvas(self.l1,height=500,bg='white',bd=0)
        self.new_frame=Frame(self.canvas,width=1500,bg='white',height=500,bd=0)
        self.myscrollbar=Scrollbar(self.l1,orient="vertical",command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.myscrollbar.set)
        self.myscrollbar.pack(side="right",fill="y")
        self.canvas.place(x=0,y=0,width=1500,height=500)
        self.canvas.create_window((0,0),window=self.new_frame,anchor='nw')
        self.new_frame.bind("<Configure>",lambda e:self.canvas.configure(scrollregion = self.canvas.bbox('all')))
        var.set(self.alter_exist_table.get())
        table_name=Label(self.create_table_frame,text="New Table Name : ",font=('times new roman',20,"bold"),bg='white',fg='Green').place(x=250,y=10,width=250)       
        self.table_name_txt=Entry(self.create_table_frame,textvariable=var,font=('times new roman',20),bg='lightgray',fg="red")
        self.table_name_txt.place(x=500,y=10,width=200) 
        attribute_label=Button(text="Attribute Name",fg="red",bg="White",font=('times new roman',20,"bold"),relief='solid',state="disabled").place(x=50,y=80,width=200)
        datatype_label=Button(text="Data Type",fg="red",bg="White",font=('times new roman',20,"bold"),relief='solid',state="disabled").place(x=319,y=80,width=200)
        datalength_label=Button(text="Data Length",fg="red",bg="White",font=('times new roman',20,"bold"),relief='solid',state="disabled").place(x=530,y=80,width=200)
        not_null_label=Button(text="Not  Null",fg="red",bg="White",font=('times new roman',20,"bold"),relief='solid',state="disabled").place(x=740,y=80,width=200)
        pk_label=Button(text="PK",fg="red",bg="White",font=('times new roman',20,"bold"),relief='solid',state="disabled").place(x=950,y=80,width=200)
        fk_label=Button(text="FK",fg="red",bg="White",font=('times new roman',20,"bold"),relief='solid',state="disabled").place(x=1170,y=80,width=200)
        last_frame=Frame(self.root,bd=0,bg='white')
        last_frame.place(x=0,y=650,width=1500,height=150)
        cancel_new_entry_btn=Button(root,text="Cancel",font=("times new roman",20,"bold"),fg="black",bg="Red",bd=5,cursor="hand2",command=self.alter_table)
        cancel_new_entry_btn.place(x=500,y=700,width=200)
        submit_new_entry_btn=Button(root,text="Create Table",font=("times new roman",20,"bold"),fg="black",bg="Green",bd=5,cursor="hand2",command=self.submit_alter_modify_column_data)
        submit_new_entry_btn.place(x=900,y=700,width=200)
        home_btn=Button(root,text="HOME",font=("times new roman",20,"bold"),fg="White",bg="skyblue",bd=5,cursor="hand2",command=self.alter_table).place(x=0,y=10,width=150)
    def alter_drop_column(self):
        if(self.alter_columns_of_table.get()==''):
            messagebox.showerror("Error","Select Column First")
        else:
            main_sql='ALTER TABLE '+str(self.alter_exist_table.get())+' DROP COLUMN '+str(self.alter_columns_of_table.get())
            try:
                with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(main_sql)
                        connection.commit()
                        messagebox.showinfo("Sucess","Column Is Dropped Sucessfully",parent=self.root)
                        self.alter_table()
            except cx_Oracle.Error as error:
                messagebox.showerror("Error",error)
    def drop_selected_table(self):
        if(self.drop_exist_table.get()=="Exist Table List"):
             messagebox.showerror("Error","Select Table First")
        else:
            main_sql='DROP TABLE '+str(self.drop_exist_table.get())
            try:
                with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(main_sql)
                        connection.commit()
                        messagebox.showinfo("Sucess","Table Is Dropped Sucessfully",parent=self.root)
                        self.drop_table()
            except cx_Oracle.Error as error:
                messagebox.showerror("Error",error)
    def alter_rename_column(self):
        if(self.alter_columns_of_table.get()==''):
            messagebox.showerror("Error","Select Column First")
        else:
            renamed_column_name=simpledialog.askstring("Rename Column ","Enter New Name For Column : ")
            main_sql='ALTER TABLE '+str(self.alter_exist_table.get())+' RENAME COLUMN '+str(self.alter_columns_of_table.get())+' To '+str(renamed_column_name)
            print(main_sql)
            try:
                with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(main_sql)
                        connection.commit()
                        messagebox.showinfo("Sucess","Column Is Renamed Sucessfully",parent=self.root)
                        self.alter_table()
            except cx_Oracle.Error as error:
                messagebox.showerror("Error",error)
    def alter_rename_table(self):
        if(self.alter_exist_table.get()==''):
            messagebox.showerror("Error","Select Column First")
        else:
            new_table_name=simpledialog.askstring("Rename Table ","Enter New Name For Table : ")
            main_sql='ALTER TABLE '+str(self.alter_exist_table.get())+' RENAME TO '+str(new_table_name)
            try:
                with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(main_sql)
                        connection.commit()
                        messagebox.showinfo("Sucess","Table Is Renamed Sucessfully",parent=self.root)
                        self.alter_table()
            except cx_Oracle.Error as error:
                messagebox.showerror("Error",error)
    def submit_insert_tuple_data(self):
        val_attribute=[]
        for i in self.entries_list:
            val_attribute.append(i.get())
        try:
            main_sql="insert into "+self.insert_tuple_exist_table.get() +"(" + self.columnName_str+" ) values ( "+self.columnName_val_str+")"
            with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(main_sql,val_attribute)
                    connection.commit()
                    messagebox.showinfo("Sucess","Tuple Is Inserted Sucessfully",parent=self.root)
                    self.insert_tuple()
        except cx_Oracle.Error as error:
            messagebox.showerror("Error",error)
    def clear_insert_tuple(self):
        for i in self.entries_list:
            i.delete(0,END)
    def display_columns_constraint(self,event):
        column_name_arr=[]
        data_type_arr=[]
        nn_arr=[]
        pk_arr=[]
        fk_arr=[]
        self.entries_list=[]
        pk_val_list=["Primary Key List"]
        self.columnName_str=""
        self.columnName_val_str=""
        self.column_frame=Frame(self.insert_tuple_frame,bd=0,bg='yellow')
        self.column_frame.place(x=0,y=150,width=1500,height=600)
        cancel_insert_tuple_btn=Button(self.column_frame,text="Cancel",font=("times new roman",20,"bold"),fg="black",bg="Red",bd=5,cursor="hand2",command=self.clear_insert_tuple)
        cancel_insert_tuple_btn.place(x=500,y=500,width=200)
        submit_insert_tuple_btn=Button(self.column_frame,text="INSERT TUPLE",font=("times new roman",20,"bold"),fg="black",bg="Green",bd=5,cursor="hand2",command=self.submit_insert_tuple_data)
        submit_insert_tuple_btn.place(x=900,y=500,width=250)
        try:
            with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
               with connection.cursor() as cursor:
                   cursor.execute(("SELECT column_name,data_type,nullable FROM all_tab_columns where table_name = :txt_table_name"),[self.insert_tuple_exist_table.get()])
                   rows3=cursor.fetchall()
                   connection.commit()                
        except cx_Oracle.Error as error:
           messagebox.showerror("Error",error)
        for r in rows3:
            column_name_arr.append(r[0])
            data_type_arr.append(r[1])
            if(r[2]=="N"):
                nn_arr.append("NOT NULL")
            else:
                nn_arr.append("NULLABLE")
        try:
           with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
               with connection.cursor() as cursor:
                   cursor.execute(("SELECT cols.column_name FROM all_constraints cons, all_cons_columns cols WHERE cols.table_name =:txt_table_name AND cons.constraint_type = 'P' AND cons.constraint_name = cols.constraint_name AND cons.owner = cols.owner"),[self.insert_tuple_exist_table.get()])
                   rows2 = cursor.fetchall()
                   connection.commit()                
        except cx_Oracle.Error as error:
           messagebox.showerror("Error",error)
        for i in rows2:
            for j in i:
                pk_arr.append(j)
        try:
           with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
               with connection.cursor() as cursor:
                   cursor.execute(("SELECT cols.column_name FROM all_constraints cons, all_cons_columns cols WHERE cols.table_name =:txt_table_name AND cons.constraint_type = 'R' AND cons.constraint_name = cols.constraint_name AND cons.owner = cols.owner ORDER BY cols.table_name, cols.position"),[self.insert_tuple_exist_table.get()])
                   rows3=cursor.fetchall()
                   connection.commit()                
        except cx_Oracle.Error as error:
           messagebox.showerror("Error",error)
        for i in rows3:
            for j in i:
                fk_arr.append(j)
        try:
          with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
              with connection.cursor() as cursor:
                  sql="select "+pk_arr[0]+" from "+self.insert_tuple_exist_table.get()
                  cursor.execute(sql)
                  rows4=cursor.fetchall()
                  connection.commit()                
        except cx_Oracle.Error as error:
           messagebox.showerror("Error",error)
        for i in rows4:
            for j in i:
                pk_val_list.append(j)
            
        for i in range(len(column_name_arr)):
            pk=''
            fk=''
            if(column_name_arr[i] in pk_arr):
                pk="PRIMARY KEY"
            if(column_name_arr[i]in fk_arr):
                fk="FOREIGN KEY"
            newButton = Button(self.column_frame, text=column_name_arr[i],bg="white",state="disabled")
            newButton.grid(row=0,column=i,padx=10,pady=10)
            entry=Entry(self.column_frame,bg='white',fg="black")
            entry.grid(row=2,column=i,padx=10,pady=10)
            self.entries_list.append(entry)      
            newLabel=Label(self.column_frame,text=pk+"\n"+fk+"\n"+data_type_arr[i]+"\n"+nn_arr[i],bg="white")
            newLabel.grid(row=1,column=i,padx=10,pady=10)
            
        insert_tuple_exist_table=ttk.Combobox(self.column_frame,font=('times now roman',13),justify=CENTER)
        insert_tuple_exist_table['values']=pk_val_list
        insert_tuple_exist_table.grid(row=0,column=i+1)
        insert_tuple_exist_table.current(0)
        
        for i in range(len(column_name_arr)):
            self.columnName_str = self.columnName_str + column_name_arr[i]
            self.columnName_val_str =self.columnName_val_str+":"+column_name_arr[i]
            if(i != len(column_name_arr)-1):
                 self.columnName_str = self.columnName_str + ","
                 self.columnName_val_str =self.columnName_val_str +","
    def whereClause(self,event):
        if(self.where_oprands.get()==">" or self.where_oprands.get()==">=" or self.where_oprands.get()=="<" or self.where_oprands.get()=="<=" or self.where_oprands.get()=="="  or self.where_oprands.get()=="!="):
            messagebox.showinfo("Where Clause Clue Additional Information","Please Enter Single Value In Entry Box")
        if(self.where_oprands.get()=="IN" or self.where_oprands.get()=="NOT IN" or self.where_oprands.get()=="ANY" or self.where_oprands.get()=="ALL" ):
            messagebox.showinfo("Where Clause Clue Additional Information","You Can Enter Multiple Comma Seperated Values In Entry Box")
        if(self.where_oprands.get()=="BETWEEN" or self.where_oprands.get()=="NOT BETWEEN" ):
            messagebox.showinfo("Where Clause Clue Additional Information","Enter Only two(Lower value first and Higher value later) Comma Seperated Values In Entry Box")
        if(self.where_oprands.get()=="IS NULL" or self.where_oprands.get()=="IS NOT NULL" ):
            messagebox.showinfo("Where Clause Clue Additional Information","NO NEED TO ENTER VALUE IN ENTRY BOX")
    def where_sql(self):
        self.sql=""
        self.sql += " "+self.where_oprands.get()+" "
        if(self.where_oprands.get()==">" or self.where_oprands.get()==">=" or self.where_oprands.get()=="<" or self.where_oprands.get()=="<=" or self.where_oprands.get()=="="  or self.where_oprands.get()=="!="):
            self.sql += self.where_entry.get()
        elif(self.where_oprands.get()=="IN" or self.where_oprands.get()=="NOT IN" or self.where_oprands.get()=="ANY" or self.where_oprands.get()=="ALL" ):
            self.sql += "( "
            self.sql += self.where_entry.get()
            self.sql += " )"
        elif(self.where_oprands.get()=="BETWEEN" or self.where_oprands.get()=="NOT BETWEEN" ):
            low,high=self.where_entry.get().split(',')
            if(low > high):
                 (low,high)=(high,low)
            self.sql += str(low) + " AND " +str(high) 
        elif(self.where_oprands.get()==" IS NULL" or self.where_oprands.get()=="IS NOT NULL" ):
            self.sql += self.where_entry.get()    
    def submit_update_tuple_data(self):
        self.where_sql()
        main_sql=" update " +self.update_tuple_exist_table.get() +" set " + self.update_tuple_columns_of_table.get()+ " =:set_value " + " WHERE " + self.update_tuple_columns_of_table2.get()+ self.sql
        print(main_sql)
        try:
        # establish a new connection
            with cx_Oracle.connect(cfg.username,
                            cfg.password,
                            cfg.dsn,
                            encoding=cfg.encoding) as connection:
            # create a cursor
                with connection.cursor() as cursor:
                    # execute the insert statement
                    cursor.execute(main_sql, [self.set_entry.get()])
                    # commit the change
                    connection.commit()
                    messagebox.showinfo("Secessfull","Chnages Are Done Sucessfully")
                    self.alter_tuple()
        except cx_Oracle.Error as error:
            messagebox.showerror("Error",error)
    def submit_delete_tuple_data(self):
        self.where_sql()
        main_sql=" delete from " +self.delete_tuple_exist_table.get() + " WHERE " + self.delete_tuple_columns_of_table.get() +self.sql
        print(main_sql)
        try:
        # establish a new connection
            with cx_Oracle.connect(cfg.username,
                            cfg.password,
                            cfg.dsn,
                            encoding=cfg.encoding) as connection:
            # create a cursor
                with connection.cursor() as cursor:
                    # execute the insert statement
                    cursor.execute(main_sql)
                    # commit the change
                    connection.commit()
                    messagebox.showinfo("Secessfull","DELETED Sucessfully")
                    self.delete_tuple()
        except cx_Oracle.Error as error:
            messagebox.showerror("Error",error)
    def lookupAttribute(self,event):
        self.columns_of_selected_table=[]
        try:
           with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
               with connection.cursor() as cursor:
                   cursor.execute(("SELECT COLUMN_NAME FROM all_tab_columns where table_name =:txt_table_name"),[self.alter_exist_table.get()])
                   rows2=cursor.fetchall()
                   connection.commit()                
        except cx_Oracle.Error as error:
           messagebox.showerror("Error",error)
        for record in rows2:
            self.columns_of_selected_table.append(record)
        self.alter_columns_of_table['values']=self.columns_of_selected_table
    def delete_tuple_lookupattribute(self,event):
        self.columns_of_selected_table=[]
        try:
           with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
               with connection.cursor() as cursor:
                   cursor.execute(("SELECT COLUMN_NAME FROM all_tab_columns where table_name =:txt_table_name"),[self.delete_tuple_exist_table.get()])
                   rows2=cursor.fetchall()
                   connection.commit()                
        except cx_Oracle.Error as error:
           messagebox.showerror("Error",error)
        for record in rows2:
            self.columns_of_selected_table.append(record)
        self.delete_tuple_columns_of_table['values']=self.columns_of_selected_table
    def alter_tuple_lookupattribute(self,event):
        self.columns_of_selected_table=[]
        try:
           with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
               with connection.cursor() as cursor:
                   cursor.execute(("SELECT COLUMN_NAME FROM all_tab_columns where table_name =:txt_table_name"),[self.update_tuple_exist_table.get()])
                   rows2=cursor.fetchall()
                   connection.commit()                
        except cx_Oracle.Error as error:
           messagebox.showerror("Error",error)
        for record in rows2:
            self.columns_of_selected_table.append(record)
        self.update_tuple_columns_of_table['values']=self.columns_of_selected_table
        #self.update_tuple_columns_of_table.current(0)
        self.update_tuple_columns_of_table2['values']=self.columns_of_selected_table
        #self.update_tuple_columns_of_table2.current(0)
    def ShowupColumns(self,event):
        primary_key_list=[]
        foreign_key_list=[]
        display_attribute_list=[]
        try:
           with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
               with connection.cursor() as cursor:
                   cursor.execute(("SELECT cols.column_name FROM all_constraints cons, all_cons_columns cols WHERE cols.table_name =:txt_table_name AND cons.constraint_type = 'P' AND cons.constraint_name = cols.constraint_name AND cons.owner = cols.owner"),[self.alter_exist_table.get()])
                   rows2 = cursor.fetchall()
                   connection.commit()                
        except cx_Oracle.Error as error:
           messagebox.showerror("Error",error)
        for i in rows2:
            for j in i:
                primary_key_list.append(j)
        try:
           with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
               with connection.cursor() as cursor:
                   cursor.execute(("SELECT cols.column_name FROM all_constraints cons, all_cons_columns cols WHERE cols.table_name =:txt_table_name AND cons.constraint_type = 'R' AND cons.constraint_name = cols.constraint_name AND cons.owner = cols.owner ORDER BY cols.table_name, cols.position"),[self.alter_exist_table.get()])
                   rows3=cursor.fetchall()
                   connection.commit()                
        except cx_Oracle.Error as error:
           messagebox.showerror("Error",error)
        for i in rows3:
            for j in i:
                foreign_key_list.append(j)
        try:
            with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
               with connection.cursor() as cursor:
                   cursor.execute(("SELECT column_name,data_type,data_length,nullable FROM all_tab_columns where table_name = :txt_table_name"),[self.alter_exist_table.get()])
                   rows3=cursor.fetchall()
                   connection.commit()                
        except cx_Oracle.Error as error:
           messagebox.showerror("Error",error)
        for i in rows3:
            for j in i:
                display_attribute_list.append(str(j))
        if(display_attribute_list[0] in primary_key_list):
            display_attribute_list.append('YES')
        else:
            display_attribute_list.append('NO')
        if(display_attribute_list[0] in foreign_key_list):
            display_attribute_list.append('YES')
        else:
            display_attribute_list.append('NO') 
        self.datatype.set(display_attribute_list[1])
        self.datalengthsize.set(display_attribute_list[2])
        self.NotNull.set(display_attribute_list[3])
        self.PK.set(display_attribute_list[4])
        self.FK.set(display_attribute_list[5])
    def submit_create_table_data(self):
        sql_list=[]
        primary_key_list=[]
        foreign_key_list=[]
        main_sql=''
        main_sql='CREATE TABLE PD.'+str(self.table_name_txt.get())+'('
        for i in range(len(self.attribute_name_list)):
            sql=''
            sql += str(self.attribute_name_list[i][0].get())
            sql += ' '+str(self.attribute_name_list[i][1].get())
            if(self.attribute_name_list[i][2].get() and self.attribute_name_list[i][3].get()):
                sql += '('+str(self.attribute_name_list[i][2].get())+','+str(self.attribute_name_list[i][3].get())+')'
            elif(self.attribute_name_list[i][2].get()):
                sql += '('+str(self.attribute_name_list[i][2].get())+')'
            else:
                sql += ''
            if(self.attribute_name_list[i][4].get()):
                sql += ' NOT NULL'
            else:
                sql += ''
            if(self.attribute_name_list[i][5].get()):
                primary_key_list.append(self.attribute_name_list[i][0].get())
            else:
                sql += ''
            if(self.attribute_name_list[i][6].get()):
                foreign_key_list.append(self.attribute_name_list[i][0].get())
            else:
                sql += ''
                            
            if(i != len(self.attribute_name_list)-1):
                sql += ','
            sql_list.append(sql)
        for query in sql_list:
            main_sql += str(query)
        if(len(primary_key_list)):
            main_sql += ','+'PRIMARY KEY('
            for i in range(len(primary_key_list)):
                main_sql += str(primary_key_list[i])
                if(i != len(primary_key_list)-1):
                    main_sql += ','
            main_sql += ')'
        if(len(foreign_key_list)):
            main_sql += ','+'FOREIGN KEY('
            for i in range(len(foreign_key_list)):
                main_sql += str(foreign_key_list[i])
                if(i != len(foreign_key_list)-1):
                    main_sql += ','
            reference_table=simpledialog.askstring("Foreign Key Details","Foreign Key Reference Table Name")
            main_sql += ') REFERENCES '+str(reference_table)+'('
            for i in range(len(foreign_key_list)):
                main_sql += str(foreign_key_list[i])
                if(i != len(foreign_key_list)-1):
                    main_sql += ','
            main_sql += ')'
        main_sql += ')'
        print(main_sql)
        try:
            with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(main_sql)
                    connection.commit()
                    messagebox.showinfo("Sucess","Table Is Created Sucessfully",parent=self.root)
                    self.create_table()
        except cx_Oracle.Error as error:
            messagebox.showerror("Error",error)
    def submit_alter_add_column_data(self):
        sql_list=[]
        primary_key_list=[]
        foreign_key_list=[]
        main_sql=''
        main_sql='ALTER TABLE '+str(self.alter_exist_table.get())+' ADD'+'('
        for i in range(len(self.attribute_name_list)):
            sql=''
            sql += str(self.attribute_name_list[i][0].get())
            sql += ' '+str(self.attribute_name_list[i][1].get())
            if(self.attribute_name_list[i][2].get() and self.attribute_name_list[i][3].get()):
                sql += '('+str(self.attribute_name_list[i][2].get())+','+str(self.attribute_name_list[i][3].get())+')'
            elif(self.attribute_name_list[i][2].get()):
                sql += '('+str(self.attribute_name_list[i][2].get())+')'
            else:
                sql += ''
            print(self.attribute_name_list[i][4].get())
            if(self.attribute_name_list[i][4].get()):
                sql += ' NOT NULL'
            else:
                sql += ''
            if(self.attribute_name_list[i][5].get()):
                primary_key_list.append(self.attribute_name_list[i][0].get())
            else:
                sql += ''
            if(self.attribute_name_list[i][6].get()):
                foreign_key_list.append(self.attribute_name_list[i][0].get())
            else:
                sql += ''
                            
            if(i != len(self.attribute_name_list)-1):
                sql += ','
            sql_list.append(sql)
        for query in sql_list:
            main_sql += str(query)
        if(len(primary_key_list)):
            main_sql += ','+'PRIMARY KEY('
            for i in range(len(primary_key_list)):
                main_sql += str(primary_key_list[i])
                if(i != len(primary_key_list)-1):
                    main_sql += ','
            main_sql += ')'
        if(len(foreign_key_list)):
            main_sql += ','+'FOREIGN KEY('
            for i in range(len(foreign_key_list)):
                main_sql += str(foreign_key_list[i])
                if(i != len(foreign_key_list)-1):
                    main_sql += ','
            reference_table=simpledialog.askstring("Foreign Key Details","Foreign Key Reference Table Name")
            main_sql += ') REFERENCES '+str(reference_table)+'('
            for i in range(len(foreign_key_list)):
                main_sql += str(foreign_key_list[i])
                if(i != len(foreign_key_list)-1):
                    main_sql += ','
            main_sql += ')'
        main_sql += ')'
        print(main_sql)
        try:
            with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(main_sql)
                    connection.commit()
                    messagebox.showinfo("Sucess","Columns Are Added Sucessfully",parent=self.root)
                    self.alter_table()
        except cx_Oracle.Error as error:
            messagebox.showerror("Error",error)
    def submit_alter_modify_column_data(self):
        sql_list=[]
        primary_key_list=[]
        foreign_key_list=[]
        main_sql=''
        main_sql='ALTER TABLE '+str(self.alter_exist_table.get())+' MODIFY'+'('
        for i in range(len(self.attribute_name_list)):
            sql=''
            sql += str(self.attribute_name_list[i][0].get())
            sql += ' '+str(self.attribute_name_list[i][1].get())
            if(self.attribute_name_list[i][2].get() and self.attribute_name_list[i][3].get()):
                sql += '('+str(self.attribute_name_list[i][2].get())+','+str(self.attribute_name_list[i][3].get())+')'
            elif(self.attribute_name_list[i][2].get()):
                sql += '('+str(self.attribute_name_list[i][2].get())+')'
            else:
                sql += ''
            if(self.attribute_name_list[i][4].get()):
                sql += ' NOT NULL'
            else:
                sql += ''
            if(self.attribute_name_list[i][5].get()):
                primary_key_list.append(self.attribute_name_list[i][0].get())
            else:
                sql += ''
            if(self.attribute_name_list[i][6].get()):
                foreign_key_list.append(self.attribute_name_list[i][0].get())
            else:
                sql += ''
                            
            if(i != len(self.attribute_name_list)-1):
                sql += ','
            sql_list.append(sql)
        for query in sql_list:
            main_sql += str(query)
        if(len(primary_key_list)):
            main_sql += ','+'PRIMARY KEY('
            for i in range(len(primary_key_list)):
                main_sql += str(primary_key_list[i])
                if(i != len(primary_key_list)-1):
                    main_sql += ','
            main_sql += ')'
        if(len(foreign_key_list)):
            main_sql += ','+'FOREIGN KEY('
            for i in range(len(foreign_key_list)):
                main_sql += str(foreign_key_list[i])
                if(i != len(foreign_key_list)-1):
                    main_sql += ','
            reference_table=simpledialog.askstring("Foreign Key Details","Foreign Key Reference Table Name")
            main_sql += ') REFERENCES '+str(reference_table)+'('
            for i in range(len(foreign_key_list)):
                main_sql += str(foreign_key_list[i])
                if(i != len(foreign_key_list)-1):
                    main_sql += ','
            main_sql += ')'
        main_sql += ')'
        print(main_sql)
        try:
            with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(main_sql)
                    connection.commit()
                    messagebox.showinfo("Sucess","Table Is Modified  Sucessfully",parent=self.root)
                    self.alter_table()
        except cx_Oracle.Error as error:
            messagebox.showerror("Error",error)
    def new_entry_box(self):
        global z
        global r
        global radio
        global FK
        r=IntVar()
        radio=IntVar()
        FK=IntVar()
        z += 1
        self.entry=Entry(self.new_frame,font=('times new roman',15),bg='lightgray')
        self.entry.grid(row=z,column=1,padx=50,pady=10)
        self.combo=ttk.Combobox(self.new_frame,font=('times now roman',13),state='readonly',justify=CENTER)
        self.combo['values']=sorted((' Select DataType','VARCHAR2','NVARCHAR2','NUMBER','LONG','DATE','BINARY_FLOAT','BINARY_DOUBLE','RAW','LONG RAW','ROWID','CHAR','NCHAR','CLOB','NCLOB','BLOB','BFILE','TIMESTAMP','TIMESTAMP EITH TIME ZONE','INTERVAL YEAR TO MONTH','INTERVAL YEAR TO SECOND','UROWID','TIMESTAMP WITH LOCAL TIMEZONE'))
        self.combo.grid(row=z,column=2,padx=10,pady=10)  
        self.combo.current(0)
        self.datalength1_entry=Entry(self.new_frame,font=('times new roman',15),bg='lightgray',width=5)
        self.datalength1_entry.grid(row=z,column=3,padx=20,pady=10)
        self.datalength2_entry=Entry(self.new_frame,font=('times new roman',15),bg='lightgray',width=5)
        self.datalength2_entry.grid(row=z,column=4,padx=20,pady=10)
        self.r1=Radiobutton(self.new_frame,text="YES",variable=r,value=1,bg='white',borderwidth=10,fg='Green')
        self.r1.grid(row=z,column=5,padx=30,pady=10)
        self.r2=Radiobutton(self.new_frame,text="NO",variable=r,value=0,bg='white',borderwidth=10,fg='red')
        self.r2.grid(row=z,column=6,padx=0,pady=10)
        self.r3=Radiobutton(self.new_frame,text="YES",variable=radio,value=1,bg='white',borderwidth=10,fg='green')
        self.r3.grid(row=z,column=7,padx=60,pady=10)
        self.r4=Radiobutton(self.new_frame,text="NO",variable=radio,value=0,bg='white',borderwidth=10,fg='red')
        self.r4.grid(row=z,column=8,padx=0,pady=10)
        self.r5=Radiobutton(self.new_frame,text="YES",variable=FK,value=1,bg='white',borderwidth=10,fg='green')
        self.r5.grid(row=z,column=9,padx=50,pady=10)
        self.r6=Radiobutton(self.new_frame,text="NO",variable=FK,value=0,bg='white',borderwidth=10,fg='red')
        self.r6.grid(row=z,column=10,padx=0,pady=10)
        self.attribute_name_list.append([self.entry,self.combo,self.datalength1_entry,self.datalength2_entry,r,radio,FK])
    def login_window(self):
        self.background("Login Window")
        #login window_frame code
        self.login_window_frame=Frame(self.root,bg='white',bd=0)
        self.login_window_frame.place(x=550,y=30,width=450,height=750)
        #admin_image code
        self.adminimg=ImageTk.PhotoImage(file="images/adminlogo.png")
        img=Label(self.root, image = self.adminimg,bg='white').place(x=670,y=50,height=200,width=200)         
        #signin email code
        signin_email=Label(self.login_window_frame,text="Email :",font=('times new roman',15,"bold"),bg='white',fg='Gray').place(x=50,y=200)
        self.txt_signin_email=Entry(self.login_window_frame,font=('times new roman',15),bg='lightgray')
        self.txt_signin_email.place(x=50,y=230,width=350)    
        #signin password code
        signin_pass=Label(self.login_window_frame,text="Password :",font=('times new roman',15,"bold"),bg='white',fg='Gray').place(x=50,y=270)        
        self.txt_signin_pass=Entry(self.login_window_frame,font=('times new roman',15),bg='lightgray',show="*")
        self.txt_signin_pass.place(x=50,y=300,width=300)
        #code for show password and hide password
        self.show_password2=ImageTk.PhotoImage(file="images/show_password.png") 
        self.hide_password2=ImageTk.PhotoImage(file="images/hide_password.png")
        self.hide_chk2=IntVar()
        hide_chk2=Checkbutton(self.login_window_frame,image=self.hide_password2,selectimage=self.show_password2,indicatoron=False,onvalue=1,offvalue=0,bg='white',bd=0,variable=self.hide_chk2,command=lambda:self.hide_show_password(self.hide_chk2,self.txt_signin_pass)).place(x=360,y=300)
        #forgotten button code
        forget=Button(self.login_window_frame,text="forgotten password? ",bg="white",fg="red",bd=0,font=("times new roman",10),command=self.forget_password_window).place(x=50,y=330)
        #captcha code 
        captcha_label=Label(self.login_window_frame,text='Enter Captcha :',font=('times new roman',15,'bold'),bg='white',fg='Gray').place(x=50,y=360)
        self.refresh_captcha(self.login_window_frame,400,50)
        self.captcha_img=Entry(self.login_window_frame,font=('times new roman',50),bg='lightgray')
        self.captcha_img.place(x=240,y=400,width=170,height=60)
        self.refresh_btn=ImageTk.PhotoImage(file='images/refresh_btn.png')
        #refresh button for captcha code
        refresh_btn=Button(self.login_window_frame,image=self.refresh_btn,bg="white",cursor="hand2",command=lambda: self.refresh_captcha( self.login_window_frame,400,50)).place(x=200,y=360,width=30)
        #signin button
        sign_btn=Button(self.login_window_frame,text="LOGIN",font=("times new roman",20,"bold"),fg="White",bg="Green2",bd=5,cursor="hand2",command=self.signin_data).place(x=50,y=480,width=150)
        #clear button
        clear_btn=Button(self.login_window_frame,text="CLEAR",font=("times new roman",20,"bold"),fg="White",bg="red",bd=5,cursor="hand2",command=self.clear_login_window).place(x=250,y=480,width=150)
        #seperator image
        self.seperatorimg=ImageTk.PhotoImage(file="images/sep.png")
        seperatorimg=Label(self.login_window_frame, image = self.seperatorimg,bg='white').place(x=0,y=540,width=450)
        #OR label
        or_label=Label(self.login_window_frame,text="OR",font=('times new roman',25,"bold"),bg='white',fg='Black',justify='center').place(x=200,y=600)        
        #don't have an account label
        act_label=Label(self.login_window_frame,text="don't have an account?",font=('times new roman',15),bg='white',fg='Black',justify='center').place(x=130,y=640)        
        #signup button
        signup_btn=Button(self.login_window_frame,text="SIGNUP",font=("times new roman",20,"bold"),fg="White",bg="green",bd=6,cursor="hand2",command=self.registration_window).place(x=150,y=670,width=150)
    def registration_window(self):
        #background image
        self.background("Registration Window")
        #registration window  frame
        self.registration_window_frame=Frame(self.root,bg='white')
        self.registration_window_frame.place(x=540,y=50,width=600,height=700)
        title=Label(self.root,text="NEW REGISTERATION !!",font=('times new roman',20,"bold"),bg='white',fg='deepskyblue3').place(x=50,y=10)
        #username
        user_name=Label(self.registration_window_frame,text="Username :",font=('times new roman',15,"bold"),bg='white',fg='Gray').place(x=50,y=10)        
        self.txt_username=Entry(self.registration_window_frame,font=('times new roman',15),bg='lightgray')
        self.txt_username.place(x=250,y=10,width=300)    
        #first name 
        f_name=Label(self.registration_window_frame,text="Name :",font=('times new roman',15,"bold"),bg='white',fg='Gray').place(x=50,y=60)        
        self.txt_fname=Entry(self.registration_window_frame,font=('times new roman',15),bg='lightgray')
        self.txt_fname.place(x=250,y=60,width=300)    
        #last name label and entry
        l_name=Label(self.registration_window_frame,text="Surname :",font=('times new roman',15,"bold"),bg='white',fg='Gray').place(x=50,y=100)        
        self.txt_lname=Entry(self.registration_window_frame,font=('times new roman',15),bg='lightgray')
        self.txt_lname.place(x=250,y=100,width=300)
        #email label and entry
        email_name=Label(self.registration_window_frame,text="Email :",font=('times new roman',15,"bold"),bg='white',fg='Gray').place(x=50,y=140)        
        self.txt_email_name=Entry(self.registration_window_frame,font=('times new roman',15),bg='lightgray')
        self.txt_email_name.place(x=250,y=140,width=300)      
        # security question dropdown
        question=Label(self.registration_window_frame,text="Security Question :",font=('times new roman',15,"bold"),bg='white',fg='Gray').place(x=50,y=180)      
        self.cmb_question=ttk.Combobox(self.registration_window_frame,font=('times now roman',13),state='readonly',justify=CENTER)
        self.cmb_question['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_question.place(x=250,y=180,width=300)  
        self.cmb_question.current(0)   
        #security question's answer label and entry
        answer=Label(self.registration_window_frame,text="Answer :",font=('times new roman',15,"bold"),bg='white',fg='Gray').place(x=50,y=220)        
        self.txt_answer=Entry(self.registration_window_frame,font=('times new roman',15),bg='lightgray')
        self.txt_answer.place(x=250,y=220,width=300)     
        # password label and entry
        new_password=Label(self.registration_window_frame,text="Password :",font=('times new roman',15,"bold"),bg='white',fg='Gray').place(x=50,y=260)        
        self.txt_new_password=Entry(self.registration_window_frame,font=('times new roman',15),bg='lightgray',show="*")
        self.txt_new_password.place(x=250,y=260,width=300) 
        #show password and hide password button 
        self.show_password=ImageTk.PhotoImage(file="images/show_password.png") 
        self.hide_password=ImageTk.PhotoImage(file="images/hide_password.png")
        self.hide_chk=IntVar()
        hide_chk=Checkbutton(self.registration_window_frame,image=self.hide_password,selectimage=self.show_password,indicatoron=False,onvalue=1,offvalue=0,bg='white',bd=0,variable=self.hide_chk,command=lambda:self.hide_show_password(self.hide_chk,self.txt_new_password)).place(x=550,y=260)  
        #confirm password label  and entry
        confirm_password=Label(self.registration_window_frame,text="Confirm Password :",font=('times new roman',15,"bold"),bg='white',fg='Gray').place(x=50,y=300)        
        self.txt_confirm_password=Entry(self.registration_window_frame,font=('times new roman',15),bg='lightgray',show="*")
        self.txt_confirm_password.place(x=250,y=300,width=300)
        #captcha code
        captcha_label=Label(self.registration_window_frame,text='Enter Captcha :',font=('times new roman',15,'bold'),bg='white',fg='gray').place(x=50,y=340)
        self.refresh_captcha(self.registration_window_frame,370,50)
        self.refresh_btn=ImageTk.PhotoImage(file='images/refresh_btn.png')
        refresh_btn=Button(self.registration_window_frame,image=self.refresh_btn,bg="orange",cursor="hand2",command=lambda: self.refresh_captcha(self.registration_window_frame,370,50)).place(x=250,y=420,width=30)
        self.captcha_img=Entry(self.registration_window_frame,font=('times new roman',50),bg='lightgray')
        self.captcha_img.place(x=250,y=340,width=250,height=60)
        # terms and condition check button
        self.var_chk=IntVar()
        chk=Checkbutton(self.registration_window_frame,text="I agree to the terms & conditions ",onvalue=1,offvalue=0,bg='white',font=("times new roman",12),variable=self.var_chk).place(x=50,y=460)
        #submit button
        sub_btn=Button(self.registration_window_frame,text="SUBMIT",font=("times new roman",20,"bold"),fg="White",bg="orange",bd=5,cursor="hand2",command=self.register_data).place(x=50,y=500,width=150)
        #home button
        home_btn=Button(self.root,text="HOME",font=("times new roman",20,"bold"),fg="White",bg="skyblue",bd=5,cursor="hand2",command=self.login_window).place(x=50,y=50,width=150)
    def hide_show_password(self,variable,entry_name):
         if(variable.get()==1):
            entry_name.configure(show="")
         elif(variable.get()==0):
            entry_name.configure(show="*")
    def refresh_captcha(self,frame_name,Y,X):
        #Y=Y-axis distance from left
        #X=X-axis distance from top
        self.captcha_text = capt_demo.create_random_captcha_text(4)
        self.image_name=capt_demo.create_image_captcha(self.captcha_text)  
        load = Image.open(self.image_name)
        render = ImageTk.PhotoImage(load)
        img = Label(frame_name,image=render)
        img.image = render
        img.place(x=X,y=Y,width=150)
        os.remove(self.image_name)
    def forget_password_window(self):
        self.background('forget_password_window')
        #frame creation
        self.forget_password_window_frame=Frame(self.root,bg='white')
        self.forget_password_window_frame.place(x=540,y=50,width=400,height=500)
        #email name entry and label
        reset_email_label=Label(self.forget_password_window_frame,text="Enter registered email id : ",font=('times new roman',15),bg='white',fg='Black').place(x=50,y=50)        
        self.reset_email=Entry(self.forget_password_window_frame,font=('times new roman',15),bg='lightgray')
        self.reset_email.place(x=50,y=100,width=300)
        #reset email button 
        reset_btn=Button(self.forget_password_window_frame,text="SEND RESET EMAIL",font=("times new roman",20,"bold"),fg="White",bg="RED",bd=5,cursor="hand2",command=self.reset_forgotten_email).place(x=50,y=150,width=300)
        #reset email password entry and label 
        reset_email_pass_label=Label(self.forget_password_window_frame,text='Enter reset code here :',font=('times new roman',15),fg='black',bg='white').place(x=50,y=250)
        self.reset_email_pass=Entry(self.forget_password_window_frame,font=('times new roman',20,"bold"),bg='lightgray')
        self.reset_email_pass.place(x=50,y=300)
        # sign in button 
        sign_btn=Button(self.forget_password_window_frame,text="LOGIN NOW",font=("times new roman",20,"bold"),fg="White",bg="Green2",bd=5,cursor="hand2",command=self.forgotten_data_signin).place(x=50,y=370,width=200)
        #home button 
        home_btn=Button(self.root,text="HOME",font=("times new roman",20,"bold"),fg="White",bg="skyblue",bd=5,cursor="hand2",command=self.login_window).place(x=50,y=50,width=150)
    
    def forgotten_data_signin(self):
        if(self.reset_email_pass.get()==""):
            messagebox.showerror("Error","enter code first")
            return
        if(self.reset_email_pass.get()==self.captcha_text):
            sql=("select fname from login_data where email=:signin_email")
            try:
                with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(sql,[self.reset_email.get()])
                        row=cursor.fetchone()
                        if row:
                            messagebox.showinfo("Sucess","You have sucessfully logged in")
                            self.reset_email.delete(0,END)
                            self.reset_email_pass.delete(0,END)
                        else:
                            messagebox.showerror("Error","Entered email id doesn't exist")
                        connection.commit()                
            except cx_Oracle.Error as error:
                print(error)
        else:
            messagebox.showerror("error","Please enter vallid code")
    
    def reset_forgotten_email(self):
        if(self.reset_email.get()==""):
            messagebox.showerror("Error","Please enter email-id first")
            return
        sql=("select fname from login_data where email=:signin_email")
        try:
            with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
                with connection.cursor() as cursor:
                    cursor.execute(sql,[self.reset_email.get()])
                    row=cursor.fetchone()
                    if row:
                        self.captcha_text=emd.reset_email(self.reset_email.get())
                    else:
                        messagebox.showerror("Error","Entered email id doesn't exist")
                    connection.commit()                
        except cx_Oracle.Error as error:
            print(error)        

    def register_data(self):
        count=0
        if(self.txt_username.get()=="" or self.txt_fname.get() == "" or self.txt_lname.get() =="" or self.txt_email_name.get()=="" or self.cmb_question.get()=="Select" or self.txt_answer.get()=="" or self.txt_new_password.get()=="" or self.txt_confirm_password.get()=="" or self.captcha_img.get()==""):
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif(self.var_chk.get()==0):
            messagebox.showerror("Error","Please accept our termas and conditions",parent=self.root)
        else:
            if(not(self.txt_username.get().isalpha())):
                messagebox.showerror("Error","Enter Valid Username",parent=self.root)
                count=1
            if(not(self.txt_fname.get().isalpha())):
                messagebox.showerror("Error","Enter Valid Name",parent=self.root)
                count=1
            if(not(self.txt_lname.get().isalpha())): 
                count=1
                messagebox.showerror("Error","Enter Valid Surname",parent=self.root)
            if(len(self.txt_new_password.get())<8):
                messagebox.showerror("Error","use 8 characters or more for your password",parent=self.root)
                count=1
            if(len(self.txt_new_password.get())>=8):
                reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
                match_re=re.compile(reg) 
                if(re.search(match_re,self.txt_new_password.get())):
                    if(self.txt_new_password.get() != self.txt_confirm_password.get()):
                        count=1
                        messagebox.showerror("Error","Those password didn't match",parent=self.root)
                else:
                    count=1
                    messagebox.showerror("Error","Please choose a stronger password.Try a mix of letters,numbers and symbols",parent=self.root)
            reg2 ='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
            if(not(re.search(reg2,self.txt_email_name.get()))):
                 count=1
                 messagebox.showerror("Error","Invalid Email",parent=self.root)
            if(self.captcha_img.get() != self.captcha_text):
                count=1
                messagebox.showerror("Error","Captcha doesn't matched")
            
            if(count==0):
                try:
                    with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
                        with connection.cursor() as cursor:
                            cursor.execute("select uname from login_data where uname=:username",[self.txt_username.get()])
                            row =cursor.fetchone()
                            if(row):
                                messagebox.showerror("Error","Username Entered Is Already Exists. Try Another Username !!")
                                connection.commit()
                            cursor.execute("select email from login_data where email=:email",[self.txt_email_name.get()])
                            row =cursor.fetchone()
                            if(row):
                                messagebox.showerror("Error","Email-Id Entered Is Already Exists. Try Another Email-Id !!")
                                connection.commit()
                            else:
                                # execute the insert statement
                                cursor.execute("insert into Login_data (fname,lname,email,question,pwd,answer,uname) values(:2,:3,:4,:5,:6,:7,:8)", [self.txt_fname.get(),self.txt_lname.get(),self.txt_email_name.get(),self.cmb_question.get(),self.txt_new_password.get(),self.txt_answer.get(),self.txt_username.get()])
                                # commit work
                                connection.commit()
                                emd.login_email(self.txt_email_name.get())
                                messagebox.showinfo("Sucess","Register Secessful",parent=self.root)
                                self.clear_registration_window()
                except cx_Oracle.Error as error:
                   messagebox.showerror("Error",error)         
    def signin_data(self):        
        count=0
        if(self.txt_signin_email.get()=="" or self.txt_signin_pass.get()==""or self.captcha_img.get()=="" ):
            messagebox.showerror("Error","All fields are required ",parent=self.root)
        else:    
            reg2 ='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
            if(not(re.search(reg2,self.txt_signin_email.get()))):
                count=1
                messagebox.showerror("Error","Invalid Email",parent=self.root)
            if(self.captcha_img.get() != self.captcha_text):
                count=1
                messagebox.showerror("Error","Captcha doesn't matched")
            if(count==0):
                sql=("select fname from login_data where email=:signin_email and pwd=:pwd")
                try:
                    with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
                        with connection.cursor() as cursor:
                            cursor.execute(sql,[self.txt_signin_email.get(),self.txt_signin_pass.get()])
                            row=cursor.fetchone()
                            if row:
                                 self.menu_window()
                                 messagebox.showinfo("Sucess","You are logged in sucessfully",parent=self.root)
                            else:
                                 messagebox.showerror("Error","Invalid username or password")
                            connection.commit()                
                except cx_Oracle.Error as error:
                    messagebox.showerror("Error",error)         
    
    def menu_window(self):
        exist_table_list=['Exist Table List']
        try:
           with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
               with connection.cursor() as cursor:
                   cursor.execute("SELECT table_name FROM all_tables WHERE OWNER ='PD' ORDER BY table_name")
                   rows=cursor.fetchall()
                   connection.commit()                
        except cx_Oracle.Error as error:
           messagebox.showerror("Error",error)
        for record in rows:
            exist_table_list.append(record)
        self.background("Menu Window")
        self.my_menu=Menu(self.root)
        self.root.config(menu=self.my_menu)
        #file menu
        self.file_menu=Menu(self.my_menu,tearoff=0)
        self.my_menu.add_cascade(label="File",menu=self.file_menu)
        self.file_menu.add_command(label="Change Password",command=self.change_password)
        self.file_menu.add_command(label="Exit",command=self.exit_func)
        #DDL Menu
        self.ddl_menu=Menu(self.my_menu,tearoff=0)
        self.my_menu.add_cascade(label="DDL",menu=self.ddl_menu)
        self.ddl_menu.add_command(label="Create Table",command=self.create_table)
        self.ddl_menu.add_command(label="Alter Table",command=self.alter_table)
        self.ddl_menu.add_command(label="Drop Table",command=self.drop_table)
        self.ddl_menu.add_command(label="View Table Structure",command=self.view_table_structure)  
        #DML Menu
        self.dml_menu=Menu(self.my_menu,tearoff=0)
        self.my_menu.add_cascade(label="DML",menu=self.dml_menu)
        self.dml_menu.add_command(label="Insert Tuple",command=self.insert_tuple)
        self.dml_menu.add_command(label="Update Tuple",command=self.alter_tuple)
        self.dml_menu.add_command(label="Delete Tuple",command=self.delete_tuple)
        self.dml_menu.add_command(label="View Table Data",command=self.view_table_data)  
        #info menu
        self.info_menu=Menu(self.my_menu,tearoff=0)
        self.my_menu.add_cascade(label="INFO",command=self.print_info)  
    def exit_func(self):
        res=messagebox.askquestion('Exit Application', 'Do you really want to exit')
        if res == 'yes' :
            self.root.destroy()
        else :
            messagebox.showinfo('Return', 'Exit Operation Is Cancelled')
    
    def change_password(self):
        self.background("Change Password")
        self.change_password_frame=Frame(self.root,bg='white')
        self.change_password_frame.place(x=0,y=0,width=1500,height=1000)
        #new_password label and entry
        new_password=Label(self.change_password_frame,text=" New Password : ",font=('times new roman',15,"bold"),bg='white',fg='Black').place(x=250,y=210)        
        self.chg_new_password=Entry(self.change_password_frame,font=('times new roman',15),bg='lightgray',show="*")
        self.chg_new_password.place(x=500,y=210,width=250)
        #confirm password label and entry
        confirm_password=Label(self.change_password_frame,text=" Confirm Password : ",font=('times new roman',15,"bold"),bg='white',fg='Black').place(x=250,y=240)        
        self.chg_conf_password=Entry(self.change_password_frame,font=('times new roman',15),bg='lightgray',show="*")
        self.chg_conf_password.place(x=500,y=240,width=250)
        self.show_password=ImageTk.PhotoImage(file="images/show_password.png") 
        self.hide_password=ImageTk.PhotoImage(file="images/hide_password.png")
        self.hide_chk=IntVar()
        hide_chk=Checkbutton(self.change_password_frame,image=self.hide_password,selectimage=self.show_password,indicatoron=False,onvalue=1,offvalue=0,bg='white',bd=0,variable=self.hide_chk,command=lambda:self.hide_show_password(self.hide_chk,self.chg_new_password)).place(x=750,y=210)  
        #captcha creation
        captcha_label=Label(self.change_password_frame,text=' Enter Captcha :',font=('times new roman',15,'bold'),bg='white',fg='Black').place(x=250,y=270)
        self.refresh_captcha(self.change_password_frame,300,250)
        self.captcha_img=Entry(self.change_password_frame,font=('times new roman',50),bg='lightgray')
        self.captcha_img.place(x=500,y=270,width=250,height=60)
        self.refresh_btn=ImageTk.PhotoImage(file='images/refresh_btn.png')
        refresh_btn=Button(self.change_password_frame,image=self.refresh_btn,bg="orange",cursor="hand2",command=lambda: self.refresh_captcha( self.change_password_frame,300,250)).place(x=400,y=300,width=30)
        #change password button
        chg_pwd_btn=Button(self.change_password_frame,text="Change Password",font=("times new roman",20,"bold"),fg="White",bg="Red",bd=5,cursor="hand2",command=self.chg_pwd_fun).place(x=500,y=340,width=250)
    def chg_pwd_fun(self):
        count=0
        if(self.chg_new_password.get()=="" or self.chg_conf_password.get()==""):
            messagebox.showerror("Error","All fields are required !! ")
            count=1
            return
        if(len(self.chg_new_password.get())<8):
            messagebox.showerror("Error","use 8 characters or more for your password",parent=self.change_password_frame)
            count=1
        if(len(self.chg_new_password.get())>=8):
            reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
            match_re=re.compile(reg) 
            if(re.search(match_re,self.chg_new_password.get())):
                if(self.chg_new_password.get() != self.chg_conf_password.get()):
                    count=1
                    messagebox.showerror("Error","Those password didn't match",parent=self.change_password_frame)
            else:
                count=1
                messagebox.showerror("Error","Please choose a stronger password.Try a mix of letters,numbers and symbols",parent=self.change_password_frame)
        if(self.captcha_img.get() != self.captcha_text):
                count=1
                messagebox.showerror("Error","Captcha doesn't matched")
        if(count==0):
            try:
                with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
                    with connection.cursor() as cursor:
                        cursor.execute("update Login_data set PWD=:password where email=:email",[self.chg_new_password.get(),self.txt_signin_email.get()])
                        connection.commit()
                        messagebox.showinfo("Sucessful","Password Changed Sucessfully ",parent=self.change_password_frame)
                        self.chg_new_password.delete(0,END)
                        self.chg_conf_password.delete(0,END)
                        self.captcha_img.delete(0,END)
                        self.refresh_captcha(self.change_password_frame,300,250)
            except cx_Oracle.Error as error:
                print(error)
    def create_table(self):
        exist_table_list=['Exist Table List']
        try:
           with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
               with connection.cursor() as cursor:
                   cursor.execute("SELECT table_name FROM all_tables WHERE OWNER ='PD' ORDER BY table_name")
                   rows=cursor.fetchall()
                   connection.commit()                
        except cx_Oracle.Error as error:
           messagebox.showerror("Error",error)
        for record in rows:
            exist_table_list.append(record)
        self.background("Create Table")
        self.attribute_name_list=[]
        self.create_table_frame=Frame(self.root,bd=0,bg='white')
        self.create_table_frame.place(x=0,y=0,width=1500,height=150)
        self.new_entry_btn=Button(self.root,text="Add Atribute",font=("times new roman",20,"bold"),fg="White",bg="yellow",bd=5,cursor="hand2",command=self.new_entry_box)
        self.new_entry_btn.place(x=1200,y=10,width=200)
        self.l1=Frame(self.root,bg='yellow',bd=0)
        self.l1.place(x=0,y=150,width=1500,height=500)
        self.canvas=Canvas(self.l1,height=500,bg='white',bd=0)
        self.new_frame=Frame(self.canvas,width=1500,bg='white',height=500,bd=0)
        self.myscrollbar=Scrollbar(self.l1,orient="vertical",command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.myscrollbar.set)
        self.myscrollbar.pack(side="right",fill="y")
        self.canvas.place(x=0,y=0,width=1500,height=500)
        self.canvas.create_window((0,0),window=self.new_frame,anchor='nw')
        self.new_frame.bind("<Configure>",lambda e:self.canvas.configure(scrollregion = self.canvas.bbox('all')))
        table_name=Label(self.create_table_frame,text="New Table Name : ",font=('times new roman',20,"bold"),bg='white',fg='Green').place(x=50,y=10,width=250)       
        self.table_name_txt=Entry(self.create_table_frame,font=('times new roman',20),bg='lightgray',fg="red")
        self.table_name_txt.place(x=280,y=10,width=200) 
        attribute_label=Button(text="Attribute Name",fg="red",bg="White",font=('times new roman',20,"bold"),relief='solid',state="disabled").place(x=50,y=80,width=200)
        datatype_label=Button(text="Data Type",fg="red",bg="White",font=('times new roman',20,"bold"),relief='solid',state="disabled").place(x=319,y=80,width=200)
        datalength_label=Button(text="Data Length",fg="red",bg="White",font=('times new roman',20,"bold"),relief='solid',state="disabled").place(x=530,y=80,width=200)
        not_null_label=Button(text="Not  Null",fg="red",bg="White",font=('times new roman',20,"bold"),relief='solid',state="disabled").place(x=740,y=80,width=200)
        pk_label=Button(text="PK",fg="red",bg="White",font=('times new roman',20,"bold"),relief='solid',state="disabled").place(x=950,y=80,width=200)
        fk_label=Button(text="FK",fg="red",bg="White",font=('times new roman',20,"bold"),relief='solid',state="disabled").place(x=1170,y=80,width=200)
        exist_table=ttk.Combobox(font=('times now roman',13),state='readonly',justify=CENTER)
        exist_table['values']=exist_table_list
        print(len(exist_table_list))
        exist_table.place(x=700,y=10,width=200)
        exist_table.current(0)
        last_frame=Frame(self.root,bd=0,bg='white')
        last_frame.place(x=0,y=650,width=1500,height=150)
        cancel_new_entry_btn=Button(root,text="Cancel",font=("times new roman",20,"bold"),fg="black",bg="Red",bd=5,cursor="hand2",command=self.create_table)
        cancel_new_entry_btn.place(x=500,y=700,width=200)
        submit_new_entry_btn=Button(root,text="Create Table",font=("times new roman",20,"bold"),fg="black",bg="Green",bd=5,cursor="hand2",command=self.submit_create_table_data)
        submit_new_entry_btn.place(x=900,y=700,width=200)
    def alter_table(self):
        exist_table_list=[]
        self.attribute_name_list=[]
        exist_table_list.append(" Select")
        self.columns_of_selected_table=[]
        self.datatype=StringVar()
        self.datalengthsize=StringVar()
        self.NotNull=StringVar()
        self.PK=StringVar()
        self.FK=StringVar()
        try:
           with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
               with connection.cursor() as cursor:
                   cursor.execute("SELECT table_name FROM all_tables WHERE OWNER ='PD' ORDER BY table_name")
                   rows=cursor.fetchall()
                   connection.commit()                
        except cx_Oracle.Error as error:
           messagebox.showerror("Error",error)
        for record in rows:
            exist_table_list.append(record)
        self.background("Alter Table")
        self.alter_table_frame=Frame(self.root,bg="white",bd=0)
        self.alter_table_frame.place(x=0,y=0,width=1500,height=1000)
        wrapper=LabelFrame(self.root,bg="white",bd=0)
        wrapper.place(x=0,y=0,height=400,width=1500)
        wrapper2=LabelFrame(self.root,bg="white",bd=0)
        wrapper2.place(x=0,y=400,height=450,width=1500)
        Label(wrapper,text="Select Existing Table Name ").place(x=0,y=10)
        #exist_table_name=Label(wrapper,text="Existing Table Name : ",font=('times new roman',15,"bold"),bg='white',fg='Black').place(x=200,y=10)
        self.alter_exist_table=ttk.Combobox(wrapper,font=('times now roman',13),justify=CENTER)
        self.alter_exist_table['values']=exist_table_list
        self.alter_exist_table.place(x=350,y=10,width=200)
        self.alter_exist_table.current(0)
        self.alter_exist_table.bind("<<ComboboxSelected>>",self.lookupAttribute)
        Label(wrapper,text="Columns Of Selected Table : ").place(x=0,y=10)
        self.alter_columns_of_table=ttk.Combobox(wrapper,font=('times now roman',13),justify=CENTER)
        self.alter_columns_of_table.place(x=350,y=40,width=200)
        self.alter_columns_of_table.bind("<<ComboboxSelected>>",self.ShowupColumns)
        datatype_label=Label(wrapper2,text = "DataType")
        datatype_label.place(x=0,y=10,width=100)
        self.alter_datatype_entry=Entry(wrapper2,textvariable=self.datatype)
        self.alter_datatype_entry.place(x=0,y=50,width=100)
        datalength_label=Label(wrapper2,text = "Length")
        datalength_label.place(x=150,y=10)
        self.alter_datalength_entry=Entry(wrapper2,textvariable=self.datalengthsize)
        self.alter_datalength_entry.place(x=150,y=50)
        PK_label=Label(wrapper2,text = "Primary Key")
        PK_label.place(x=300,y=10)
        self.alter_PK_entry=Entry(wrapper2,textvariable=self.PK)
        self.alter_PK_entry.place(x=300,y=50)
        FK_label=Label(wrapper2,text = "Foreign Key")
        FK_label.place(x=450,y=10)
        self.alter_FK_entry=Entry(wrapper2,textvariable=self.FK)
        self.alter_FK_entry.place(x=450,y=50)
        NN_label=Label(wrapper2,text = "NULLABLE")
        NN_label.place(x=600,y=10)
        self.alter_NN_entry=Entry(wrapper2,textvariable=self.NotNull)
        self.alter_NN_entry.place(x=600,y=50)
        add_column_btn=Button(wrapper2,text="ADD COLUMNS",font=("times new roman",20,"bold"),fg="black",bg="Orange",bd=5,cursor="hand2",command=self.alter_add_column)
        add_column_btn.place(x=50,y=100,width=300)
        modify_column_btn=Button(wrapper2,text="MODIFY COLUMNS",font=("times new roman",20,"bold"),fg="black",bg="Orange",bd=5,cursor="hand2",command=self.alter_modify_column)
        modify_column_btn.place(x=50,y=150,width=300)
        drop_column_btn=Button(wrapper2,text="DROP COLUMNS",font=("times new roman",20,"bold"),fg="black",bg="Orange",bd=5,cursor="hand2",command=self.alter_drop_column)
        drop_column_btn.place(x=50,y=200,width=300)
        rename_column_btn=Button(wrapper2,text="RENAME COLUMN",font=("times new roman",20,"bold"),fg="black",bg="Orange",bd=5,cursor="hand2",command=self.alter_rename_column)
        rename_column_btn.place(x=50,y=250,width=300)
        rename_table_name_btn=Button(wrapper2,text="RENAME TABLE",font=("times new roman",20,"bold"),fg="black",bg="Orange",bd=5,cursor="hand2",command=self.alter_rename_table)
        rename_table_name_btn.place(x=50,y=300,width=300)
        
    def drop_table(self):
        exist_table_list=['Exist Table List']
        try:
           with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
               with connection.cursor() as cursor:
                   cursor.execute("SELECT table_name FROM all_tables WHERE OWNER ='PD' ORDER BY table_name")
                   rows=cursor.fetchall()
                   connection.commit()                
        except cx_Oracle.Error as error:
           messagebox.showerror("Error",error)
        for record in rows:
            exist_table_list.append(record)
        self.background("DROP TABLE")
        self.drop_table_frame=Frame(self.root,bg="white",bd=0)
        self.drop_table_frame.place(x=0,y=0,width=1500,height=1000)
        self.drop_exist_table=ttk.Combobox(self.drop_table_frame,font=('times now roman',13),justify=CENTER)
        self.drop_exist_table['values']=exist_table_list
        self.drop_exist_table.place(x=350,y=10,width=200)
        self.drop_exist_table.current(0)
        #self.drop_exist_table.bind("<<ComboboxSelected>>",self.drop_selected_table)
        drop_table_btn=Button(self.root,text="DROP TABLE",font=("times new roman",20,"bold"),fg="black",bg="Orange",bd=5,cursor="hand2",command=self.drop_selected_table)
        drop_table_btn.place(x=50,y=100,width=300)
    def view_table_structure(self):
        pass
    def insert_tuple(self):
        exist_table_list=[]
        self.attribute_name_list=[]
        exist_table_list.append(" Select")
        self.columns_of_selected_table=[]
        try:
           with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
               with connection.cursor() as cursor:
                   cursor.execute("SELECT table_name FROM all_tables WHERE OWNER ='PD' ORDER BY table_name")
                   rows=cursor.fetchall()
                   connection.commit()                
        except cx_Oracle.Error as error:
           messagebox.showerror("Error",error)
        for record in rows:
            exist_table_list.append(record)
        self.background("Insert Tuple")
        self.insert_tuple_frame=Frame(self.root,bg="white",bd=0)
        self.insert_tuple_frame.place(x=0,y=0,width=1500,height=1000)
        self.display_label=Label(self.root,text="Existing Table List : ",font=('times new roman',20,"bold"),bg="white")
        self.display_label.place(x=50,y=10,width=250)
        self.insert_tuple_exist_table=ttk.Combobox(self.root,font=('times now roman',13),justify=CENTER)
        self.insert_tuple_exist_table['values']=exist_table_list
        self.insert_tuple_exist_table.place(x=350,y=10,width=200)
        self.insert_tuple_exist_table.current(0)
        self.insert_tuple_exist_table.bind("<<ComboboxSelected>>",self.display_columns_constraint)
    def alter_tuple(self):
        exist_table_list=[]
        exist_table_list.append(" Select")
        try:
           with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
               with connection.cursor() as cursor:
                   cursor.execute("SELECT table_name FROM all_tables WHERE OWNER ='PD' ORDER BY table_name")
                   rows=cursor.fetchall()
                   connection.commit()                
        except cx_Oracle.Error as error:
           messagebox.showerror("Error",error)
        for record in rows:
            exist_table_list.append(record)
        self.background("Update Tuple")
        self.update_tuple_frame=Frame(self.root,bg="white",bd=0)
        self.update_tuple_frame.place(x=0,y=0,width=1500,height=1000)
        Label(self.root,text="UPDATE : ",font=('times new roman',20,"bold"),bg="white").place(x=50,y=50,width=250)
        self.update_tuple_exist_table=ttk.Combobox(self.root,font=('times now roman',13),justify=CENTER)
        self.update_tuple_exist_table['values']=exist_table_list
        self.update_tuple_exist_table.place(x=350,y=50,width=200)
        self.update_tuple_exist_table.current(0)
        self.update_tuple_exist_table.bind("<<ComboboxSelected>>",self.alter_tuple_lookupattribute)
        Label(self.root,text="SET : ",font=('times new roman',20,"bold"),bg="white").place(x=50,y=150,width=250)
        self.update_tuple_columns_of_table=ttk.Combobox(self.root,font=('times now roman',13),justify=CENTER)
        self.update_tuple_columns_of_table.place(x=350,y=150,width=200)
        self.set_entry=Entry(self.root,font=('times new roman',15),bg='white')
        self.set_entry.place(x=700,y=150,width=250)
        Label(self.root,text="WHERE : ",font=('times new roman',20,"bold"),bg="white").place(x=50,y=250,width=250)
        self.update_tuple_columns_of_table2=ttk.Combobox(self.root,font=('times now roman',13),justify=CENTER)
        self.update_tuple_columns_of_table2.place(x=350,y=250,width=200)
        self.where_oprands=ttk.Combobox(self.root,font=('times now roman',13),justify=CENTER)
        self.where_oprands['values']=["Select ","<",">","<=",">=","=","!=","BETWEEN","NOT BETWEEN","NOT IN","IN","IS NULL","IS NOT NULL","ANY","ALL"]
        self.where_oprands.place(x=700,y=250,width=200)
        self.where_oprands.current(0)
        self.where_oprands.bind("<<ComboboxSelected>>",self.whereClause)
        self.where_entry=Entry(self.root,font=('times new roman',15),bg='white')
        self.where_entry.place(x=1050,y=250,width=250)
        cancel_update_tuple_btn=Button(self.root,text="Cancel",font=("times new roman",20,"bold"),fg="black",bg="Red",bd=5,cursor="hand2",command=self.alter_tuple)
        cancel_update_tuple_btn.place(x=500,y=500,width=200)
        submit_update_tuple_btn=Button(self.root,text="ALTER TUPLE",font=("times new roman",20,"bold"),fg="black",bg="Green",bd=5,cursor="hand2",command=self.submit_update_tuple_data)
        submit_update_tuple_btn.place(x=900,y=500,width=250)
    def delete_tuple(self):
        exist_table_list=[]
        exist_table_list.append(" Select")
        try:
           with cx_Oracle.connect(cfg.username,cfg.password,cfg.dsn,encoding=cfg.encoding) as connection:
               with connection.cursor() as cursor:
                   cursor.execute("SELECT table_name FROM all_tables WHERE OWNER ='PD' ORDER BY table_name")
                   rows=cursor.fetchall()
                   connection.commit()                
        except cx_Oracle.Error as error:
           messagebox.showerror("Error",error)
        for record in rows:
            exist_table_list.append(record)
        self.background("Delete Tuple")
        self.delete_tuple_frame=Frame(self.root,bg="white",bd=0)
        self.delete_tuple_frame.place(x=0,y=0,width=1500,height=1000)
        Label(self.root,text="DELETE FROM ",font=('times new roman',20,"bold"),bg="white").place(x=0,y=150)
        self.delete_tuple_exist_table=ttk.Combobox(self.root,font=('times now roman',13),justify=CENTER)
        self.delete_tuple_exist_table['values']=exist_table_list
        self.delete_tuple_exist_table.place(x=250,y=150)
        self.delete_tuple_exist_table.current(0)
        self.delete_tuple_exist_table.bind("<<ComboboxSelected>>",self.delete_tuple_lookupattribute)
        Label(self.root,text="WHERE : ",font=('times new roman',20,"bold"),bg="white").place(x=500,y=150,width=250)
        self.delete_tuple_columns_of_table=ttk.Combobox(self.root,font=('times now roman',13),justify=CENTER)
        self.delete_tuple_columns_of_table.place(x=750,y=150,width=200)
        self.where_oprands=ttk.Combobox(self.root,font=('times now roman',13),justify=CENTER)
        self.where_oprands['values']=["Select ","<",">","<=",">=","=","!=","BETWEEN","NOT BETWEEN","NOT IN","IN","IS NULL","IS NOT NULL","ANY","ALL"]
        self.where_oprands.place(x=1000,y=150,width=200)
        self.where_oprands.current(0)
        self.where_oprands.bind("<<ComboboxSelected>>",self.whereClause)
        self.where_entry=Entry(self.root,font=('times new roman',15),bg='white')
        self.where_entry.place(x=1250,y=150,width=200)
        cancel_delete_tuple_btn=Button(self.root,text="Cancel",font=("times new roman",20,"bold"),fg="black",bg="Red",bd=5,cursor="hand2",command=self.delete_tuple)
        cancel_delete_tuple_btn.place(x=500,y=500,width=200)
        submit_delete_tuple_btn=Button(self.root,text="DELETE TUPLE",font=("times new roman",20,"bold"),fg="black",bg="Green",bd=5,cursor="hand2",command=self.submit_delete_tuple_data)
        submit_delete_tuple_btn.place(x=900,y=500,width=250)
    def view_table_data(self):
        pass
    def print_info(self):
        self.root.config(bg="white")
        self.info_label=ImageTk.PhotoImage(file='images/info.png')
        info_label=Label(self.root,image=self.info_label,bg="white").place(x=50,y=50,relwidth=1,relheight=1)
    def clear_registration_window(self):
         self.txt_username.delete(0,END)
         self.txt_fname.delete(0,END)
         self.txt_lname.delete(0,END)
         self.txt_email_name.delete(0,END)
         self.txt_new_password.delete(0,END)
         self.txt_confirm_password.delete(0,END)
         self.txt_answer.delete(0,END)
         self.cmb_question.current(0)
         self.captcha_img.delete(0,END)
         self.refresh_captcha(self.registration_window_frame,370,50)
    def clear_login_window(self):
        self.txt_signin_email.delete(0,END)
        self.txt_signin_pass.delete(0,END)
        
root=Tk()
obj=Register()
obj.login_window()
root.mainloop()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         
        
        
        
        
        
       
               
