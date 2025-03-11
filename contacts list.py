from tkinter import*
from tkinter import messagebox
from Arshdb import Database


win=Tk()
win.title("contacts")
win.geometry("500x490")
win.resizable(0,0)
win.config(bg="#2e8b57")
db1 =Database("D:/Arashpyt/dbproject.db")
#===============Func
def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_laddress.delete(0,END)
    ent_ltell.delete(0,END)
    ent_fname.focus_set()

def show_list():
    lst_name.delete(0,END)
    for row in db1.select_records():
        lst_name.insert(0,row)
        
def insert():
    if ent_fname.get()=="" or ent_lname.get()=="" or ent_laddress.get()=="" or ent_ltell.get()=="":
        eror_1=messagebox.showerror("Eror","You should fill all the blanks")
        return
    db1.insert(ent_fname.get(),ent_lname.get(),ent_laddress.get(),ent_ltell.get())
    clear()
    show_list()

def delete ():
    try:
        index=lst_name.curselection()[0]
        data= lst_name.get(index)
        record_id= data[0]
        db1.delete(record_id)
        clear()
        show_list()
    except:
        messagebox.showerror("error","no item selected")
def select_item(event):
    clear()
    index=lst_name.curselection()
    data=lst_name.get(index)
    ent_fname.insert(0, data[1])
    ent_lname.insert(0, data[2])
    ent_laddress.insert(0, data[3])
    ent_ltell.insert(0, data[4])

def update():
    global select_item
    index=lst_name.curselection()
    data=lst_name.get(index)
    db1.update(data[0],ent_fname.get(),ent_lname.get(),ent_laddress.get(),ent_ltell.get())
    show_list()

def exit():
    a1=messagebox.askquestion("Exit","Are you sure?")
    if a1=="yes":
        win.destroy()

def search():
    search_result=db1.search(ent_lsearch.get())
    if len(search_result)==0:
        messagebox.showerror("Eror","You should fill the blank")
        return
    lst_name.delete(0,END)
    for row in search_result:
        lst_name.insert(END,row)
    ent_lsearch.delete(0,END)
#===============widget
lbl_fname= Label(win,text="name:",font="calibry 19",bg="#2e8b57")
lbl_fname.place(x=7,y=10)
ent_fname=Entry(win,font='calibry 16',width=10)
ent_fname.place(x=95,y=13)

lbl_lname= Label(win,text="family:",font="calibry 19",bg="#2e8b57")
lbl_lname.place(x=7,y=60)
ent_lname=Entry(win,font='calibry 16',width=10)
ent_lname.place(x=95,y=63)

lbl_laddress= Label(win,text="address:",font="calibry 19",bg="#2e8b57")
lbl_laddress.place(x=225,y=10)
ent_laddress=Entry(win,font='calibry 16',width=10)
ent_laddress.place(x=330,y=13)

lbl_ltell= Label(win,text="phone:",font="calibry 19",bg="#2e8b57")
lbl_ltell.place(x=230,y=60)
ent_ltell=Entry(win,font='calibry 16',width=10)
ent_ltell.place(x=330,y=63)

lst_name=Listbox(win,font="20",width=41,height=10)
lst_name.place(x=15,y=150) 

ent_lsearch=Entry(win,font='calibry 16',width=30)
ent_lsearch.place(x=20,y=109)

lst_name.bind("<<ListboxSelect>>",select_item)
lst_name.bind()
#================Button
btn_insert=Button(win,text="Insert",font="arial 16",width=8,command= insert)
btn_insert.place (x=18,y=400)   

btn_update=Button(win,text="Update",font="arial 16 ",width=8,command=update)
btn_update.place (x=187,y=400)

btn_show=Button(win,text="Show",font="arial 16",width=8,command=show_list)
btn_show.place (x=364,y=400)

btn_delete=Button(win,text="Delete",font="arial 16",width=8,command=delete)
btn_delete.place (x=18,y=445)

btn_clear=Button(win,text="Clear",font="arial 16",width=8,command=clear)
btn_clear.place (x=187,y=445)

btn_exit=Button(win,text="Exit",font="arial 16",width=8,command= exit)
btn_exit.place (x=364,y=445)

btn_search=Button(win,text="Search",font="arial 16",bg="yellow",width=8,command=search)
btn_search.place (x=390,y=107)
win.mainloop()